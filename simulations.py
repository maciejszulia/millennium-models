#!/usr/bin/env python3
"""Simulations for the minimal models: numerics only (numpy), no plotting.

models_check.py asserts the returned numbers (checks 9 to 12); animations.py draws them.

  curve_shortening   Poincare, one dimension lower: a closed curve shrinks, its area falls at rate 2*pi
  vorticity_2d       Navier-Stokes in two dimensions: enstrophy and maximal vorticity never grow
  classical_x2y2     Yang-Mills valleys: classical orbits of x^2 y^2 run far into the valleys
  sat_search         P vs NP: backtracking search on random 3-SAT grows exponentially with n
"""
import math
import random

import numpy as np


# --- Poincare: curve shortening flow, the one-dimensional relative of the Ricci flow ---


def _resample(z):
    """The same closed polygon with points at equal arc-length spacing."""
    closed = np.append(z, z[0])
    s = np.concatenate([[0.0], np.cumsum(np.abs(np.diff(closed)))])
    target = np.linspace(0, s[-1], z.size, endpoint=False)
    return np.interp(target, s, closed.real) + 1j * np.interp(target, s, closed.imag)


def polygon_area(z):
    return 0.5 * float(np.sum((np.conj(z) * np.roll(z, -1)).imag))


def polygon_length(z):
    return float(np.sum(np.abs(np.roll(z, -1) - z)))


def curve_shortening(points=160, frames=60, stop=0.9):
    """Flow dz/dt = curvature * normal for a closed non-convex curve, until `stop` of its lifetime.

    Theorem (Gage, Hamilton, Grayson): area(t) = area(0) - 2*pi*t and the curve becomes round.
    Returns times, areas, isoperimetric ratios L^2 / (4*pi*A) and the stored curves.
    """
    phi = np.linspace(0, 2 * np.pi, points, endpoint=False)
    z = _resample((1 + 0.45 * np.cos(3 * phi) + 0.2 * np.sin(2 * phi)) * np.exp(1j * phi))
    lifetime = polygon_area(z) / (2 * np.pi)
    t, times, areas, ratios, curves = 0.0, [], [], [], []
    for k in range(frames + 1):
        while t < k * stop * lifetime / frames:
            ahead, behind = np.roll(z, -1) - z, z - np.roll(z, 1)
            d1, d2 = np.abs(ahead), np.abs(behind)
            dt = min(0.2 * float(min(d1.min(), d2.min())) ** 2, k * stop * lifetime / frames - t)
            z = _resample(z + dt * 2 / (d1 + d2) * (ahead / d1 - behind / d2))  # second derivative in arc length
            t += dt
        area, length = polygon_area(z), polygon_length(z)
        times.append(t)
        areas.append(area)
        ratios.append(length**2 / (4 * np.pi * area))
        curves.append(z.copy())
    return np.array(times), np.array(areas), np.array(ratios), curves


# --- Navier-Stokes in two dimensions: vorticity on a torus, pseudo-spectral ---


def vorticity_2d(n=64, viscosity=0.01, steps=400, dt=0.02, every=10, seed=3):
    """Vorticity equation w_t + u.grad(w) = viscosity * laplace(w) on [0, 2*pi)^2, RK4, 2/3 dealiasing.

    Theorems for two dimensions without forcing: energy, enstrophy and max |w| never grow.
    Returns times, energies, enstrophies, max |w| and the stored vorticity fields.
    """
    k = np.fft.fftfreq(n, 1 / n)
    kx, ky = np.meshgrid(k, k, indexing="ij")
    k2 = kx**2 + ky**2
    inv = np.divide(1.0, k2, out=np.zeros_like(k2), where=k2 > 0)
    keep = (np.abs(kx) < n / 3) & (np.abs(ky) < n / 3)
    w = np.fft.ifft2(np.fft.fft2(np.random.default_rng(seed).standard_normal((n, n))) * np.exp(-k2 / 8) * keep).real
    w_hat = np.fft.fft2(6 * w / np.abs(w).max()) * keep  # smooth random vortices with max |w| = 6

    def velocity(w_hat):
        psi = w_hat * inv  # laplace(psi) = -w
        return np.fft.ifft2(1j * ky * psi).real, np.fft.ifft2(-1j * kx * psi).real

    def rhs(w_hat):
        u, v = velocity(w_hat)
        wx, wy = np.fft.ifft2(1j * kx * w_hat).real, np.fft.ifft2(1j * ky * w_hat).real
        return -np.fft.fft2(u * wx + v * wy) * keep - viscosity * k2 * w_hat

    times, energies, enstrophies, peaks, fields = [], [], [], [], []
    for step in range(steps + 1):
        if step % every == 0:
            w, (u, v) = np.fft.ifft2(w_hat).real, velocity(w_hat)
            times.append(step * dt)
            energies.append(0.5 * float(np.mean(u * u + v * v)))
            enstrophies.append(0.5 * float(np.mean(w * w)))
            peaks.append(float(np.abs(w).max()))
            fields.append(w)
        k1 = rhs(w_hat)
        k2_ = rhs(w_hat + 0.5 * dt * k1)
        k3 = rhs(w_hat + 0.5 * dt * k2_)
        k4 = rhs(w_hat + dt * k3)
        w_hat = w_hat + dt / 6 * (k1 + 2 * k2_ + 2 * k3 + k4)
    return np.array(times), np.array(energies), np.array(enstrophies), np.array(peaks), fields


# --- Yang-Mills valleys: classical orbits in the potential x^2 y^2 ---


GROUND_LEVEL = 1.10822  # E0 of -Laplace + x^2 y^2 from check 5, rounded; models_check.py asserts the match


def classical_x2y2(energy=GROUND_LEVEL, orbits=32, steps=50_000, dt=0.002, every=25, limit=30.0):
    """Orbits of H = px^2 + py^2 + x^2 y^2 that start at the origin with the given energy (leapfrog).

    The valleys are open, so an orbit close to an axis runs away: an orbit stops when it leaves
    the square |x|, |y| <= limit. Returns the positions (orbit, time, 2) and the largest
    relative energy drift.
    """
    angle = (np.arange(orbits) + 0.5) * (np.pi / 2) / orbits  # one quadrant of directions
    x, y = np.zeros(orbits), np.zeros(orbits)
    px, py = math.sqrt(energy) * np.cos(angle), math.sqrt(energy) * np.sin(angle)
    alive = np.ones(orbits, dtype=bool)
    path, drift = [], 0.0
    for step in range(steps):
        px = px - 0.5 * dt * 2 * x * y * y * alive
        py = py - 0.5 * dt * 2 * x * x * y * alive
        x = x + dt * 2 * px * alive
        y = y + dt * 2 * py * alive
        px = px - 0.5 * dt * 2 * x * y * y * alive
        py = py - 0.5 * dt * 2 * x * x * y * alive
        alive &= (np.abs(x) < limit) & (np.abs(y) < limit)
        if step % every == 0:
            path.append(np.stack([x, y], axis=1))
            drift = max(drift, float(np.abs(px * px + py * py + x * x * y * y - energy).max()) / energy)
    return np.stack(path, axis=1), drift


def ground_density(m, grid):
    """Density |psi_0(x, y)|^2 of the x^2 y^2 ground state on grid x grid, from an m x m oscillator basis."""
    from models_check import x2y2_hamiltonian

    coefficients = np.linalg.eigh(x2y2_hamiltonian(m, 0, 0))[1][:, 0].reshape(m, m)
    phi = np.zeros((2 * m, grid.size))  # normalised eigenfunctions of p^2 + x^2
    phi[0] = np.pi**-0.25 * np.exp(-grid * grid / 2)
    phi[1] = np.sqrt(2.0) * grid * phi[0]
    for n in range(1, 2 * m - 1):
        phi[n + 1] = np.sqrt(2.0 / (n + 1)) * grid * phi[n] - np.sqrt(n / (n + 1)) * phi[n - 1]
    return (phi[::2].T @ coefficients @ phi[::2]) ** 2


def quantum_mass_outside(m, box):
    """Probability that the x^2 y^2 ground state lies outside the square |x|, |y| <= box."""
    grid = np.linspace(-9, 9, 721)
    density = ground_density(m, grid)
    inside = np.abs(grid) <= box
    return 1.0 - float(density[np.ix_(inside, inside)].sum() / density.sum())


# --- P vs NP: backtracking search on random 3-SAT near the satisfiability threshold ---


def _search(clauses, assignment, counter):
    """DPLL with unit propagation; counter[0] counts the branching nodes."""
    assignment = dict(assignment)
    while True:  # unit propagation
        unit = None
        for clause in clauses:
            free, satisfied = [], False
            for lit in clause:
                value = assignment.get(abs(lit))
                if value is None:
                    free.append(lit)
                elif value == (lit > 0):
                    satisfied = True
                    break
            if satisfied:
                continue
            if not free:
                return None  # conflict
            if len(free) == 1:
                unit = free[0]
                break
        if unit is None:
            break
        assignment[abs(unit)] = unit > 0
    variables = {abs(lit) for clause in clauses for lit in clause}
    free = sorted(variables - assignment.keys())
    if not free:
        return assignment
    counter[0] += 1
    for value in (True, False):
        result = _search(clauses, {**assignment, free[0]: value}, counter)
        if result is not None:
            return result
    return None


def sat_search(sizes=(10, 15, 20, 25, 30, 35, 40), ratio=4.26, instances=25, seed=7):
    """Median number of branching nodes per size n, and the slope of log2(median) against n."""
    rng = random.Random(seed)
    medians = []
    for n in sizes:
        nodes = []
        for _ in range(instances):
            clauses = [[v * rng.choice((1, -1)) for v in rng.sample(range(1, n + 1), 3)]
                       for _ in range(round(ratio * n))]
            counter = [0]
            _search(clauses, {}, counter)
            nodes.append(counter[0])
        medians.append(float(np.median(nodes)))
    slope = float(np.polyfit(sizes, np.log2(np.maximum(medians, 1)), 1)[0])
    return list(sizes), medians, slope


if __name__ == "__main__":
    times, areas, ratios, _ = curve_shortening()
    law = areas[0] - 2 * np.pi * times
    print(f"curve shortening: area error {np.abs(areas - law).max() / areas[0]:.4f} of the first area; "
          f"isoperimetric ratio {ratios[0]:.3f} -> {ratios[-1]:.4f}")
    times, energies, enstrophies, peaks, _ = vorticity_2d()
    print(f"vorticity 2d: enstrophy {enstrophies[0]:.3f} -> {enstrophies[-1]:.3f}, largest increase "
          f"{np.diff(enstrophies).max():.2e}; max |w| {peaks[0]:.2f} -> {peaks[-1]:.2f}, largest {peaks.max():.3f}")
    path, drift = classical_x2y2()
    reach = np.abs(path).max(axis=(1, 2))
    outside = float((np.abs(path).max(axis=2) > 3).mean())
    print(f"classical x2y2: reach {reach.max():.2f} (median {np.median(reach):.2f}); time outside the box 3: "
          f"{outside:.4f}; quantum mass outside: {quantum_mass_outside(20, 3):.2e}; energy drift {drift:.1e}")
    sizes, medians, slope = sat_search()
    print(f"sat search: medians {medians}; slope {slope:.3f} bits per variable")
