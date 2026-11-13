#!/usr/bin/env python3
"""Runnable checks for three minimal models of the Millennium Prize Problems.

Every check verifies a statement that is a theorem inside a model, with one
exception: check 4 compares numbers with the Birch and Swinnerton-Dyer
conjecture itself. No check proves anything about an open problem.

Model 1  surface E x E with the curves H, V, D, G  -> Riemann, BSD, Hodge
Model 2  scale flow: one number per length scale   -> Poincare, Yang-Mills, Navier-Stokes
Model 3  counting queries and gates                -> P vs NP

The Poincare and Navier-Stokes parts of model 2 are closed-form formulas,
so this file computes nothing for them.

Run: python3 models_check.py   (needs numpy; takes about 2 minutes)
"""
import math
import time
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


def bsd_series(xmax=100_000):
    """Primes 2 < p <= xmax and, per curve, log of prod N_q / q over good primes q <= p.

    Skipped primes (2 and the bad prime) change only a constant factor.
    """
    ps = [p for p in primes_upto(xmax) if p > 2]
    logs = {k: np.zeros(len(ps)) for k in CURVES}
    big = np.arange(xmax, dtype=np.int64)
    for idx, p in enumerate(ps):
        xs = big[:p]
        chi = legendre_table(p, xs)
        x2 = xs * xs
        x3 = x2 * xs  # below 1e15, fits int64
        for name, (c2, c1, c0, bad, _) in CURVES.items():
            if p == bad:
                continue
            fx = x3 + c2 * x2 + c1 * xs + c0
            n_p = p + 1 + int(chi[(4 * fx + 1) % p].sum())
            logs[name][idx] = math.log(n_p / p)
    return np.array(ps, dtype=float), {k: np.cumsum(v) for k, v in logs.items()}


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


def check_x2y2(sizes=(20, 35, 50)):
    conv = [(m, float(x2y2_levels(m, 0, 0)[0]), float(x2y2_levels(m, 0, 0, 0.0)[0])) for m in sizes]
    m = sizes[-1]
    levels = sorted(
        float(e) for px, py in ((0, 0), (1, 1), (0, 1), (1, 0)) for e in x2y2_levels(m, px, py)
    )
    assert abs(conv[-1][1] - conv[-2][1]) < 1e-2 and conv[-1][1] > 1.0, conv
    assert conv[-1][2] < conv[0][2], conv  # free particle: no stable ground level
    return conv, levels[:4]


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


if __name__ == "__main__":
    t0 = time.time()
    curves, pairs, worst = check_hasse_via_hodge_index()
    print(f"[check 1] E over F_p, 5 <= p < 100: {curves} curves: 0 violations of a^2 < 4p; "
          f"max a^2/(4p) = {worst:.4f}")
    print(f"[check 2] {pairs} pairs (p, N_p): intersection form on H, V, D, G has signature (1, 3) for every pair")
    for name, (dh, dc) in check_hodge_on_torus().items():
        print(f"[check 3] E x E over C, {name}: rational (1,1) classes = {dh}, spanned by curves = {dc}")
    t1 = time.time()
    bsd = bsd_products()
    for name, (r, marks, slope) in bsd.items():
        print(f"[check 4] {name:7s} rank {r}: log prod N_p/p at X=1e3, 1e4, 1e5 = "
              f"{marks[0]:+.3f}, {marks[1]:+.3f}, {marks[2]:+.3f}; slope vs log log X = {slope:.2f}")
    print(f"[check 4] time {time.time() - t1:.0f} s")
    conv, levels = check_x2y2()
    for m, e0, free in conv:
        print(f"[check 5] basis {m}x{m}: E0(-Laplace + x^2 y^2) = {e0:.5f}; E0(free particle) = {free:.5f}")
    print(f"[check 5] lowest levels: {', '.join(f'{e:.5f}' for e in levels)}; gap = {levels[1] - levels[0]:.5f}")
    rows = check_queries()
    print(f"[check 6] OR_n, n = 1..{len(rows)}: deterministic queries = n, certificate for answer 1 = 1 bit")
    for n in (20, 30):
        print(f"[check 7] n = {n}: some function needs at least {shannon_min_gates(n)} gates; "
              f"best explicit bound 3.1*n = {3.1 * n:.0f}")
    report = Path(__file__).with_name("REPORT.md")
    if report.exists():  # the report must quote the numbers computed above
        quoted = [thousands(curves), str(pairs), pl(worst, 4), *(pl(v[2]) for v in bsd.values()),
                  pl(levels[0], 5), pl(levels[1], 5), pl(levels[1] - levels[0], 5),
                  thousands(shannon_min_gates(20))]
        missing = [q for q in quoted if q not in report.read_text(encoding="utf-8")]
        assert not missing, f"REPORT.md does not quote: {missing}"
        print(f"[report] REPORT.md quotes all {len(quoted)} computed numbers")
    print(f"all checks passed in {time.time() - t0:.0f} s")
