#!/usr/bin/env python3
"""Interactive versions of the figures (plotly) on one page: docs/index.html.

Hover shows the numbers behind every mark; the 3D figures rotate and zoom; two figures have a time slider.
Every number comes from models_check.py or simulations.py.
Run: python3 interactive.py   (needs numpy and plotly; takes about 1 minute)
"""
from html import escape
from pathlib import Path

import numpy as np
import plotly.graph_objects as go
from plotly.offline import get_plotlyjs_version
from plotly.subplots import make_subplots

import models_check as mc
import simulations as sim
from models_check import pl, thousands

OUT = Path(__file__).parent / "docs" / "index.html"
SURFACE, INK, INK2, MUTED, GRID, AXIS = "#fcfcfb", "#0b0b0b", "#52514e", "#898781", "#e1e0d9", "#c3c2b7"
BLUE, ORANGE, RED = "#2a78d6", "#eb6834", "#e34948"
RAMP = ["#86b6ef", "#3987e5", "#1c5cab", "#0d366b"]
SEQ = [[0, SURFACE], [0.15, "#cde2fb"], [0.4, "#6da7ec"], [0.7, "#256abf"], [1, "#0d366b"]]
FONT = "system-ui, -apple-system, 'Segoe UI', sans-serif"
AXIS_STYLE = {"gridcolor": GRID, "linecolor": AXIS, "zeroline": False, "ticks": "outside", "tickcolor": AXIS}


def tidy(fig, height=460, legend_y=1.1, **layout):
    """Shared chrome: surface colour, one font, decimal comma, legend above the plot (below it for subplots)."""
    fig.update_layout(paper_bgcolor=SURFACE, plot_bgcolor=SURFACE, height=height, separators=", ",
                      font={"family": FONT, "size": 13, "color": INK2}, margin={"l": 64, "r": 24, "t": 60, "b": 56},
                      legend={"orientation": "h", "y": legend_y, "x": 0}, hoverlabel={"bgcolor": "#ffffff"}, **layout)
    fig.update_xaxes(**AXIS_STYLE)
    fig.update_yaxes(**AXIS_STYLE)
    return fig


def scene(**axes):
    style = {"backgroundcolor": SURFACE, "gridcolor": GRID, "linecolor": AXIS}
    return {key: {**style, **value} for key, value in axes.items()}


def riemann_hasse():
    pairs = mc.hasse_pairs()
    p = np.array([key[0] for key in pairs])
    n = np.array([key[1] for key in pairs])
    grid = np.linspace(4, 100, 200)
    fig = go.Figure()
    for sign in (1, -1):
        fig.add_scatter(x=grid, y=sign * 2 * np.sqrt(grid), mode="lines", line={"color": INK2, "width": 1.5},
                        hoverinfo="skip", name="granica a = ±2√p", showlegend=sign == 1)
    fig.add_scatter(x=p, y=p + 1 - n, mode="markers", name="para (p, a)",
                    marker={"color": BLUE, "size": 7, "line": {"color": SURFACE, "width": 1}},
                    customdata=np.stack([n, list(pairs.values())], axis=1),
                    hovertemplate="p = %{x}<br>a = %{y}<br>N = %{customdata[0]}<br>liczba krzywych: %{customdata[1]}"
                                  "<extra></extra>")
    tidy(fig, xaxis_title="liczba pierwsza p", yaxis_title="a = p + 1 − N")
    return (f"Każda z {thousands(sum(pairs.values()))} krzywych leży wewnątrz granicy \\(a^2 = 4p\\)",
            "Punkt oznacza parę \\((p, a)\\), dla której istnieje co najmniej 1 krzywa eliptyczna nad ciałem "
            "\\(F_p\\). Wskaż punkt, żeby odczytać liczbę punktów \\(N\\) i liczbę krzywych.", fig)


def riemann_zeta():
    zeros, off_line = mc.check_zeta()
    sigma, t = np.linspace(0, 1, 41), np.linspace(10, 40, 241)
    s_grid, t_grid = np.meshgrid(sigma, t)
    fig = go.Figure()
    fig.add_surface(x=sigma, y=t, z=np.abs(mc.zeta(s_grid + 1j * t_grid)), colorscale=SEQ, showscale=False,
                    hovertemplate="σ = %{x:.2f}<br>t = %{y:.2f}<br>|ζ| = %{z:.3f}<extra></extra>")
    fig.add_scatter3d(x=[0.5] * len(zeros), y=zeros, z=[0] * len(zeros), mode="markers", name="zero",
                      marker={"color": ORANGE, "size": 6, "line": {"color": SURFACE, "width": 1}},
                      hovertemplate="zero: σ = 0,5, t = %{y:.3f}<extra></extra>")
    tidy(fig, height=560, scene=scene(xaxis={"title": "σ"}, yaxis={"title": "t"}, zaxis={"title": "|ζ|"}),
         scene_camera={"eye": {"x": 1.6, "y": -1.5, "z": 0.9}})
    return (f"{len(zeros)} zer funkcji dzeta dla \\(t\\) od 10 do 40 leży na prostej \\(\\sigma = 1/2\\)",
            "Powierzchnia \\(|\\zeta(\\sigma + it)|\\) nad pasem \\(0 \\le \\sigma \\le 1\\). Obróć rysunek myszą. "
            f"Najmniejsza wartość na prostych \\(\\sigma = 0{{,}}25\\) i \\(\\sigma = 0{{,}}75\\) wynosi {pl(off_line, 3)}.",
            fig)


def riemann_counterexample_thread():
    ratios = mc.lagarias_ratios()
    nmax, worst_n, worst_ratio = mc.check_lagarias(ratios)
    edges = np.unique(np.round(np.logspace(np.log10(2), np.log10(nmax + 1), 61)).astype(int))
    rows = [(np.sqrt(lo * (hi - 1)), ratios[lo - 1 : hi - 1].max(), float(np.median(ratios[lo - 1 : hi - 1])),
             lo + int(np.argmax(ratios[lo - 1 : hi - 1])), lo, hi - 1) for lo, hi in zip(edges[:-1], edges[1:])]
    centre, top, median, best, lo, hi = map(np.array, zip(*rows))
    fig = go.Figure()
    fig.add_hline(y=1, line={"color": INK2, "width": 1.5})
    fig.add_scatter(x=centre, y=median, mode="lines", line={"color": MUTED, "width": 2}, name="mediana ilorazu",
                    hovertemplate="%{y:.4f}<extra>mediana</extra>")
    fig.add_scatter(x=centre, y=top, mode="lines", line={"color": BLUE, "width": 2}, name="największy iloraz",
                    customdata=np.stack([best, lo, hi], axis=1),
                    hovertemplate="%{y:.4f} dla n = %{customdata[0]}<br>przedział od %{customdata[1]} do "
                                  "%{customdata[2]}<extra>największy</extra>")
    tidy(fig, hovermode="x unified", xaxis_title="liczba n (skala logarytmiczna)", yaxis_title="iloraz",
         xaxis_type="log", yaxis_range=[0, 1.1])
    return (f"Wątek kontrprzykładów nie zatrzymał się: iloraz nie przekracza {pl(worst_ratio, 4)} "
            f"dla \\(n\\) od 2 do {thousands(nmax)}",
            "Iloraz \\(\\sigma(n) / (H_n + e^{H_n} \\ln H_n)\\). Hipoteza Riemanna jest równoważna zdaniu: żaden "
            f"iloraz nie przekracza 1. Największy iloraz daje liczba \\(n = {worst_n}\\).", fig)


def bsd_slopes(data):
    primes, series = data
    summary = mc.bsd_products(data=data)
    keep = np.flatnonzero(primes >= 10)[::8]
    fig = go.Figure()
    for color, (name, (rank, _, slope)) in zip(RAMP, summary.items()):
        fig.add_scatter(x=np.log(np.log(primes[keep])), y=series[name][keep], mode="lines", customdata=primes[keep],
                        line={"color": color, "width": 2}, name=f"{name}, ranga {rank}, nachylenie {pl(slope)}",
                        hovertemplate="%{y:.3f}<extra>" + name + "</extra>")
    marks = [10, 100, 1000, 10_000, 100_000]
    tidy(fig, hovermode="x unified", xaxis_title="X (skala ln ln X)", yaxis_title="suma ln(N_p / p) dla p ≤ X")
    fig.update_xaxes(tickvals=np.log(np.log(marks)), ticktext=["10", "100", "1 000", "10 000", "100 000"])
    return ("Nachylenie iloczynu rośnie z rangą krzywej: " + "; ".join(pl(v[2]) for v in summary.values()),
            "Hipoteza BSD przewiduje nachylenie równe randze. Wskaż rysunek, żeby odczytać 4 sumy dla 1 wartości "
            "\\(X\\).", fig)


def bsd_sato_tate(data):
    distance, values = mc.sato_tate_distance(data)
    grid = np.linspace(-1, 1, 201)
    fig = go.Figure()
    fig.add_histogram(x=values, xbins={"start": -1, "end": 1, "size": 0.05}, histnorm="probability density",
                      marker={"color": BLUE, "line": {"color": SURFACE, "width": 2}}, name="histogram wartości",
                      hovertemplate="przedział %{x}<br>gęstość %{y:.3f}<extra></extra>")
    fig.add_scatter(x=grid, y=2 / np.pi * np.sqrt(1 - grid**2), mode="lines", line={"color": INK2, "width": 2},
                    name="rozkład półokręgu", hovertemplate="%{y:.3f}<extra>półokrąg</extra>")
    tidy(fig, xaxis_title="a / (2√p)", yaxis_title="gęstość")
    return (f"Wartości \\(a/(2\\sqrt{{p}})\\) krzywej 37a1 układają się według rozkładu półokręgu",
            f"Histogram {thousands(values.size)} wartości. Największa różnica dystrybuant wynosi {pl(distance, 4)}.",
            fig)


def model_1_torus(multiplier=3):
    big, small = 2.0, 0.8

    def embed(u, v):
        return (big + small * np.cos(v)) * np.cos(u), (big + small * np.cos(v)) * np.sin(u), small * np.sin(v)

    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 80), np.linspace(0, 2 * np.pi, 40))
    x, y, z = embed(u, v)
    fig = go.Figure()
    fig.add_surface(x=x, y=y, z=z, opacity=0.3, showscale=False, hoverinfo="skip",
                    colorscale=[[0, "#cde2fb"], [1, "#cde2fb"]])
    s = np.linspace(0, 2 * np.pi, 600)
    for name, cu, cv, color, width in (("H = E × {punkt}", s, 0 * s, MUTED, 4), ("V = {punkt} × E", 0 * s, s, INK2, 4),
                                       ("D = przekątna", s, s, BLUE, 7),
                                       (f"G = wykres x → {multiplier}x", s, multiplier * s, ORANGE, 7)):
        cx, cy, cz = embed(cu, cv)
        fig.add_scatter3d(x=cx, y=cy, z=cz, mode="lines", line={"color": color, "width": width}, name=name,
                          hoverinfo="name")
    fixed = 2 * np.pi * np.arange(multiplier - 1) / (multiplier - 1)
    fx, fy, fz = embed(fixed, fixed)
    fig.add_scatter3d(x=fx, y=fy, z=fz, mode="markers", marker={"color": INK, "size": 6}, name="punkt stały",
                      hovertemplate="punkt stały odwzorowania<extra></extra>")
    hidden = {"visible": False}
    tidy(fig, height=560, scene={"xaxis": hidden, "yaxis": hidden, "zaxis": hidden, "aspectmode": "data"})
    return (f"Przekątna D przecina wykres G odwzorowania x → {multiplier}x w {multiplier - 1} punktach",
            "Model 1 w przekroju rzeczywistym: krzywa \\(E\\) jest okręgiem, a powierzchnia \\(E \\times E\\) torusem. "
            f"Na krzywej eliptycznej liczba przecięć wynosi {(multiplier - 1) ** 2}.", fig)


def hodge_lattices():
    dims = list(mc.check_hodge_on_torus().values())
    fig = make_subplots(1, 2, subplot_titles=(f"τ = i: {dims[0][0]} klasy, {dims[0][1]} krzywe",
                                              f"τ = i × ∛2: {dims[1][0]} klasy, {dims[1][1]} krzywe"))
    for col, t in ((1, 1.0), (2, 2 ** (1 / 3))):
        m, n = np.meshgrid(np.arange(-3, 4), np.arange(-3, 4))
        x, y = m.ravel().astype(float), n.ravel() * t
        inside = np.abs(y) < 3.3
        label = [f"{a} + {b}τ" for a, b in zip(m.ravel()[inside], n.ravel()[inside])]
        fig.add_scatter(x=-y[inside], y=x[inside], mode="markers", row=1, col=col, name="punkt po mnożeniu przez i",
                        marker={"color": "rgba(0,0,0,0)", "size": 15, "line": {"color": ORANGE, "width": 2}},
                        customdata=label, hovertemplate="i × (%{customdata})<extra></extra>", showlegend=col == 1)
        fig.add_scatter(x=x[inside], y=y[inside], mode="markers", row=1, col=col, name="punkt kraty",
                        marker={"color": BLUE, "size": 8, "line": {"color": SURFACE, "width": 1}},
                        customdata=label, hovertemplate="%{customdata}<extra></extra>", showlegend=col == 1)
    tidy(fig, height=520, legend_y=-0.18)
    fig.update_xaxes(range=[-3.6, 3.6], title_text="Re z")
    fig.update_yaxes(range=[-3.6, 3.6], title_text="Im z", scaleanchor="x")
    return ("Krata kwadratowa wraca na siebie po obrocie o 90°, więc torus ma 4. krzywą",
            "Mnożenie przez \\(i\\) obraca kratę \\(Z + \\tau Z\\) o 90°. Liczba wymiernych klas typu (1,1) na "
            "\\(E \\times E\\) równa się liczbie klas krzywych.", fig)


def poincare_sphere():
    fractions = [0, 0.25, 0.5, 0.75]
    u, v = np.meshgrid(np.linspace(0, 2 * np.pi, 48), np.linspace(0, np.pi, 24))
    unit = np.cos(u) * np.sin(v), np.sin(u) * np.sin(v), np.cos(v)

    def ball(fraction):
        r = np.sqrt(1 - fraction)
        return go.Surface(x=r * unit[0], y=r * unit[1], z=r * unit[2], showscale=False, opacity=0.9,
                          colorscale=[[0, RAMP[1]], [1, RAMP[1]]],
                          hovertemplate=f"t = {pl(fraction / 4, 4)}<br>r² = {pl(1 - fraction)}<extra></extra>")

    fig = go.Figure(data=[ball(0)], frames=[go.Frame(data=[ball(f)], name=str(f)) for f in fractions])
    steps = [{"label": f"t = {pl(f, 2)} T", "method": "animate",
              "args": [[str(f)], {"mode": "immediate", "frame": {"duration": 0, "redraw": True}}]} for f in fractions]
    span = {"range": [-1.05, 1.05], "visible": False}
    tidy(fig, height=520, sliders=[{"steps": steps, "x": 0.1, "len": 0.8, "currentvalue": {"prefix": "chwila: "}}],
         scene={"xaxis": span, "yaxis": span, "zaxis": span, "aspectmode": "cube"})
    return ("Okrągła sfera kurczy się liniowo w \\(r^2\\) i znika w chwili \\(T = r_0^2/4\\)",
            "Przekrój sfery \\(S^3\\) pod przepływem Ricciego: \\(r^2(t) = r_0^2 - 4t\\). Przesuń suwak czasu.", fig)


def poincare_curve():
    times, areas, ratios, curves = sim.curve_shortening()
    error = float(np.abs(areas - (areas[0] - 2 * np.pi * times)).max() / areas[0])

    def shape(i):
        closed = np.append(curves[i], curves[i][0])
        return go.Scatter(x=closed.real, y=closed.imag, mode="lines", line={"color": BLUE, "width": 3},
                          name="krzywa w chwili t", hovertemplate=f"t = {pl(times[i], 3)}<br>pole = {pl(areas[i], 3)}"
                          f"<br>iloraz izoperymetryczny = {pl(ratios[i], 4)}<extra></extra>")

    first = np.append(curves[0], curves[0][0])
    start = go.Scatter(x=first.real, y=first.imag, mode="lines", line={"color": MUTED, "width": 1},
                       name="krzywa początkowa", hoverinfo="skip")
    picks = range(0, len(curves), 4)
    fig = go.Figure(data=[start, shape(0)], frames=[go.Frame(data=[start, shape(i)], name=str(i)) for i in picks])
    steps = [{"label": pl(times[i], 2), "method": "animate",
              "args": [[str(i)], {"mode": "immediate", "frame": {"duration": 0, "redraw": False}}]} for i in picks]
    tidy(fig, height=540, sliders=[{"steps": steps, "x": 0.1, "len": 0.8, "currentvalue": {"prefix": "czas t = "}}])
    fig.update_xaxes(range=[-1.8, 1.8], visible=False)
    fig.update_yaxes(range=[-1.8, 1.8], visible=False, scaleanchor="x")
    return (f"Pole krzywej maleje w tempie \\(2\\pi\\): odchylenie symulacji wynosi {pl(100 * error)} % pola "
            "początkowego", "Przepływ skracający krzywą, czyli odpowiednik przepływu Ricciego o 1 wymiar niżej. "
            "Przesuń suwak czasu i wskaż krzywą, żeby odczytać pole.", fig)


def yang_mills_density():
    _, levels, bound = mc.check_x2y2()
    grid = np.linspace(-5, 5, 161)
    density = sim.ground_density(20, grid)
    gx, gy = np.meshgrid(grid, grid)
    fig = go.Figure()
    fig.add_heatmap(x=grid, y=grid, z=density / density.max(), colorscale=SEQ, zmin=0, zmax=1,
                    colorbar={"title": "gęstość", "thickness": 12},
                    hovertemplate="x = %{x:.2f}<br>y = %{y:.2f}<br>gęstość = %{z:.3f}<extra></extra>")
    fig.add_contour(x=grid, y=grid, z=gx**2 * gy**2, showscale=False, hoverinfo="skip",
                    contours={"start": levels[0], "end": levels[0], "size": 1, "coloring": "lines"},
                    line={"color": INK2, "width": 1.5}, colorscale=[[0, INK2], [1, INK2]])
    tidy(fig, height=540, xaxis_title="x", yaxis_title="y")
    fig.update_xaxes(range=[-5, 5], constrain="domain")
    fig.update_yaxes(range=[-5, 5], scaleanchor="x", constrain="domain")
    return ("Stan podstawowy zostaje w środku, choć doliny potencjału \\(x^2y^2\\) są otwarte",
            f"Gęstość stanu podstawowego hamiltonianu \\(-\\Delta + x^2y^2\\) i kontur \\(x^2y^2 = E_0\\). "
            f"\\(E_0 = {pl(levels[0], 5).replace(',', '{,}')}\\), \\(E_1 - E_0 = "
            f"{pl(levels[1] - levels[0], 5).replace(',', '{,}')}\\), granica dolna dla \\(E_0\\): {pl(bound, 4)}.", fig)


def yang_mills_potential():
    _, levels, _ = mc.check_x2y2()
    path, _ = sim.classical_x2y2()
    reach = np.abs(path).max(axis=(1, 2))
    orbit = path[int(np.argsort(reach)[len(reach) // 4])]
    grid = np.linspace(-4, 4, 121)
    gx, gy = np.meshgrid(grid, grid)
    ox = np.where(np.abs(orbit).max(axis=1) <= 4, orbit[:, 0], np.nan)
    fig = go.Figure()
    fig.add_surface(x=grid, y=grid, z=np.minimum(gx**2 * gy**2, 2), colorscale=SEQ, showscale=False, opacity=0.9,
                    hovertemplate="x = %{x:.2f}<br>y = %{y:.2f}<br>potencjał = %{z:.3f}<extra></extra>")
    fig.add_scatter3d(x=ox, y=orbit[:, 1], z=ox**2 * orbit[:, 1] ** 2 + 0.03, mode="lines", name="orbita klasyczna",
                      line={"color": ORANGE, "width": 3}, hoverinfo="skip")
    tidy(fig, height=560, scene=scene(xaxis={"title": "x"}, yaxis={"title": "y"},
                                      zaxis={"title": "x²y²", "range": [0, 2], "tickvals": [0, 1, 2]}),
         scene_camera={"eye": {"x": 0.9, "y": -1.1, "z": 1.5}}, scene_aspectratio={"x": 1, "y": 1, "z": 0.4})
    return (f"Doliny potencjału \\(x^2y^2\\) mają dno na wysokości 0, a poziom podstawowy ma wysokość "
            f"{pl(levels[0], 3)}", "Powierzchnia potencjału obcięta na wysokości 2 oraz 1 orbita klasyczna o energii "
            "\\(E_0\\), która wchodzi w doliny. Obróć rysunek myszą.", fig)


def navier_stokes_cascade():
    lam, steps = 2.0, np.arange(0, 13)
    fig = make_subplots(1, 2, shared_yaxes=True, subplot_titles=("3 wymiary: mnożnik √(θ × λ)", "2 wymiary: mnożnik √θ"))
    for col, dim in ((1, 3), (2, 2)):
        for theta, color, text in ((0.35, BLUE, "mniej niż 1/λ"), (0.5, MUTED, "równe 1/λ"), (0.7, RED, "więcej niż 1/λ")):
            fig.add_scatter(x=steps, y=(theta * lam ** (dim - 2)) ** (steps / 2), mode="lines", row=1, col=col,
                            line={"color": color, "width": 2}, name=f"θ = {pl(theta)}: {text}", showlegend=col == 1,
                            hovertemplate="%{y:.4f}<extra>θ = " + pl(theta) + "</extra>")
    tidy(fig, hovermode="x unified", legend_y=-0.22)
    fig.update_yaxes(type="log", dtick=1)
    fig.update_yaxes(title_text="Re<sub>n</sub> / Re<sub>0</sub>", row=1, col=1)
    fig.update_xaxes(title_text="numer wiru n")
    return ("W 3 wymiarach liczba Reynoldsa rośnie tylko dla \\(\\theta > 1/\\lambda\\); w 2 wymiarach maleje",
            "Wzór modelu 2: \\(\\mathrm{Re}_n/\\mathrm{Re}_0 = (\\theta \\lambda^{d-2})^{n/2}\\) dla \\(\\lambda = 2\\). "
            "Wzór jest rachunkiem bez dowodu dla prawdziwego równania.", fig)


def p_vs_np_cube():
    _, queries, certificate = mc.check_queries(3)[-1]
    corners = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    fig = go.Figure()
    fig.add_mesh3d(x=[1, 1, 1, 1], y=[0, 1, 1, 0], z=[0, 0, 1, 1], i=[0, 0], j=[1, 2], k=[2, 3], color=BLUE,
                   opacity=0.15, hoverinfo="skip", name="ściana: pierwszy bit 1")
    for i, a in enumerate(corners):
        for b in corners[i + 1 :]:
            if sum(p != q for p, q in zip(a, b)) == 1:
                at_zero = (0, 0, 0) in (a, b)
                fig.add_scatter3d(x=[a[0], b[0]], y=[a[1], b[1]], z=[a[2], b[2]], mode="lines", hoverinfo="skip",
                                  line={"color": ORANGE if at_zero else MUTED, "width": 7 if at_zero else 3},
                                  showlegend=False)
    values = [int(any(c)) for c in corners]
    fig.add_scatter3d(x=[c[0] for c in corners], y=[c[1] for c in corners], z=[c[2] for c in corners],
                      mode="markers+text", text=["".join(map(str, c)) for c in corners], textposition="top center",
                      marker={"size": 8, "color": [BLUE if v else SURFACE for v in values],
                              "line": {"color": [SURFACE if v else ORANGE for v in values], "width": 3}},
                      customdata=values, name="wejście", showlegend=False,
                      hovertemplate="wejście %{text}<br>wartość OR: %{customdata}<extra></extra>")
    hidden = {"visible": False}
    tidy(fig, height=520, scene={"xaxis": hidden, "yaxis": hidden, "zaxis": hidden, "aspectmode": "cube"})
    return (f"Odpowiedź 1 funkcji OR ma certyfikat o {certificate} bicie, a odpowiedź 0 wymaga {queries} zapytań",
            "Sześcian 8 wejść o 3 bitach. Ściana niebieska: 4 wejścia z pierwszym bitem 1. Krawędzie pomarańczowe: "
            "3 zmiany 1 bitu, które zmieniają wartość z 0 na 1.", fig)


def p_vs_np_bounds():
    sizes = np.arange(10, 31)
    counting = [mc.shannon_min_gates(int(n)) for n in sizes]
    nodes_n, medians, slope = sim.sat_search()
    fig = make_subplots(1, 2, subplot_titles=("Dolne ograniczenia liczby bramek", "Przeszukiwanie losowych formuł 3-SAT"))
    fig.add_scatter(x=sizes, y=counting, mode="lines", line={"color": BLUE, "width": 2}, row=1, col=1,
                    name="zliczanie: co najmniej 1 funkcja", hovertemplate="%{y:,.0f} bramek<extra>zliczanie</extra>")
    fig.add_scatter(x=sizes, y=3.1 * sizes, mode="lines", line={"color": ORANGE, "width": 2}, row=1, col=1,
                    name="funkcja podana wzorem: 3,1 × n", hovertemplate="%{y:.0f} bramek<extra>wzór</extra>")
    fig.add_scatter(x=nodes_n, y=medians, mode="markers", row=1, col=2, name="mediana liczby węzłów",
                    marker={"color": BLUE, "size": 10, "line": {"color": SURFACE, "width": 1}},
                    hovertemplate="n = %{x}<br>mediana: %{y:.0f} węzłów<extra></extra>")
    tidy(fig, hovermode="x unified", legend_y=-0.22)
    fig.update_yaxes(type="log")
    fig.update_yaxes(tickvals=[5, 10, 20, 50, 100], row=1, col=2)
    fig.update_xaxes(title_text="liczba zmiennych n")
    return (f"Dla n = 20 zliczanie wymusza {thousands(mc.shannon_min_gates(20))} bramek, a ograniczenie dla funkcji "
            "podanej wzorem daje 62", f"Prawy panel: przeszukiwanie z nawrotami podwaja liczbę węzłów co "
            f"{pl(1 / slope, 1)} zmiennej. Skale pionowe są logarytmiczne.", fig)


PAGE = """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Minimalne modele 7 problemów milenijnych: rysunki interaktywne</title>
<script src="https://cdn.plot.ly/plotly-{version}.min.js" charset="utf-8"></script>
<script>window.MathJax = {{tex: {{inlineMath: [["\\\\(", "\\\\)"]]}}}};</script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-chtml.js" async></script>
<style>
  body {{ margin: 0; background: #f9f9f7; color: {ink}; font-family: {font}; line-height: 1.5; }}
  main {{ max-width: 1000px; margin: 0 auto; padding: 24px 16px 64px; }}
  h1 {{ font-size: 1.6rem; margin: 0 0 8px; }}
  h2 {{ font-size: 1.15rem; margin: 0 0 6px; }}
  p {{ margin: 0 0 10px; color: {ink2}; }}
  .warning {{ border-left: 4px solid {orange}; padding: 8px 12px; background: {surface}; color: {ink}; }}
  section {{ background: {surface}; border: 1px solid {grid}; border-radius: 6px; padding: 16px; margin-top: 20px; }}
  .tag {{ font-size: 0.8rem; color: {ink2}; text-transform: uppercase; letter-spacing: 0.04em; }}
  a {{ color: {blue}; }}
</style>
</head>
<body>
<main>
<h1>Minimalne modele 7 problemów milenijnych: rysunki interaktywne</h1>
<p class="warning"><strong>OSTRZEŻENIE:</strong> Nie cytuj żadnej propozycji z tej strony jako dowodu. Każda propozycja
dla problemu otwartego ma brakujący krok, którego dowodu autor nie zna.</p>
<p>Wskaż znak na rysunku, żeby odczytać liczby. Rysunki w 3 wymiarach obracaj myszą. 2 rysunki mają suwak czasu.
Pełny tekst zawiera plik <a href="https://github.com/maciejszulia/millennium-models/blob/main/REPORT.md">REPORT.md</a>.
Autor: Maciej Szulia, maciej.szulia@gmail.com</p>
{sections}
</main>
</body>
</html>
"""


def build():
    data = mc.bsd_series()
    figures = [
        ("Riemann", riemann_hasse()), ("Riemann, 3 wymiary", riemann_zeta()),
        ("Riemann, algorytm", riemann_counterexample_thread()),
        ("BSD", bsd_slopes(data)), ("BSD", bsd_sato_tate(data)),
        ("Model 1, 3 wymiary", model_1_torus()), ("Hodge", hodge_lattices()),
        ("Poincaré, 3 wymiary, suwak", poincare_sphere()), ("Poincaré, symulacja, suwak", poincare_curve()),
        ("Yang–Mills", yang_mills_density()), ("Yang–Mills, 3 wymiary", yang_mills_potential()),
        ("Navier–Stokes", navier_stokes_cascade()),
        ("P a NP, 3 wymiary", p_vs_np_cube()), ("P a NP", p_vs_np_bounds()),
    ]
    sections = []
    for number, (tag, (title, text, fig)) in enumerate(figures, 1):
        chart = fig.to_html(full_html=False, include_plotlyjs=False, div_id=f"figure-{number}",
                            config={"displaylogo": False, "responsive": True})
        sections.append(f'<section>\n<div class="tag">{number}. {escape(tag)}</div>\n<h2>{title}</h2>\n<p>{text}</p>\n'
                        f"{chart}\n</section>")
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(PAGE.format(version=get_plotlyjs_version(), sections="\n".join(sections), ink=INK, ink2=INK2,
                               surface=SURFACE, grid=GRID, orange=ORANGE, blue=BLUE, font=FONT), encoding="utf-8")
    print("wrote", OUT, f"({OUT.stat().st_size / 1e6:.1f} MB, {len(figures)} figures)")


if __name__ == "__main__":
    build()
