#!/usr/bin/env python3
"""Draw one figure per Millennium Prize Problem from the models in models_check.py.

Every number in a title comes from a function call, never from a typed constant.
Chart rules: the title states the finding, the subtitle says what is drawn,
the footer names the source. One font, straight lines, a validated palette.

Run: python3 figures.py   (needs numpy and matplotlib; takes about 2 minutes)
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.lines import Line2D

from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import models_check as mc
import simulations as sim
from models_check import pl, thousands

OUT = Path(__file__).parent / "figures"

# Light-surface chrome and the documented palette; checked with validate_palette.js.
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLUE, ORANGE, RED = "#2a78d6", "#eb6834", "#e34948"
RAMP = ["#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]  # one hue, ordinal steps, light to dark
SEQ = LinearSegmentedColormap.from_list(
    "seq", [SURFACE, "#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"]
)
SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
LINE, RING = 1.6, 1.3  # about 2 px at the rendered size


def style():
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 9.5, "mathtext.fontset": "dejavusans",
        "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
        "axes.edgecolor": AXIS, "axes.linewidth": 0.8, "axes.spines.top": False, "axes.spines.right": False,
        "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "grid.linestyle": "-",
        "axes.axisbelow": True, "axes.labelcolor": INK2, "axes.labelsize": 9, "text.color": INK,
        "xtick.color": AXIS, "ytick.color": AXIS, "xtick.labelcolor": INK2, "ytick.labelcolor": INK2,
        "xtick.labelsize": 8.5, "ytick.labelsize": 8.5, "lines.linewidth": LINE,
        "lines.solid_capstyle": "round", "lines.solid_joinstyle": "round",
        "legend.frameon": False, "legend.fontsize": 8.5, "legend.labelcolor": INK2,
    })


def comma_ticks(axis, nd=2):
    axis.set_major_formatter(lambda v, _: pl(v, nd))


def frame(title, subtitle, footer, ncols=1, width_ratios=None, sharey=False, height=5.4, projection=None):
    """Figure whose title is the finding, subtitle is what is drawn, footer is the source."""
    fig, axes = plt.subplots(1, ncols, figsize=(9.6, height), sharey=sharey,
                             gridspec_kw={"width_ratios": width_ratios},
                             subplot_kw={"projection": projection} if projection else None)
    unit = 5.4 / height  # text sizes are fixed in points, so the margins shrink as the figure grows

    def up(t):  # a position given for the default height, measured from the top edge
        return 1 - (1 - t) * unit

    sub_y = 0.962 - 0.052 * (title.count("\n") + 1)
    top = sub_y - 0.046 * (subtitle.count("\n") + 1) - 0.07
    fig.subplots_adjust(left=0.075, right=0.965, top=up(top), bottom=0.175 * unit, wspace=0.3)
    fig.text(0.03, up(0.962), title, fontsize=12.5, fontweight="bold", va="top", linespacing=1.25)
    fig.text(0.03, up(sub_y - 0.008), subtitle, fontsize=9.5, color=INK2, va="top", linespacing=1.35)
    fig.text(0.03, 0.028 * unit, footer, fontsize=8, color=MUTED, va="bottom", linespacing=1.35)
    return fig, list(np.atleast_1d(axes))


def panel_title(ax, text):
    ax.set_title(text, loc="left", fontsize=9, color=INK2, pad=7)


def save(fig, name):
    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / name, dpi=200)
    plt.close(fig)
    print("wrote", OUT / name)


def affine_points(c2, c1, c0, p):
    """Points (x, y) of y^2 + y = x^3 + c2*x^2 + c1*x + c0 over F_p."""
    xs = np.arange(p, dtype=np.int64)
    rhs = (xs * xs * xs + c2 * xs * xs + c1 * xs + c0) % p
    lhs = (xs * xs + xs) % p  # y^2 + y for y = xs
    return [(int(x), int(y)) for x in xs for y in np.flatnonzero(lhs == rhs[x])]


def figure_riemann():
    pairs = mc.hasse_pairs()
    p0 = 97
    points = affine_points(*mc.CURVES["37a1"][:3], p0)
    n0 = len(points) + 1  # plus the point at infinity
    fig, (left, right) = frame(
        f"Każda z {thousands(sum(pairs.values()))} krzywych leży wewnątrz granicy a² = 4p",
        f"Lewy panel: punkty 1 krzywej nad ciałem F{str(p0).translate(SUB)}. "
        f"Prawy panel: {len(pairs)} par (p, a) dla każdej krzywej eliptycznej\nnad ciałem o p elementach, "
        "p od 5 do 97 włącznie. Hipoteza Riemanna dla krzywej to nierówność a² ≤ 4p.",
        "Źródło: models_check.py, sprawdziany 1 i 2. a = p + 1 − N, gdzie N oznacza liczbę punktów krzywej "
        "razem z punktem w nieskończoności.",
        ncols=2, width_ratios=[0.8, 1.2],
    )
    left.scatter(*zip(*points), s=15, color=BLUE, edgecolors=SURFACE, linewidths=0.5, zorder=3)
    left.set(xlim=(-3, p0 + 2), ylim=(-3, p0 + 2), xlabel="x", ylabel="y", aspect="equal")
    panel_title(left, f"y² + y = x³ − x: N = {n0}, a = {pl(p0 + 1 - n0, 0)}")
    ps = np.array([p for p, _ in pairs])
    trace = np.array([p + 1 - n for p, n in pairs])
    right.scatter(ps, trace, s=13, color=BLUE, edgecolors=SURFACE, linewidths=0.5, zorder=3)
    grid = np.linspace(4, 100, 300)
    for sign, label in ((1, "a = 2√p"), (-1, "a = −2√p")):
        right.plot(grid, sign * 2 * np.sqrt(grid), color=INK2, lw=1.3, zorder=2)
        right.text(101.5, sign * 20, label, va="center", fontsize=8.5, color=INK2)
    right.set(xlim=(0, 118), xlabel="liczba pierwsza p", ylabel="a = p + 1 − N")
    panel_title(right, "Punkt = para (p, a), dla której istnieje co najmniej 1 krzywa")
    save(fig, "riemann-hasse-bound.png")


def figure_bsd(data):
    primes, series = data
    summary = mc.bsd_products(data=data)
    slopes = [summary[name][2] for name in mc.CURVES]
    fig, (ax,) = frame(
        "Nachylenie iloczynu rośnie z rangą krzywej: " + "; ".join(pl(s) for s in slopes),
        "Suma ln($N_p/p$) po liczbach pierwszych p ≤ X, na skali ln ln X. "
        "Hipoteza BSD przewiduje nachylenie równe randze.",
        f"Źródło: models_check.py, sprawdzian 4. {thousands(len(primes))} liczb pierwszych od 3 do "
        f"{thousands(int(primes[-1]))}. Nachylenie z dopasowania prostej dla X od 100 do 100 000.",
    )
    x = np.log(np.log(primes))
    shown = primes >= 10
    for color, (name, (rank, _, slope)) in zip(RAMP, summary.items()):
        y = series[name]
        ax.plot(x[shown], y[shown], color=color, label=f"{name}, ranga {rank}")
        ax.text(x[-1] + 0.02, y[-1], f"nachylenie {pl(slope)}", va="center", fontsize=8.5, color=INK2)
    marks = [10, 100, 1000, 10_000, 100_000]
    ax.set_xticks(np.log(np.log(marks)), ["10", "100", "1 000", "10 000", "100 000"])
    ax.set(xlim=(np.log(np.log(10)), x[-1] + 0.36), xlabel="X (skala ln ln X)", ylabel=r"suma ln$(N_p/p)$")
    ax.legend(loc="upper left", title="Krzywa", title_fontsize=8.5, alignment="left")
    save(fig, "bsd-product-slopes.png")


def figure_hodge():
    dims = list(mc.check_hodge_on_torus().values())  # (rational (1,1) classes, classes of curves)
    fig, axes = frame(
        "Krata kwadratowa wraca na siebie po obrocie o 90°, więc torus ma 4. krzywą",
        "Torus E = C/(Z + τZ). Mnożenie przez i obraca kratę o 90°. Liczba wymiernych klas typu (1,1) na E × E\n"
        f"równa się liczbie klas krzywych: {dims[0][0]} = {dims[0][1]} dla τ = i oraz "
        f"{dims[1][0]} = {dims[1][1]} dla τ = i × ∛2.",
        "Źródło: models_check.py, sprawdzian 3. G oznacza wykres mnożenia przez i.",
        ncols=2,
    )
    cases = ((1.0, "τ = i: obrót zachowuje kratę, krzywe H, V, D, G"),
             (2 ** (1 / 3), "τ = i × ∛2: obrót zmienia kratę, krzywe H, V, D"))
    for ax, (t, text) in zip(axes, cases):
        m, n = np.meshgrid(np.arange(-5, 6), np.arange(-5, 6))
        x, y = m.ravel().astype(float), n.ravel() * t
        inside = (np.abs(x) < 3.3) & (np.abs(y) < 3.3)  # no half-drawn markers at the frame
        x, y = x[inside], y[inside]
        ax.scatter(-y, x, s=90, facecolors="none", edgecolors=ORANGE, linewidths=LINE, zorder=2)
        ax.scatter(x, y, s=30, color=BLUE, edgecolors=SURFACE, linewidths=RING, zorder=3)
        ax.set(xlim=(-3.6, 3.6), ylim=(-3.6, 3.6), aspect="equal", xlabel="Re z", ylabel="Im z")
        ax.set_xticks(range(-3, 4))
        ax.set_yticks(range(-3, 4))
        panel_title(ax, text)
    handles = [
        Line2D([], [], marker="o", ls="", color=BLUE, markeredgecolor=SURFACE, markersize=7, label="punkt kraty"),
        Line2D([], [], marker="o", ls="", markerfacecolor="none", markeredgecolor=ORANGE, markeredgewidth=LINE,
               markersize=10, label="punkt kraty po mnożeniu przez i"),
    ]
    fig.legend(handles=handles, loc="lower right", bbox_to_anchor=(0.965, 0.02), ncol=2)
    save(fig, "hodge-lattice-rotation.png")


def figure_poincare():
    fractions = [0.0, 0.25, 0.5, 0.75]  # t / T
    labels = ["t = 0", "t = T/4", "t = T/2", "t = 3T/4"]
    colors = RAMP[::-1]  # dark at t = 0, light near the end
    fig, (left, right) = frame(
        "Okrągła sfera S³ kurczy się liniowo w r² i znika w chwili T = r₀²/4",
        "Przepływ Ricciego okrągłej sfery: r²(t) = r₀² − 4t. Lewy panel: przekrój sfery w 4 chwilach. "
        "Prawy panel: r² w czasie.",
        "Źródło: wzór z modelu 2 (tensor Ricciego okrągłej sfery S³). Dowód hipotezy Poincarégo: Perelman 2002, 2003.",
        ncols=2, width_ratios=[0.85, 1.15],
    )
    for frac, label, color in zip(fractions, labels, colors):
        left.add_patch(plt.Circle((0, 0), np.sqrt(1 - frac), fill=False, edgecolor=color, lw=2))
        right.plot(frac / 4, 1 - frac, "o", color=color, markeredgecolor=SURFACE, markeredgewidth=RING,
                   markersize=8, zorder=3, clip_on=False)
    left.set(xlim=(-1.12, 1.12), ylim=(-1.12, 1.12), aspect="equal")
    left.axis("off")
    left.legend(handles=[Line2D([], [], color=c, lw=2, label=text) for c, text in zip(colors, labels)],
                loc="upper center", bbox_to_anchor=(0.5, 0.02), ncol=4, handlelength=1.4, columnspacing=1.2)
    panel_title(left, "Przekrój sfery o promieniu r(t)")
    right.plot([0, 0.25], [1, 0], color=INK2, zorder=2)
    right.plot(0.25, 0, "o", markerfacecolor=SURFACE, markeredgecolor=INK2, markeredgewidth=LINE, markersize=8,
               zorder=3, clip_on=False)
    right.plot([0.25, 0.25], [0.035, 0.34], color=MUTED, lw=1, zorder=1)
    right.text(0.262, 0.36, "sfera znika: T = r₀²/4", ha="right", fontsize=8.5, color=INK2)
    right.set(xlim=(0, 0.27), ylim=(0, 1.08), xlabel="czas t w jednostkach r₀²", ylabel="r² w jednostkach r₀²")
    comma_ticks(right.xaxis)
    comma_ticks(right.yaxis, 1)
    panel_title(right, "Prosta r² = r₀² − 4t")
    save(fig, "poincare-sphere-shrinks.png")


def hermite_functions(nmax, x):
    """Normalised eigenfunctions n = 0..nmax of p^2 + x^2 on the grid x."""
    phi = np.zeros((nmax + 1, x.size))
    phi[0] = np.pi ** -0.25 * np.exp(-x * x / 2)
    phi[1] = np.sqrt(2.0) * x * phi[0]
    for n in range(1, nmax):
        phi[n + 1] = np.sqrt(2.0 / (n + 1)) * x * phi[n] - np.sqrt(n / (n + 1)) * phi[n - 1]
    return phi


def figure_yang_mills():
    m = 20
    _, levels, bound = mc.check_x2y2()
    e0, e1, e2 = sorted(set(round(e, 5) for e in levels))[:3]
    coefficients = np.linalg.eigh(mc.x2y2_hamiltonian(m, 0, 0))[1][:, 0].reshape(m, m)
    grid = np.linspace(-5, 5, 401)
    even = hermite_functions(2 * m, grid)[: 2 * m : 2]  # n = 0, 2, ..., 2m - 2
    density = (even.T @ coefficients @ even) ** 2
    assert abs(density.sum() * (grid[1] - grid[0]) ** 2 - 1) < 1e-3, "ground state must be normalised"
    colours = 3
    b0 = 11 * colours / (48 * np.pi**2)
    x_star = 1 / (2 * b0)  # ln(l*/l0) for g^2(l0) = 1
    fig, (left, mid, right) = frame(
        "Stan podstawowy zostaje w środku, choć doliny potencjału x²y² są otwarte",
        "Lewy panel: sprzężenie g w rachunku 1 pętli. Środkowy panel: gęstość stanu podstawowego "
        "hamiltonianu −Δ + x²y²\ni kontur potencjału na poziomie E₀. Prawy panel: poziomy energii.",
        f"Źródło: models_check.py, sprawdzian 5, baza {m} × {m}. Gęstość w jednostkach maksimum. "
        "Granica dolna: H ≥ (−Δ + |x| + |y|)/2.\n"
        f"Lewy panel: przykład dla grupy SU({colours}) i sprzężenia g²(ℓ₀) = 1.",
        ncols=3, width_ratios=[1.0, 1.2, 0.72],
    )
    left.plot([0, x_star], [1, 0], color=BLUE, zorder=2)
    left.plot(x_star, 0, "o", color=BLUE, markeredgecolor=SURFACE, markeredgewidth=RING, markersize=8,
              zorder=3, clip_on=False)
    left.text(x_star - 1.5, 0.035, "1/g² = 0\nna długości ℓ*", ha="right", va="bottom", fontsize=8.5, color=INK2,
              linespacing=1.3)
    left.set(xlim=(0, x_star * 1.08), ylim=(0, 1.08), xlabel="ln(ℓ/ℓ₀)", ylabel="1/g²")
    comma_ticks(left.yaxis, 1)
    panel_title(left, "1/g²(ℓ) = 1/g²(ℓ₀) − 2 b₀ ln(ℓ/ℓ₀)")
    image = mid.imshow(density / density.max(), extent=(-5, 5, -5, 5), origin="lower", cmap=SEQ, vmin=0, vmax=1)
    gx, gy = np.meshgrid(grid, grid)
    mid.contour(gx, gy, gx**2 * gy**2, levels=[e0], colors=[INK2], linewidths=1.1)
    mid.grid(False)
    mid.set(xlabel="x", ylabel="y", aspect="equal")
    bar = fig.colorbar(image, ax=mid, fraction=0.046, pad=0.035, ticks=[0, 0.5, 1])
    bar.ax.set_yticklabels(["0", "0,5", "1"])
    bar.outline.set_visible(False)
    panel_title(mid, "Gęstość |ψ₀|² i kontur x²y² = E₀")
    for value, text in ((e0, f"E₀ = {pl(e0, 3)}"), (e1, f"E₁ = {pl(e1, 3)} (2 stany)"), (e2, f"E₂ = {pl(e2, 3)}")):
        right.plot([0.05, 0.62], [value, value], color=INK, lw=LINE)
        right.text(0.05, value + 0.07, text, fontsize=8.5, color=INK2, va="bottom")
    right.plot([0.05, 0.62], [bound, bound], color=MUTED, lw=1)
    right.text(0.05, bound - 0.07, f"granica dolna {pl(bound, 3)}", fontsize=8.5, color=INK2, va="top")
    right.plot([0.8, 0.8], [e0, e1], color=INK2, lw=1.1)
    for value in (e0, e1):
        right.plot([0.76, 0.84], [value, value], color=INK2, lw=1.1)
    right.text(0.86, (e0 + e1) / 2, pl(e1 - e0, 3), fontsize=8.5, color=INK2, va="center")
    right.set(xlim=(0, 1.12), ylim=(0, 3.7), ylabel="energia")
    right.set_xticks([])
    right.set_yticks([0, 1, 2, 3])
    right.grid(False)
    panel_title(right, "Odstęp E₁ − E₀ > 0")
    save(fig, "yang-mills-coupling-and-gap.png")


def figure_navier_stokes():
    lam = 2.0
    steps = np.arange(0, 13)
    thetas = ((0.35, BLUE, "mniej niż 1/λ"), (0.5, MUTED, "równe 1/λ"), (0.7, RED, "więcej niż 1/λ"))
    fig, axes = frame(
        "W 3 wymiarach liczba Reynoldsa rośnie tylko dla θ > 1/λ; w 2 wymiarach maleje",
        r"Wzór modelu 2: $\mathrm{Re}_n/\mathrm{Re}_0$ = (θ × λ^(d − 2))^(n/2), tutaj λ = 2. "
        "θ oznacza ułamek energii wiru n,\nktóry przechodzi do wiru n + 1. Skala pionowa jest logarytmiczna.",
        "Źródło: wzór z modelu 2; rachunek bez dowodu. Próg dla 3 wymiarów: θ = 1/λ = 0,5.",
        ncols=2, sharey=True,
    )
    for ax, dim in zip(axes, (3, 2)):
        for theta, color, text in thetas:
            ratio = (theta * lam ** (dim - 2)) ** (steps / 2)
            ax.plot(steps, ratio, color=color, label=f"θ = {pl(theta)}: {text}")
            ax.text(steps[-1] + 0.25, ratio[-1], f"θ = {pl(theta)}", va="center", fontsize=8.5, color=INK2)
        ax.set_yscale("log")
        ax.set(xlim=(0, 14.8), xlabel="numer wiru n (rozmiar wiru: λ^(−n))")
        ax.set_xticks(range(0, 13, 2))
        panel_title(ax, f"{dim} wymiary: mnożnik na 1 krok = " + ("√(θ × λ)" if dim == 3 else "√θ"))
    axes[0].set_ylabel(r"$\mathrm{Re}_n/\mathrm{Re}_0$")
    axes[0].set_yticks([0.001, 0.01, 0.1, 1, 10, 100], ["0,001", "0,01", "0,1", "1", "10", "100"])
    axes[0].legend(loc="upper left")
    save(fig, "navier-stokes-reynolds-cascade.png")


def figure_p_vs_np():
    rows = mc.check_queries()
    sizes = np.arange(10, 31)
    counting = np.array([mc.shannon_min_gates(int(n)) for n in sizes], dtype=float)
    explicit = 3.1 * sizes
    n0 = 20
    c0, x0 = mc.shannon_min_gates(n0), 3.1 * n0
    fig, (left, right) = frame(
        f"Dla n = {n0} zliczanie wymusza {thousands(c0)} bramek, a ograniczenie\n"
        f"dla funkcji podanej wzorem daje {pl(x0, 0)}",
        "Lewy panel: funkcja OR w modelu zapytań. Prawy panel: dolne ograniczenia liczby bramek obwodu, "
        "skala logarytmiczna.",
        "Źródło: models_check.py, sprawdziany 6 i 7. Zliczanie: (16 × (n + s)²)^s ≥ 2^(2^n). "
        "Funkcja podana wzorem: 3,1 × n (Li, Yang 2022).",
        ncols=2,
    )
    ns = [n for n, _, _ in rows]
    for values, color, label in (([d for _, d, _ in rows], BLUE, "zapytania algorytmu deterministycznego"),
                                 ([c for _, _, c in rows], ORANGE, "bity certyfikatu odpowiedzi „1”")):
        left.plot(ns, values, "-o", color=color, markeredgecolor=SURFACE, markeredgewidth=RING, markersize=8,
                  label=label, zorder=3)
    left.text(ns[-1] + 0.25, rows[-1][1], "n", va="center", fontsize=8.5, color=INK2)
    left.text(ns[-1] + 0.25, rows[-1][2], "1", va="center", fontsize=8.5, color=INK2)
    left.set(xlim=(0.5, 9), ylim=(0, 9.6), xlabel="liczba bitów wejścia n", ylabel="liczba bitów")
    left.legend(loc="upper left")
    panel_title(left, "Funkcja OR: n zapytań, certyfikat 1 bit")
    right.plot(sizes, counting, color=BLUE, label="zliczanie: co najmniej 1 funkcja wymaga tylu bramek")
    right.plot(sizes, explicit, color=ORANGE, label="funkcja podana wzorem: 3,1 × n")
    right.plot([n0, n0], [x0, c0], color=MUTED, lw=1, zorder=2)
    for value, color, offset in ((c0, BLUE, 0.42), (x0, ORANGE, 0.5)):
        right.plot(n0, value, "o", color=color, markeredgecolor=SURFACE, markeredgewidth=RING, markersize=8, zorder=3)
        right.text(n0 + 0.7, value * offset, thousands(round(value)), fontsize=8.5, color=INK2, va="center")
    right.set_yscale("log")
    right.set(xlim=(10, 31), ylim=(10, 1e9), xlabel="liczba zmiennych n", ylabel="liczba bramek")
    right.set_xticks(range(10, 31, 5))
    right.set_yticks([10, 1e3, 1e5, 1e7, 1e9], ["10", "1 000", "100 000", "10 mln", "1 mld"])
    right.legend(loc="upper left")
    panel_title(right, "Dolne ograniczenia liczby bramek")
    save(fig, "p-vs-np-queries-and-gates.png")


def figure_counterexample_thread():
    ratios = mc.lagarias_ratios()
    nmax, worst_n, worst_ratio = mc.check_lagarias(ratios)
    edges = np.unique(np.round(np.logspace(np.log10(2), np.log10(nmax + 1), 61)).astype(int))
    centre, top, median = [], [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        part = ratios[lo - 1 : hi - 1]  # n from lo to hi - 1
        centre.append(np.sqrt(lo * (hi - 1)))
        top.append(part.max())
        median.append(np.median(part))
    fig, (ax,) = frame(
        "Wątek kontrprzykładów dla hipotezy Riemanna nie zatrzymał się:\n"
        f"iloraz nie przekracza {pl(worst_ratio, 4)} dla n od 2 do {thousands(nmax)}",
        r"Iloraz σ(n) / ($H_n$ + exp($H_n$) × ln $H_n$) w " + f"{len(top)} przedziałach liczby n. "
        "Hipoteza Riemanna jest równoważna zdaniu:\nżaden iloraz nie przekracza 1.",
        "Źródło: models_check.py, sprawdzian 8. Kryterium: Lagarias 2002. σ(n) oznacza sumę dzielników liczby n, "
        r"$H_n$ oznacza sumę 1 + 1/2 + … + 1/n.",
    )
    ax.axhline(1, color=INK2, lw=1.3, zorder=2)
    ax.text(2.2, 1.012, "granica: iloraz większy niż 1 obala hipotezę", fontsize=8.5, color=INK2, va="bottom")
    ax.plot(centre, median, color=MUTED, label="mediana ilorazu w przedziale", zorder=2)
    ax.plot(centre, top, color=BLUE, label="największy iloraz w przedziale", zorder=3)
    ax.plot(worst_n, worst_ratio, "o", color=BLUE, markeredgecolor=SURFACE, markeredgewidth=RING, markersize=8, zorder=4,
            label=f"największy iloraz: {pl(worst_ratio, 4)} dla n = {worst_n}")
    ax.set_xscale("log")
    ax.set(xlim=(2, nmax * 1.6), ylim=(0, 1.1), xlabel="liczba n (skala logarytmiczna)", ylabel="iloraz")
    ax.set_xticks([10, 100, 1000, 10_000, 100_000, 1_000_000],
                  ["10", "100", "1 000", "10 000", "100 000", "1 000 000"])
    comma_ticks(ax.yaxis, 1)
    ax.legend(loc="lower left")
    save(fig, "riemann-counterexample-thread.png")


def box(ax, x, y, text, color, width, height=9.0):
    ax.add_patch(plt.Rectangle((x - width / 2, y - height / 2), width, height, facecolor=SURFACE,
                               edgecolor=color, lw=LINE, zorder=2))
    ax.text(x, y, text, ha="center", va="center", fontsize=9, linespacing=1.3, zorder=3)


def arrow(ax, points, label=None, at=None):
    """Polyline with an arrow head at its end; only horizontal and vertical segments are allowed."""
    assert all(a[0] == b[0] or a[1] == b[1] for a, b in zip(points, points[1:])), points
    ax.plot(*zip(*points[:-1]), color=INK2, lw=1.1, solid_capstyle="butt", zorder=1)
    ax.annotate("", xy=points[-1], xytext=points[-2], zorder=1,
                arrowprops={"arrowstyle": "-|>", "color": INK2, "lw": 1.1, "shrinkA": 0, "shrinkB": 0})
    if label:
        ax.text(*at, label, fontsize=8.5, color=INK2, ha="center", va="center", zorder=3,
                bbox={"facecolor": SURFACE, "edgecolor": "none", "pad": 1.5})


def figure_algorithm():
    fig, (ax,) = frame(
        "Algorytm 2 wątków kończy pracę, gdy istnieje dowód, obalenie albo kontrprzykład",
        "Schemat pętli dla tezy T i teorii z programem, który sprawdza dowody. Ramka niebieska oznacza krok, "
        "ramka szara pytanie,\nramka pomarańczowa wynik. Algorytm pracuje bez końca, gdy teoria nie rozstrzyga tezy T "
        "i teza T nie ma kontrprzykładu.",
        "Źródło: sekcja „Algorytm” w pliku REPORT.md. Wątek kontrprzykładów istnieje dla zdań klasy Π₁, "
        "np. dla hipotezy Riemanna (sprawdzian 8).",
        height=7.4,
    )
    ax.set(xlim=(0, 100), ylim=(8, 100))
    ax.axis("off")
    main, result, loop = 42, 86, 8
    box(ax, main, 94, "Start: teza T, k = 1", MUTED, 44, 7)
    box(ax, main, 80, "Wątek dowodów:\nsprawdź każdy tekst o długości k", BLUE, 44)
    box(ax, main, 64, "Tekst jest dowodem tezy T?", INK2, 44, 7)
    box(ax, main, 48, "Tekst jest dowodem zaprzeczenia tezy T?", INK2, 44, 7)
    box(ax, main, 32, "Wątek kontrprzykładów:\nsprawdź kandydata numer k", BLUE, 44)
    box(ax, main, 16, "Kandydat narusza tezę T?", INK2, 44, 7)
    box(ax, result, 64, "Wynik:\nteza T ma dowód", ORANGE, 26)
    box(ax, result, 32, "Wynik:\nteza T jest fałszywa", ORANGE, 26)
    box(ax, loop, 48, "k := k + 1", BLUE, 14, 7)
    arrow(ax, [(main, 90.5), (main, 84.5)])
    arrow(ax, [(main, 75.5), (main, 67.5)])
    arrow(ax, [(main, 60.5), (main, 51.5)], "nie", (main, 56))
    arrow(ax, [(main, 44.5), (main, 36.5)], "nie", (main, 40.5))
    arrow(ax, [(main, 27.5), (main, 19.5)])
    arrow(ax, [(main + 22, 64), (result - 13, 64)], "tak", (68.5, 64))
    arrow(ax, [(main + 22, 48), (result, 48), (result, 36.5)], "tak", (68.5, 48))
    arrow(ax, [(main + 22, 16), (result, 16), (result, 27.5)], "tak", (68.5, 16))
    arrow(ax, [(main - 22, 16), (loop, 16), (loop, 44.5)], "nie", (14, 16))
    arrow(ax, [(loop, 51.5), (loop, 80), (main - 22, 80)])
    save(fig, "algorithm-two-threads.png")


def quiet_3d(ax, elev, azim):
    """Panes in the surface colour, a fixed view and manual draw order for a 3D axes."""
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.set_pane_color(SURFACE)
    ax.computed_zorder = False
    ax.view_init(elev=elev, azim=azim)


def figure_zeta_surface():
    zeros, off_line = mc.check_zeta()
    sigma, t = np.linspace(0, 1, 41), np.linspace(10, 40, 301)
    s_grid, t_grid = np.meshgrid(sigma, t)
    fig, (ax,) = frame(
        f"{len(zeros)} zer funkcji dzeta dla t od 10 do 40 leży na prostej " + r"$\sigma = 1/2$",
        r"Powierzchnia $|\zeta(\sigma + it)|$ nad pasem $0 \leq \sigma \leq 1$. Punkty pomarańczowe: zera. "
        r"Linia czarna: prosta $\sigma = 1/2$.",
        r"Źródło: models_check.py, sprawdzian 13. Najmniejsza wartość $|\zeta|$ na prostych $\sigma = 0{,}25$ "
        rf"i $\sigma = 0{{,}}75$ wynosi {pl(off_line, 3)}.",
        projection="3d", height=6.6,
    )
    quiet_3d(ax, 34, -56)
    ax.plot_surface(s_grid, t_grid, np.abs(mc.zeta(s_grid + 1j * t_grid)), cmap=SEQ, linewidth=0, rcount=150,
                    ccount=41, zorder=1)
    ax.plot(np.full(t.size, 0.5), t, np.abs(mc.zeta(0.5 + 1j * t)), color=INK, lw=1.2, zorder=2)
    ax.scatter(np.full(len(zeros), 0.5), zeros, np.zeros(len(zeros)), s=42, color=ORANGE, edgecolors=SURFACE,
               linewidths=RING, depthshade=False, zorder=3)
    ax.set(xlabel=r"$\sigma$", ylabel="t", zlabel=r"$|\zeta|$")
    comma_ticks(ax.xaxis, 1)
    save(fig, "riemann-zeta-surface.png")


def figure_torus(multiplier=3):
    big, small = 2.0, 0.8

    def embed(u, v):
        return (big + small * np.cos(v)) * np.cos(u), (big + small * np.cos(v)) * np.sin(u), small * np.sin(v)

    fig, (ax,) = frame(
        f"Przekątna D przecina wykres G odwzorowania x → {multiplier}x w {multiplier - 1} punktach:\n"
        "punkty stałe odwzorowania są przecięciami krzywych",
        "Torus z 4 krzywymi modelu 1 w przekroju rzeczywistym: krzywa E jest tutaj okręgiem, a powierzchnia E × E "
        "torusem.\nPunkty czarne: przecięcia krzywych D i G, czyli punkty stałe odwzorowania.",
        f"Źródło: wzór modelu 1. W przekroju rzeczywistym (D, G) = {multiplier - 1}. Na krzywej eliptycznej "
        f"(D, G) = {(multiplier - 1) ** 2}, bo odwzorowanie x → x − {multiplier}x ma stopień {(multiplier - 1) ** 2}.",
        projection="3d", height=6.6,
    )
    quiet_3d(ax, 38, -62)
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 80), np.linspace(0, 2 * np.pi, 40))
    ax.plot_surface(*embed(u, v), color="#cde2fb", alpha=0.3, linewidth=0, shade=False, zorder=1)
    s = np.linspace(0, 2 * np.pi, 800)
    curves = (("H = E × {punkt}", s, 0 * s, MUTED, 1.4), ("V = {punkt} × E", 0 * s, s, INK2, 1.4),
              ("D = przekątna", s, s, BLUE, 2.2), (f"G = wykres x → {multiplier}x", s, multiplier * s, ORANGE, 2.2))
    for label, cu, cv, color, width in curves:
        ax.plot(*embed(cu, cv), color=color, lw=width, label=label, zorder=2)
    fixed = 2 * np.pi * np.arange(multiplier - 1) / (multiplier - 1)
    ax.scatter(*embed(fixed, fixed), s=60, color=INK, edgecolors=SURFACE, linewidths=RING, depthshade=False,
               zorder=3, label="punkt stały")
    ax.set_box_aspect((1, 1, 0.42))
    ax.set_axis_off()
    ax.legend(loc="upper left", bbox_to_anchor=(0.0, 0.98))
    save(fig, "model-1-torus-curves.png")


def figure_potential_3d():
    _, levels, _ = mc.check_x2y2()
    x = np.linspace(-4, 4, 241)
    gx, gy = np.meshgrid(x, x)
    potential = gx**2 * gy**2
    fig, (ax,) = frame(
        rf"Doliny potencjału $x^2y^2$ mają dno na wysokości 0, a poziom podstawowy ma wysokość {pl(levels[0], 3)}",
        "Powierzchnia potencjału, obcięta na wysokości 2: 4 ramiona dolin (jasne) biegną wzdłuż 2 osi "
        "i nie zamykają się.\nLinia czarna: poziom podstawowy $E_0$.",
        "Źródło: models_check.py, sprawdzian 5. Orbity klasyczne w dolinach pokazuje animacja ze sprawdzianu 11.",
        projection="3d", height=6.6,
    )
    quiet_3d(ax, 62, -58)
    ax.plot_surface(gx, gy, np.minimum(potential, 2), cmap=SEQ, vmin=0, vmax=2.6, linewidth=0, rcount=120,
                    ccount=120, zorder=1)
    ax.contour(gx, gy, potential, levels=[levels[0]], colors=[INK], linewidths=1.3, zorder=2)
    ax.set(xlabel="x", ylabel="y", zlabel=r"$x^2y^2$", zlim=(0, 2))
    ax.set_zticks([0, 1, 2])
    save(fig, "yang-mills-potential-3d.png")


def figure_cube():
    _, queries, certificate = mc.check_queries(3)[-1]
    corners = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    fig, (ax,) = frame(
        f"Odpowiedź 1 funkcji OR ma certyfikat o {certificate} bicie, a odpowiedź 0 wymaga {queries} zapytań",
        "Sześcian 8 wejść o 3 bitach. Punkt pełny: wartość 1. Punkt pusty: wartość 0. "
        "Ściana niebieska: 4 wejścia z pierwszym bitem 1.\n"
        "Krawędzie pomarańczowe: 3 zmiany dokładnie 1 bitu, które zmieniają wartość funkcji z 0 na 1.",
        "Źródło: models_check.py, sprawdzian 6 dla n = 3. Napis przy wierzchołku podaje 3 bity wejścia.",
        projection="3d", height=6.6,
    )
    quiet_3d(ax, 22, -58)
    ax.add_collection3d(Poly3DCollection([[(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)]], facecolor=BLUE, alpha=0.14,
                                         edgecolor="none", zorder=1))
    for i, a in enumerate(corners):
        for b in corners[i + 1 :]:
            if sum(p != q for p, q in zip(a, b)) == 1:
                at_zero = (0, 0, 0) in (a, b)
                ax.plot(*zip(a, b), color=ORANGE if at_zero else MUTED, lw=2.4 if at_zero else 1.0, zorder=2)
    ones = [c for c in corners if any(c)]
    ax.scatter(*zip(*ones), s=90, color=BLUE, edgecolors=SURFACE, linewidths=RING, depthshade=False, zorder=3)
    ax.scatter([0], [0], [0], s=90, color=SURFACE, edgecolors=ORANGE, linewidths=2.2, depthshade=False, zorder=3)
    for c in corners:
        shift = 0.06 if any(c) else -0.14  # the label of 000 moves away from the orange edges
        ax.text(c[0] + shift, c[1] + shift, c[2] + shift, "".join(map(str, c)), fontsize=9, color=INK2, zorder=4)
    ax.set_box_aspect((1, 1, 1))
    ax.set_axis_off()
    save(fig, "p-vs-np-cube.png")


def figure_sato_tate(data):
    import seaborn as sns

    distance, values = mc.sato_tate_distance(data)
    grid = np.linspace(-1, 1, 400)
    fig, (ax,) = frame(
        rf"Wartości $a/(2\sqrt{{p}})$ krzywej 37a1 wypełniają przedział od −1 do 1 według rozkładu półokręgu",
        f"Histogram {thousands(values.size)} wartości dla liczb pierwszych p od 3 do 99 991. "
        r"Linia: gęstość $\frac{2}{\pi}\sqrt{1 - x^2}$." "\n"
        "Nierówność Hassego oznacza, że żadna wartość nie leży poza przedziałem.",
        "Źródło: models_check.py, sprawdzian 14. Największa różnica dystrybuanty z danych i dystrybuanty "
        f"rozkładu półokręgu wynosi {pl(distance, 4)}.",
    )
    sns.histplot(x=values, bins=40, stat="density", color=BLUE, edgecolor=SURFACE, linewidth=1.2, alpha=1, ax=ax)
    ax.plot(grid, 2 / np.pi * np.sqrt(1 - grid**2), color=INK2, lw=LINE, label="rozkład półokręgu")
    ax.set(xlim=(-1.08, 1.08), xlabel=r"$a/(2\sqrt{p})$", ylabel="gęstość")
    ax.set_xticks([-1, -0.5, 0, 0.5, 1])
    comma_ticks(ax.xaxis, 1)
    comma_ticks(ax.yaxis, 1)
    ax.legend(loc="upper right")
    save(fig, "bsd-sato-tate.png")


if __name__ == "__main__":
    style()
    figure_algorithm()
    figure_counterexample_thread()
    figure_riemann()
    figure_hodge()
    figure_poincare()
    figure_yang_mills()
    figure_navier_stokes()
    figure_p_vs_np()
    figure_zeta_surface()
    figure_torus()
    figure_potential_3d()
    figure_cube()
    data = mc.bsd_series()
    figure_bsd(data)
    figure_sato_tate(data)
