#!/usr/bin/env python3
"""Animate the simulations of simulations.py with matplotlib (three GIF files and one PNG in figures/).

Every number in a title comes from the simulation that models_check.py asserts.
Run: python3 animations.py   (needs numpy, matplotlib and pillow; takes about 1 minute)
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter
from matplotlib.colors import LinearSegmentedColormap

import simulations as sim
from figures import BLUE, INK2, LINE, MUTED, ORANGE, OUT, RED, RING, SEQ, SURFACE, comma_ticks, frame, panel_title, save, style
from models_check import pl


def save_gif(fig, update, frames, name, fps=8):
    OUT.mkdir(exist_ok=True)
    FuncAnimation(fig, update, frames=frames, blit=False).save(OUT / name, writer=PillowWriter(fps=fps), dpi=80)
    plt.close(fig)
    print("wrote", OUT / name)


def animate_curve_shortening():
    times, areas, ratios, curves = sim.curve_shortening()
    error = float(np.abs(areas - (areas[0] - 2 * np.pi * times)).max() / areas[0])
    fig, (left, right) = frame(
        rf"Pole krzywej maleje w tempie $2\pi$: odchylenie symulacji wynosi {pl(100 * error)} % pola początkowego",
        "Przepływ skracający krzywą, czyli odpowiednik przepływu Ricciego o 1 wymiar niżej. "
        "Lewy panel: krzywa w czasie.\n"
        r"Prawy panel: pole obszaru wewnątrz krzywej i prosta $A(t) = A_0 - 2\pi t$.",
        "Źródło: simulations.py, sprawdzian 9. Twierdzenie: Gage, Hamilton 1986; Grayson 1987. "
        f"Iloraz izoperymetryczny spada z {pl(ratios[0], 3)} do {pl(ratios[-1], 4)}.",
        ncols=2, width_ratios=[0.9, 1.1],
    )
    first = np.append(curves[0], curves[0][0])
    left.plot(first.real, first.imag, color=MUTED, lw=1)
    (line,) = left.plot([], [], color=BLUE, lw=2)
    left.set(xlim=(-1.8, 1.8), ylim=(-1.8, 1.8), aspect="equal")
    left.axis("off")
    panel_title(left, "Krzywa początkowa (szara) i krzywa w chwili t (niebieska)")
    right.plot(times, areas[0] - 2 * np.pi * times, color=INK2, lw=1.3, label=r"prosta $A_0 - 2\pi t$")
    (dots,) = right.plot([], [], "o", color=BLUE, markeredgecolor=SURFACE, markeredgewidth=RING, markersize=6,
                         label="pole z symulacji")
    right.set(xlim=(0, times[-1] * 1.05), ylim=(0, areas[0] * 1.08), xlabel="czas t", ylabel="pole A")
    comma_ticks(right.xaxis, 1)
    comma_ticks(right.yaxis, 1)
    right.legend(loc="upper right")
    panel_title(right, "Pole obszaru wewnątrz krzywej")

    def update(i):
        closed = np.append(curves[i], curves[i][0])
        line.set_data(closed.real, closed.imag)
        dots.set_data(times[: i + 1 : 2], areas[: i + 1 : 2])

    save_gif(fig, update, range(0, len(curves), 2), "poincare-curve-shortening.gif")


def animate_vorticity():
    times, _, enstrophies, peaks, fields = sim.vorticity_2d()
    diverging = LinearSegmentedColormap.from_list("diverging", [BLUE, "#f0efec", RED])
    fig, (left, right) = frame(
        "W 2 wymiarach enstrofia i największa wirowość nie rosną:\n"
        f"enstrofia spada z {pl(enstrophies[0], 3)} do {pl(enstrophies[-1], 3)}",
        "Równania Naviera–Stokesa na torusie w 2 wymiarach, bez siły zewnętrznej. "
        r"Lewy panel: wirowość $\omega$." "\n"
        "Prawy panel: enstrofia i największa wirowość jako ułamek wartości początkowej.",
        "Źródło: simulations.py, sprawdzian 10. Siatka 64 × 64, lepkość 0,01, metoda pseudospektralna, "
        f"czas od 0 do {pl(times[-1], 0)}.",
        ncols=2, width_ratios=[0.9, 1.1],
    )
    image = left.imshow(fields[0].T, origin="lower", cmap=diverging, vmin=-peaks[0], vmax=peaks[0],
                        extent=(0, 2 * np.pi, 0, 2 * np.pi), interpolation="bilinear")
    left.set(xlabel="x", ylabel="y")
    left.grid(False)
    panel_title(left, "Wirowość: kolor niebieski ujemna, kolor czerwony dodatnia")
    right.axhline(1, color=INK2, lw=1.1)
    (enstrophy_line,) = right.plot([], [], color=BLUE, label="enstrofia")
    (peak_line,) = right.plot([], [], color=ORANGE, label="największa wirowość")
    right.set(xlim=(0, times[-1]), ylim=(0, 1.1), xlabel="czas t", ylabel="ułamek wartości początkowej")
    comma_ticks(right.yaxis, 1)
    right.legend(loc="lower left")
    panel_title(right, "Żadna z 2 wielkości nie przekracza wartości początkowej")

    def update(i):
        image.set_data(fields[i].T)
        enstrophy_line.set_data(times[: i + 1], enstrophies[: i + 1] / enstrophies[0])
        peak_line.set_data(times[: i + 1], peaks[: i + 1] / peaks[0])

    save_gif(fig, update, range(len(fields)), "navier-stokes-vorticity-2d.gif")


def animate_classical_orbit():
    path, _ = sim.classical_x2y2()
    reach = np.abs(path).max(axis=(1, 2))
    mass = sim.quantum_mass_outside(20, 3)
    k = int(np.argsort(reach)[len(reach) // 4])  # an orbit that stays inside the frame
    distance = np.abs(path[k]).max(axis=1)
    times = np.arange(distance.size) * 25 * 0.002
    grid = np.linspace(-16, 16, 641)
    density = sim.ground_density(20, grid)
    fig, (left, right) = frame(
        f"Każda z {reach.size} orbit klasycznych wychodzi poza kwadrat o boku 6,\n"
        f"a stan kwantowy ma poza kwadratem {pl(100 * mass)} % masy",
        r"Potencjał $x^2y^2$ o otwartych dolinach. Lewy panel: gęstość stanu podstawowego (niebieska) "
        "i 1 orbita klasyczna (pomarańczowa)\n"
        r"o energii $E_0$. Prawy panel: odległość orbity od środka, czyli większa z liczb $|x|$, $|y|$.",
        "Źródło: simulations.py, sprawdzian 11. Orbity startują ze środka w 32 kierunkach. "
        f"Orbita z rysunku dochodzi do odległości {pl(reach[k], 1)}.",
        ncols=2, width_ratios=[0.9, 1.1],
    )
    left.imshow(density / density.max(), extent=(-16, 16, -16, 16), origin="lower", cmap=SEQ, vmin=0, vmax=1)
    gx, gy = np.meshgrid(grid, grid)
    left.contour(gx, gy, gx**2 * gy**2, levels=[sim.GROUND_LEVEL], colors=[INK2], linewidths=0.8)
    left.plot([-3, 3, 3, -3, -3], [-3, -3, 3, 3, -3], color=INK2, lw=1.1)
    (orbit,) = left.plot([], [], color=ORANGE, lw=1.2)
    left.set(xlim=(-16, 16), ylim=(-16, 16), xlabel="x", ylabel="y", aspect="equal")
    left.grid(False)
    panel_title(left, r"Kontur $x^2y^2 = E_0$ i kwadrat o boku 6")
    right.axhline(3, color=INK2, lw=1.1)
    right.text(15, 3.4, "granica kwadratu o boku 6", ha="left", fontsize=8.5, color=INK2)
    (trace,) = right.plot([], [], color=ORANGE)
    right.set(xlim=(0, times[-1]), ylim=(0, 16), xlabel="czas t", ylabel="odległość od środka")
    panel_title(right, "Orbita wraca z doliny i wchodzi w następną dolinę")

    def update(i):
        orbit.set_data(path[k, :i, 0], path[k, :i, 1])
        trace.set_data(times[:i], distance[:i])

    save_gif(fig, update, range(0, distance.size + 1, 50), "yang-mills-classical-orbit.gif")


def figure_sat_search():
    sizes, medians, slope = sim.sat_search()
    fit = np.polyfit(sizes, np.log2(medians), 1)
    fig, (ax,) = frame(
        f"Przeszukiwanie z nawrotami rośnie wykładniczo: liczba węzłów podwaja się co {pl(1 / slope, 1)} zmiennej",
        "Mediana liczby węzłów przeszukiwania dla 25 losowych formuł 3-SAT na każdy rozmiar, "
        "przy 4,26 klauzuli na zmienną.\nSkala pionowa jest logarytmiczna, więc wzrost wykładniczy daje prostą.",
        f"Źródło: simulations.py, sprawdzian 12. Nachylenie prostej: {pl(slope, 3)} bitu na zmienną.",
    )
    ax.plot(sizes, 2 ** np.polyval(fit, sizes), color=INK2, lw=1.3, label="prosta dopasowana")
    ax.plot(sizes, medians, "o", color=BLUE, markeredgecolor=SURFACE, markeredgewidth=RING, markersize=8,
            label="mediana z symulacji", zorder=3)
    ax.set_yscale("log", base=2)
    ax.set_yticks([4, 8, 16, 32, 64, 128], ["4", "8", "16", "32", "64", "128"])
    ax.set(xlabel="liczba zmiennych n", ylabel="liczba węzłów przeszukiwania")
    ax.legend(loc="upper left")
    save(fig, "p-vs-np-sat-search.png")


if __name__ == "__main__":
    style()
    animate_curve_shortening()
    animate_vorticity()
    animate_classical_orbit()
    figure_sat_search()
