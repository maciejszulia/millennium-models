function [times, areas, ratios, curves] = curve_shortening(points, frames, stop)
% CURVE_SHORTENING  Flow dz/dt = curvature * normal for a closed non-convex curve.
%   The same scheme as simulations.py. Theorem (Gage, Hamilton, Grayson): the area falls
%   at the rate 2*pi and the curve becomes round.
%   Returns the times, the areas, the isoperimetric ratios L^2 / (4*pi*A) and the curves (one column per frame).
  if nargin < 1, points = 160; end
  if nargin < 2, frames = 60; end
  if nargin < 3, stop = 0.9; end
  phi = (0:points - 1).' * 2 * pi / points;
  z = resample((1 + 0.45 * cos(3 * phi) + 0.2 * sin(2 * phi)) .* exp(1i * phi));
  lifetime = polygon_area(z) / (2 * pi);
  t = 0;
  times = zeros(frames + 1, 1);
  areas = times;
  ratios = times;
  curves = zeros(points, frames + 1);
  for k = 0:frames
    target = k * stop * lifetime / frames;
    while t < target
      ahead = circshift(z, -1) - z;
      behind = z - circshift(z, 1);
      d1 = abs(ahead);
      d2 = abs(behind);
      dt = min(0.2 * min([d1; d2]) ^ 2, target - t);
      z = resample(z + dt * 2 ./ (d1 + d2) .* (ahead ./ d1 - behind ./ d2));   % second derivative in arc length
      t = t + dt;
    end
    len = sum(abs(circshift(z, -1) - z));
    times(k + 1) = t;
    areas(k + 1) = polygon_area(z);
    ratios(k + 1) = len ^ 2 / (4 * pi * areas(k + 1));
    curves(:, k + 1) = z;
  end
end

function z = resample(z)
% The same closed polygon with points at equal arc-length spacing.
  closed = [z; z(1)];
  s = [0; cumsum(abs(diff(closed)))];
  target = (0:numel(z) - 1).' * s(end) / numel(z);
  z = interp1(s, real(closed), target) + 1i * interp1(s, imag(closed), target);
end

function a = polygon_area(z)
  a = 0.5 * sum(imag(conj(z) .* circshift(z, -1)));
end
