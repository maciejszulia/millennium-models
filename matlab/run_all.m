% RUN_ALL  Run the 3 simulations, compare the numbers with REPORT.md and write 3 figures.
%   GNU Octave 11, from the repository root:  octave-cli matlab/run_all.m
%   MATLAB:                                   cd matlab; run_all
here = fileparts(mfilename('fullpath'));
addpath(here);
set(0, 'defaultaxesfontname', 'Nimbus Sans', 'defaulttextfontname', 'Nimbus Sans');   % a font with Polish letters
out = fullfile(here, '..', 'figures');
if exist('OCTAVE_VERSION', 'builtin') && strcmp(graphics_toolkit(), 'gnuplot')
  device = '-dpngcairo';   % the png terminal of gnuplot drops Polish letters, cairo draws them
else
  device = '-dpng';
end
pl = @(x, digits) strrep(sprintf('%.*f', digits, x), '.', ',');
commas = @(ax, name) set(ax, [name 'ticklabel'], strtrim(strrep(cellstr(num2str(get(ax, [name 'tick']).')), '.', ',')));
blue = [42 120 214] / 255;
orange = [235 104 52] / 255;
ink = [82 81 78] / 255;
ramp = [linspace(0.99, 0.05, 64).', linspace(0.99, 0.21, 64).', linspace(0.98, 0.42, 64).'];
half = linspace(0, 1, 32).';
diverging = [blue + (0.93 - blue) .* half; 0.93 + (orange - 0.93) .* half];

% 1. Yang-Mills cross-section: levels of -Laplace + x^2 y^2 (REPORT.md, check 5)
[levels, bound, density, points] = x2y2_levels(20);
fprintf('[octave 1] levels %.5f, %.5f; gap %.5f; lower bound %.4f\n', levels(1), levels(2), levels(2) - levels(1), bound);
assert(abs(levels(1) - 1.10822) < 5e-6 && abs(levels(2) - 2.37864) < 5e-6);
assert(abs(bound - 1.0188) < 5e-5 && bound <= levels(1));

fig = figure('visible', 'off', 'position', [0 0 1100 700]);
surf(points, points, density, 'edgecolor', 'none');
colormap(gca, ramp);
view(-38, 48);
axis([-5 5 -5 5 0 0.25]);
grid off;
xlabel('x'); ylabel('y');
title(sprintf('Gęstość stanu podstawowego zostaje w środku: E_0 = %s, granica dolna %s', pl(levels(1), 5), pl(bound, 4)), 'color', ink);
commas(gca, 'z');
print(fig, fullfile(out, 'octave-x2y2-ground-state.png'), device, '-r150');
close(fig);

% 2. Poincare, one dimension lower: curve shortening (REPORT.md, check 9)
[times, areas, ratios, curves] = curve_shortening();
area_error = max(abs(areas - (areas(1) - 2 * pi * times))) / areas(1);
fprintf('[octave 2] area error %.2f %%; isoperimetric ratio %.3f -> %.4f\n', 100 * area_error, ratios(1), ratios(end));
assert(abs(100 * area_error - 0.83) < 0.005 && abs(ratios(1) - 1.732) < 5e-4 && abs(ratios(end) - 1.0008) < 5e-5);

fig = figure('visible', 'off', 'position', [0 0 1300 600]);
subplot(1, 2, 1);
hold on;
shades = linspace(0.75, 0, 5);
frames = [1 16 31 46 61];
for j = 1:5
  z = curves(:, frames(j));
  plot(real([z; z(1)]), imag([z; z(1)]), 'color', blue + (1 - blue) * shades(j), 'linewidth', 2);
end
axis equal; axis off;
title(sprintf('Krzywa staje się okręgiem: iloraz %s \\rightarrow %s', pl(ratios(1), 3), pl(ratios(end), 4)), 'color', ink);
subplot(1, 2, 2);
plot(times, areas(1) - 2 * pi * times, '-', 'color', orange, 'linewidth', 2);
hold on;
plot(times(1:4:end), areas(1:4:end), 'o', 'color', blue, 'markerfacecolor', blue, 'markersize', 5);
xlabel('czas t'); ylabel('pole');
legend({'prosta A_0 - 2\pi t', 'pole z symulacji'}, 'location', 'northeast');
legend('boxoff');
title(sprintf('Pole maleje w tempie 2\\pi: odchylenie %s %% pola początkowego', pl(100 * area_error, 2)), 'color', ink);
commas(gca, 'x'); commas(gca, 'y');
print(fig, fullfile(out, 'octave-curve-shortening.png'), device, '-r150');
close(fig);

% 3. Navier-Stokes in 2 dimensions (REPORT.md, check 10)
w0 = dlmread(fullfile(here, 'vorticity_initial.csv'), ',');
[times, enstrophies, peaks, first, last] = vorticity_2d(w0);
fprintf('[octave 3] enstrophy %.3f -> %.3f; max |w| %.2f -> %.2f\n', enstrophies(1), enstrophies(end), peaks(1), peaks(end));
assert(abs(enstrophies(1) - 2.206) < 5e-4 && abs(enstrophies(end) - 1.147) < 5e-4);
assert(abs(peaks(1) - 6.00) < 5e-3 && abs(peaks(end) - 4.51) < 5e-3);
assert(all(diff(enstrophies) <= 0) && max(peaks) <= peaks(1) * (1 + 1e-9));
peak_rise = max(diff(peaks) ./ peaks(1:end - 1));
fprintf('[octave 3] largest rise of max |w| between 2 samples %.2f %%\n', 100 * peak_rise);
assert(abs(100 * peak_rise - 0.25) < 0.005);

fig = figure('visible', 'off', 'position', [0 0 1500 520]);
fields = {first, last};
names = {'Wirowość w chwili 0', sprintf('Wirowość w chwili %d', round(times(end)))};
for j = 1:2
  subplot(1, 3, j);
  imagesc(fields{j}.', [-6 6]);
  colormap(gca, diverging);
  axis image; axis off;
  title(names{j}, 'color', ink);
end
subplot(1, 3, 3);
plot(times, enstrophies, '-', 'color', blue, 'linewidth', 2);
xlabel('czas t'); ylabel('enstrofia');
ylim([0 2.5]);
title(sprintf('Enstrofia maleje: %s \\rightarrow %s', pl(enstrophies(1), 3), pl(enstrophies(end), 3)), 'color', ink);
commas(gca, 'y');
print(fig, fullfile(out, 'octave-vorticity-2d.png'), device, '-r150');
close(fig);

fprintf('all octave checks passed\n');
