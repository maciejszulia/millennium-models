#!/usr/bin/env python3
"""Runnable checks for three minimal models of the Millennium Prize Problems.

Every check verifies a statement that is a theorem inside a model, with one
exception: check 4 compares numbers with the Birch and Swinnerton-Dyer
conjecture itself. No check proves anything about an open problem.

Model 1  surface E x E with the curves H, V, D, G  -> Riemann, BSD, Hodge
Model 2  scale flow: one number per length scale   -> Poincare, Yang-Mills, Navier-Stokes
Model 3  counting queries and gates                -> P vs NP

Check 8 runs the counterexample thread of the two-thread algorithm for the
Riemann hypothesis. The Poincare and Navier-Stokes parts of model 2 are
closed-form formulas, so this file computes nothing for them.

Run: python3 models_check.py   (needs numpy; takes under 1 minute on 4 cores)
"""
import math
import os
import time
from concurrent.futures import ProcessPoolExecutor
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import numpy as np


def pl(x, nd=2):
    """Number with a decimal comma and without a negative zero, as the report prints it."""
    text = f"{x:.{nd}f}"
    if float(text) == 0:
        text = text.lstrip("-")
    return text.replace(".", ",").replace("-", "−")


def thousands(n):
    return f"{n:,}".replace(",", " ")


def primes_upto(n):
    sieve = np.ones(n + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i :: i] = False
    return [int(p) for p in np.flatnonzero(sieve)]


def legendre_table(p, xs):
    """chi[v] = Legendre symbol (v/p) for an odd prime p."""
    chi = np.full(p, -1, dtype=np.int64)
    chi[(xs * xs) % p] = 1
    chi[0] = 0
    return chi


# --- Model 1, checks 1 and 2: Hasse bound (Riemann hypothesis for E over F_p) from the Hodge index ---


def gram(deg_f, fixed_points):
    """Intersection matrix of H = E x pt, V = pt x E, D = diagonal, G = graph of f on E x E."""
    return [
        [0, 1, 1, deg_f],
        [1, 0, 1, 1],
        [1, 1, 0, fixed_points],
        [deg_f, 1, fixed_points, 0],
    ]


def det_exact(m):
    if len(m) == 1:
        return m[0][0]
    return sum(
        (-1) ** j * m[0][j] * det_exact([r[:j] + r[j + 1 :] for r in m[1:]])
        for j in range(len(m))
    )


def hasse_pairs(pmax=100):
    """Number of curves y^2 = x^3 + a*x + b over F_p, 5 <= p < pmax, per pair (p, #E(F_p))."""
    pairs = {}
    for p in primes_upto(pmax):
        if p < 5:
            continue
        xs = np.arange(p, dtype=np.int64)
        chi = legendre_table(p, xs)
        cube = (xs * xs % p) * xs % p
        bs = xs.reshape(-1, 1)
        for a in range(p):
            smooth = (4 * a**3 + 27 * xs * xs) % p != 0  # one flag per b
            n = p + 1 + chi[(cube + a * xs + bs) % p].sum(axis=1)  # #E(F_p) per b
            values, counts = np.unique(n[smooth], return_counts=True)
            for v, c in zip(values, counts):
                pairs[(p, int(v))] = pairs.get((p, int(v)), 0) + int(c)
    return pairs


def check_hasse_via_hodge_index(pmax=100):
    pairs = hasse_pairs(pmax)
    worst = 0.0
    for p, n in sorted(pairs):
        trace = p + 1 - n
        g = gram(p, n)
        assert trace * trace < 4 * p, (p, n)  # Hasse
        assert det_exact(g) == trace * trace - 4 * p, (p, n)
        ev = np.linalg.eigvalsh(np.array(g, dtype=float))
        assert (ev > 0).sum() == 1 and (ev < 0).sum() == 3, (p, n)  # Hodge index
        worst = max(worst, trace * trace / (4 * p))
    return sum(pairs.values()), len(pairs), worst


# --- Model 1, check 3: Hodge classes on E x E over C are classes of curves (Lefschetz (1,1)) ---


class K:
    """Element c0 + c1*s + c2*s^2 of Q(s), s^3 = 2."""

    __slots__ = ("c",)

    def __init__(self, c0=0, c1=0, c2=0):
        self.c = (Fraction(c0), Fraction(c1), Fraction(c2))

    def __add__(self, o):
        return K(*(x + y for x, y in zip(self.c, o.c)))

    def __sub__(self, o):
        return K(*(x - y for x, y in zip(self.c, o.c)))

    def __mul__(self, o):
        a, b = self.c, o.c
        return K(
            a[0] * b[0] + 2 * (a[1] * b[2] + a[2] * b[1]),
            a[0] * b[1] + a[1] * b[0] + 2 * a[2] * b[2],
            a[0] * b[2] + a[1] * b[1] + a[2] * b[0],
        )


PAIRS = list(combinations(range(4), 2))  # coordinates of an alternating form on Z^4


def hodge_equations(t, t_inv):
    """Rational rows of J^T A J = A on the lattice (Z + tau Z)^2, tau = i*t."""
    zero, one = K(0), K(1)
    jt = [[zero, zero - t], [t_inv, zero]]  # multiplication by i in the basis (1, tau)
    J = [[jt[i % 2][j % 2] if i // 2 == j // 2 else zero for j in range(4)] for i in range(4)]
    rows = []
    for i in range(4):
        for j in range(4):
            coeffs = []
            for k, l in PAIRS:
                v = J[k][i] * J[l][j] - J[l][i] * J[k][j]
                if (i, j) == (k, l):
                    v = v - one
                if (i, j) == (l, k):
                    v = v + one
                coeffs.append(v)
            for comp in range(3):  # a rational solution must kill every Q-component
                rows.append([c.c[comp] for c in coeffs])
    return rows


def rank(rows):
    rows = [[Fraction(x) for x in r] for r in rows if any(r)]
    r = 0
    for c in range(len(rows[0]) if rows else 0):
        piv = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c] / rows[r][c]
                rows[i] = [x - f * y for x, y in zip(rows[i], rows[r])]
        r += 1
    return r


def fibre_class(phi):
    """Class of a fibre of phi: Lambda^2 -> Lambda; phi[i] = (a, b) means a + b*tau."""
    return [phi[i][0] * phi[j][1] - phi[i][1] * phi[j][0] for i, j in PAIRS]


def graph_class(m):
    """Graph of the endomorphism with lattice matrix m: fibre of (u1, u2) -> u2 - m*u1."""
    return fibre_class([(-m[0][0], -m[1][0]), (-m[0][1], -m[1][1]), (1, 0), (0, 1)])


def intersect(a, b):
    return a[0] * b[5] - a[1] * b[4] + a[2] * b[3] + a[3] * b[2] - a[4] * b[1] + a[5] * b[0]


H = fibre_class([(0, 0), (0, 0), (1, 0), (0, 1)])
V = fibre_class([(1, 0), (0, 1), (0, 0), (0, 0)])
DIAG = graph_class([[1, 0], [0, 1]])
GRAPH_I = graph_class([[0, -1], [1, 0]])  # graph of multiplication by i (exists for tau = i)


def satisfies(rows, cls):
    return all(sum(r[k] * cls[k] for k in range(6)) == 0 for r in rows)


def check_hodge_on_torus():
    out = {}
    cases = (
        ("tau = i (CM)", K(1), K(1), [H, V, DIAG, GRAPH_I]),
        ("tau = i*2^(1/3) (no CM)", K(0, 1), K(0, 0, Fraction(1, 2)), [H, V, DIAG]),
    )
    for name, t, t_inv, curves in cases:
        rows = hodge_equations(t, t_inv)
        dim_hodge = 6 - rank(rows)
        assert all(satisfies(rows, c) for c in curves), name
        assert rank(curves) == dim_hodge, name
        out[name] = (dim_hodge, rank(curves))
    # negative control: the graph of "multiplication by i" is not a Hodge class without CM
    assert not satisfies(hodge_equations(K(0, 1), K(0, 0, Fraction(1, 2))), GRAPH_I)
    four = (H, V, DIAG, GRAPH_I)
    g = [[intersect(a, b) for b in four] for a in four]
    assert g == gram(1, 2), g  # deg(i) = 1, deg(1 - i) = 2: same matrix shape as over F_p
    return out


# --- Model 1, check 4: the original Birch and Swinnerton-Dyer product ---

CURVES = {  # y^2 + y = x^3 + c2*x^2 + c1*x + c0: (c2, c1, c0, bad prime, rank)
    "11a3": (-1, 0, 0, 11, 0),
    "37a1": (0, -1, 0, 37, 1),
    "389a1": (1, -2, 0, 389, 2),
    "5077a1": (0, -7, 6, 5077, 3),
}


def _bsd_logs(ps):
    """log(N_p / p) per curve (rows) and per prime of ps (columns); 0 at the bad prime."""
    coef = [(4 * c2, 4 * c1, 4 * c0 + 1, bad) for c2, c1, c0, bad, _ in CURVES.values()]
    logs = np.zeros((len(coef), len(ps)))
    big = np.arange(max(ps), dtype=np.int64)
    for idx, p in enumerate(ps):
        xs = big[:p]
        x2 = xs * xs
        chi = np.full(p, -1, dtype=np.int8)  # Legendre symbol table
        chi[x2 % p] = 1
        chi[0] = 0
        x3 = 4 * x2 * xs  # below 4e15, fits int64
        for j, (a2, a1, a0, bad) in enumerate(coef):
            if p == bad:
                continue
            v = x3 + a0  # 4*f(x) + 1: the discriminant of y^2 + y = f(x)
            if a2:
                v += a2 * x2
            if a1:
                v += a1 * xs
            logs[j, idx] = math.log((p + 1 + int(chi[v % p].sum(dtype=np.int64))) / p)
    return logs


def bsd_series(xmax=100_000, workers=None):
    """Primes 2 < p <= xmax and, per curve, log of prod N_q / q over good primes q <= p.

    Skipped primes (2 and the bad prime) change only a constant factor.
    The primes are dealt out to worker processes; the result does not depend on their number.
    """
    ps = [p for p in primes_upto(xmax) if p > 2]
    workers = min(workers or os.cpu_count() or 1, len(ps))
    logs = np.zeros((len(CURVES), len(ps)))
    with ProcessPoolExecutor(workers) as pool:
        for i, part in enumerate(pool.map(_bsd_logs, [ps[i::workers] for i in range(workers)])):
            logs[:, i::workers] = part
    return np.array(ps, dtype=float), dict(zip(CURVES, np.cumsum(logs, axis=1)))


def bsd_products(xmax=100_000, data=None):
    """Per curve: rank, log product at X = 1e3, 1e4, xmax, and the fitted slope against log log X."""
    arr, series = data or bsd_series(xmax)
    loglog = np.log(np.log(arr))
    fit = arr >= 100
    out = {}
    for name, (_, _, _, _, r) in CURVES.items():
        cum = series[name]
        marks = [float(cum[np.searchsorted(arr, x, side="right") - 1]) for x in (1e3, 1e4, xmax)]
        slope = float(np.polyfit(loglog[fit], cum[fit], 1)[0])
        out[name] = (r, marks, slope)
    slopes = [v[2] for v in out.values()]
    assert slopes == sorted(slopes) and len(set(slopes)) == 4, slopes
    return out


def sato_tate_distance(data=None, name="37a1"):
    """Check 14: Kolmogorov distance between a_p / (2 sqrt p) of one curve and the semicircle law.

    Returns the distance and the sorted values; the bad prime is left out.
    """
    primes, series = data or bsd_series()
    counts = np.rint(primes * np.exp(np.diff(series[name], prepend=0.0)))  # N_p back from log(N_p / p)
    keep = primes != CURVES[name][3]
    x = np.sort((primes[keep] + 1 - counts[keep]) / (2 * np.sqrt(primes[keep])))
    assert np.abs(x).max() < 1  # Hasse
    law = 0.5 + (x * np.sqrt(1 - x * x) + np.arcsin(x)) / np.pi
    return float(np.abs(np.arange(1, x.size + 1) / x.size - law).max()), x


# --- Model 2, check 5: x^2 y^2 quantum mechanics (Yang-Mills fields in a small box) ---


def x2_matrix(m, parity):
    """<n|x^2|n'> between eigenstates n = 2k + parity (k < m) of h = p^2 + x^2."""
    n = 2 * np.arange(m) + parity
    off = np.sqrt((n[:-1] + 1.0) * (n[:-1] + 2.0)) / 2.0
    return n, np.diag(n + 0.5) + np.diag(off, 1) + np.diag(off, -1)


def x2y2_hamiltonian(m, px, py, coupling=1.0):
    """-Laplace + coupling * x^2 y^2 in the product basis with parities px, py."""
    nx, ax = x2_matrix(m, px)
    ny, ay = x2_matrix(m, py)
    kx = np.diag(2.0 * nx + 1.0) - ax  # p_x^2 = h_x - x^2
    ky = np.diag(2.0 * ny + 1.0) - ay
    eye = np.eye(m)
    return np.kron(kx, eye) + np.kron(eye, ky) + coupling * np.kron(ax, ay)


def x2y2_levels(m, px, py, coupling=1.0, k=3):
    """Lowest Rayleigh-Ritz levels (upper bounds)."""
    return np.linalg.eigvalsh(x2y2_hamiltonian(m, px, py, coupling))[:k]


def abs_potential_ground_level(n=1201, half_width=10.0):
    """Lowest level of -d^2/dx^2 + |x| by finite differences; it bounds E0 of x^2 y^2 from below."""
    x = np.linspace(-half_width, half_width, n)
    step = x[1] - x[0]
    off = np.full(n - 1, -1.0 / step**2)
    return float(np.linalg.eigvalsh(np.diag(2.0 / step**2 + np.abs(x)) + np.diag(off, 1) + np.diag(off, -1))[0])


def check_x2y2(sizes=(12, 16, 20)):
    conv = [(m, float(x2y2_levels(m, 0, 0)[0]), float(x2y2_levels(m, 0, 0, 0.0)[0])) for m in sizes]
    m = sizes[-1]
    levels = sorted(
        float(e) for px, py in ((0, 0), (1, 1), (0, 1), (1, 0)) for e in x2y2_levels(m, px, py)
    )
    bound = abs_potential_ground_level()
    assert abs(conv[-1][1] - conv[0][1]) < 1e-5, conv  # the ground level has converged
    assert conv[-1][2] < conv[0][2], conv  # free particle: no stable ground level
    assert levels[0] >= bound > 1.0, (levels[0], bound)  # H >= (-Laplace + |x| + |y|) / 2
    return conv, levels[:4], bound


# --- Model 3, checks 6 and 7: query complexity and Shannon counting ---


def decision_tree_depth(f, n):
    """Exact deterministic query complexity D(f) by search over subcubes."""

    @lru_cache(maxsize=None)
    def depth(mask, val):
        free = [i for i in range(n) if not mask >> i & 1]
        seen = set()
        for bits in range(1 << len(free)):
            x = val
            for j, i in enumerate(free):
                if bits >> j & 1:
                    x |= 1 << i
            seen.add(f(x))
            if len(seen) > 1:
                break
        if len(seen) == 1:
            return 0
        return 1 + min(
            max(depth(mask | 1 << i, val), depth(mask | 1 << i, val | 1 << i)) for i in free
        )

    return depth(0, 0)


def certificate_one(f, n):
    """Largest, over inputs with f = 1, of the smallest set of bits that forces f = 1."""
    worst = 0
    for x in range(1 << n):
        if not f(x):
            continue
        for k in range(n + 1):
            masks = (sum(1 << i for i in c) for c in combinations(range(n), k))
            if any(all(f((y & ~m) | (x & m)) for y in range(1 << n)) for m in masks):
                worst = max(worst, k)
                break
    return worst


def shannon_min_gates(n):
    """Smallest s with (16*(n+s)^2)^s >= 2^(2^n); fewer gates cannot reach every function."""
    lo, hi = 1, 2**n
    while lo < hi:
        mid = (lo + hi) // 2
        if mid * (4 + 2 * math.log2(n + mid)) >= 2**n:
            hi = mid
        else:
            lo = mid + 1
    return lo


def check_queries(nmax=8):
    def f_or(x):
        return int(x != 0)

    rows = [(n, decision_tree_depth(f_or, n), certificate_one(f_or, n)) for n in range(1, nmax + 1)]
    assert all(d == n and c == 1 for n, d, c in rows), rows
    return rows


# --- Algorithm, check 8: the counterexample thread for the Riemann hypothesis ---


def lagarias_ratios(nmax=1_000_000):
    """sigma(n) / (H_n + exp(H_n) * log(H_n)) for n = 1..nmax.

    The Riemann hypothesis holds if and only if no ratio exceeds 1 (Lagarias 2002).
    """
    sigma = np.arange(nmax + 1, dtype=np.int64)  # the divisor d = n
    for d in range(1, nmax // 2 + 1):
        sigma[2 * d :: d] += d
    h = np.cumsum(1.0 / np.arange(1, nmax + 1))
    return sigma[1:] / (h + np.exp(h) * np.log(h))


def check_lagarias(ratios=None):
    """Largest ratio over n >= 2 (n = 1 gives equality): returns nmax, the n that attains it, the ratio."""
    ratios = lagarias_ratios() if ratios is None else ratios
    worst = int(np.argmax(ratios[1:])) + 2
    assert ratios[0] == 1.0 and ratios[worst - 1] < 1.0, (worst, ratios[worst - 1])
    return len(ratios), worst, float(ratios[worst - 1])


# --- Checks 9 to 12: the simulations; check 13: the zeta function behind the 3D figure ---


def check_simulations():
    """Numbers of the four simulations, each asserted against a theorem or a stated expectation."""
    import simulations as sim

    times, areas, ratios, _ = sim.curve_shortening()
    area_error = float(np.abs(areas - (areas[0] - 2 * np.pi * times)).max() / areas[0])
    assert area_error < 0.015 and ratios[-1] < 1.01 < ratios[0], (area_error, ratios[0], ratios[-1])  # check 9
    _, energies, enstrophies, peaks, _ = sim.vorticity_2d()
    assert np.diff(enstrophies).max() <= 0 and np.diff(energies).max() <= 0, "enstrophy and energy must not grow"
    assert peaks.max() <= peaks[0] * (1 + 1e-9), peaks.max()  # check 10: maximum principle
    assert abs(x2y2_levels(20, 0, 0)[0] - sim.GROUND_LEVEL) < 1e-5  # the orbits start with the energy E0
    path, drift = sim.classical_x2y2()
    reach = np.abs(path).max(axis=(1, 2))
    time_outside = float((np.abs(path).max(axis=2) > 3).mean())
    mass_outside = sim.quantum_mass_outside(20, 3)
    assert reach.min() > 3 and mass_outside < 0.01 and drift < 0.01, (reach.min(), mass_outside, drift)  # check 11
    sizes, medians, slope = sim.sat_search()
    assert slope > 0.05 and medians[-1] > 4 * medians[0], (slope, medians)  # check 12: exponential growth
    return {
        "area_error": area_error, "ratio_start": float(ratios[0]), "ratio_end": float(ratios[-1]),
        "enstrophy_start": float(enstrophies[0]), "enstrophy_end": float(enstrophies[-1]),
        "peak_start": float(peaks[0]), "peak_end": float(peaks[-1]),
        "orbits": int(reach.size), "orbits_at_limit": int((reach >= 30).sum()), "reach_min": float(reach.min()),
        "time_outside": time_outside, "mass_outside": mass_outside,
        "sat_sizes": sizes, "sat_medians": medians, "sat_slope": slope,
    }


def zeta(s, terms=120):
    """Riemann zeta on an array of complex s with Re s >= 0, s != 1 (Borwein's alternating series)."""
    d, acc = [], Fraction(0)
    for i in range(terms + 1):
        acc += Fraction(math.factorial(terms + i - 1) * 4**i, math.factorial(terms - i) * math.factorial(2 * i))
        d.append(terms * acc)
    s = np.asarray(s, dtype=complex)
    total = np.zeros(s.shape, dtype=complex)
    for k in range(terms):
        total += (-1) ** k * float((d[k] - d[terms]) / d[terms]) * np.exp(-s * math.log(k + 1))
    return -total / (1 - 2.0 ** (1 - s))


def zeta_zeros_on_line(tmax=40.0, step=0.001):
    """Heights t <= tmax where |zeta(1/2 + i*t)| has a local minimum below 0.01."""
    t = np.arange(step, tmax, step)
    size = np.abs(zeta(0.5 + 1j * t))
    low = (size[1:-1] < size[:-2]) & (size[1:-1] < size[2:]) & (size[1:-1] < 0.01)
    return [float(v) for v in t[1:-1][low]]


def check_zeta():
    known = [14.134725, 21.022040, 25.010858, 30.424876, 32.935062, 37.586178]  # first zeros, to 6 places
    assert abs(zeta(2.0) - np.pi**2 / 6) < 1e-12
    zeros = zeta_zeros_on_line()
    assert len(zeros) == len(known) and all(abs(a - b) < 2e-3 for a, b in zip(zeros, known)), zeros
    t = np.arange(0.5, 40, 0.01)
    off_line = float(min(np.abs(zeta(sigma + 1j * t)).min() for sigma in (0.25, 0.75)))
    assert off_line > 0.05, off_line  # no zero on these two lines for t < 40
    return zeros, off_line


if __name__ == "__main__":
    t0 = time.time()
    curves, pairs, worst = check_hasse_via_hodge_index()
    print(f"[check 1] E over F_p, 5 <= p < 100: {curves} curves: 0 violations of a^2 < 4p; "
          f"max a^2/(4p) = {worst:.4f}")
    print(f"[check 2] {pairs} pairs (p, N_p): intersection form on H, V, D, G has signature (1, 3) for every pair")
    for name, (dh, dc) in check_hodge_on_torus().items():
        print(f"[check 3] E x E over C, {name}: rational (1,1) classes = {dh}, spanned by curves = {dc}")
    t1 = time.time()
    data = bsd_series()
    bsd = bsd_products(data=data)
    distance, _ = sato_tate_distance(data)
    assert distance < 0.03, distance
    for name, (r, marks, slope) in bsd.items():
        print(f"[check 4] {name:7s} rank {r}: log prod N_p/p at X=1e3, 1e4, 1e5 = "
              f"{marks[0]:+.3f}, {marks[1]:+.3f}, {marks[2]:+.3f}; slope vs log log X = {slope:.2f}")
    print(f"[check 4] time {time.time() - t1:.0f} s")
    conv, levels, bound = check_x2y2()
    for m, e0, free in conv:
        print(f"[check 5] basis {m}x{m}: E0(-Laplace + x^2 y^2) = {e0:.5f}; E0(free particle) = {free:.5f}")
    print(f"[check 5] lowest levels: {', '.join(f'{e:.5f}' for e in levels)}; gap = {levels[1] - levels[0]:.5f}; "
          f"lower bound for E0 = {bound:.4f}")
    rows = check_queries()
    print(f"[check 6] OR_n, n = 1..{len(rows)}: deterministic queries = n, certificate for answer 1 = 1 bit")
    for n in (20, 30):
        print(f"[check 7] n = {n}: some function needs at least {shannon_min_gates(n)} gates; "
              f"best explicit bound 3.1*n = {3.1 * n:.0f}")
    nmax, worst_n, worst_ratio = check_lagarias()
    print(f"[check 8] Lagarias inequality, n = 2..{nmax}: 0 violations; largest ratio {worst_ratio:.4f} at n = {worst_n}")
    sim = check_simulations()
    print(f"[check 9] curve shortening: area error {100 * sim['area_error']:.2f} % of the first area; "
          f"isoperimetric ratio {sim['ratio_start']:.3f} -> {sim['ratio_end']:.4f}")
    print(f"[check 10] vorticity in 2 dimensions: enstrophy {sim['enstrophy_start']:.3f} -> {sim['enstrophy_end']:.3f}; "
          f"max |w| {sim['peak_start']:.2f} -> {sim['peak_end']:.2f}; neither grows")
    print(f"[check 11] classical orbits of x^2 y^2: {sim['orbits']} of {sim['orbits']} leave the square 3, "
          f"{sim['orbits_at_limit']} reach 30; time outside {100 * sim['time_outside']:.0f} %; "
          f"quantum mass outside {100 * sim['mass_outside']:.2f} %")
    print(f"[check 12] random 3-SAT search: median nodes {sim['sat_medians']}; slope {sim['sat_slope']:.3f} bits per variable")
    zeros, off_line = check_zeta()
    print(f"[check 13] zeta: {len(zeros)} zeros on the line for t < 40 at {', '.join(f'{z:.3f}' for z in zeros)}; "
          f"min |zeta| on the lines 0.25 and 0.75: {off_line:.3f}")
    print(f"[check 14] Sato-Tate for 37a1: distance to the semicircle law {distance:.4f}")
    report = Path(__file__).with_name("REPORT.md")
    if report.exists():  # the report must quote the numbers computed above
        quoted = [thousands(curves), str(pairs), pl(worst, 4), *(pl(v[2]) for v in bsd.values()),
                  pl(levels[0], 5), pl(levels[1], 5), pl(levels[1] - levels[0], 5), pl(bound, 4),
                  thousands(shannon_min_gates(20)), thousands(nmax), pl(worst_ratio, 4),
                  pl(100 * sim["area_error"], 2), pl(sim["ratio_end"], 4), pl(sim["enstrophy_start"], 3),
                  pl(sim["enstrophy_end"], 3), pl(100 * sim["mass_outside"], 2), pl(sim["sat_slope"], 3),
                  pl(zeros[0], 3), pl(off_line, 3), pl(distance, 4)]
        text = report.read_text(encoding="utf-8").replace("{,}", ",")  # LaTeX decimal comma
        missing = [q for q in quoted if q not in text]
        assert not missing, f"REPORT.md does not quote: {missing}"
        print(f"[report] REPORT.md quotes all {len(quoted)} computed numbers")
    print(f"all checks passed in {time.time() - t0:.0f} s")
