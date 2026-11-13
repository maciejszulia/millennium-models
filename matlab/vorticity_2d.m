function [times, enstrophies, peaks, first, last] = vorticity_2d(w0, viscosity, steps, dt, every)
% VORTICITY_2D  Vorticity equation w_t + u.grad(w) = viscosity * laplace(w) on [0, 2*pi)^2.
%   The same scheme as simulations.py: pseudo-spectral, RK4, 2/3 dealiasing.
%   Theorems for 2 dimensions without forcing: enstrophy and max |w| never grow.
%   w0 is the first vorticity field (vorticity_initial.csv stores the field of simulations.py).
  if nargin < 2, viscosity = 0.01; end
  if nargin < 3, steps = 400; end
  if nargin < 4, dt = 0.02; end
  if nargin < 5, every = 10; end
  n = size(w0, 1);
  k = [0:n / 2 - 1, -n / 2:-1].';
  [g.ky, g.kx] = meshgrid(k, k);             % kx changes along the first index
  g.k2 = g.kx .^ 2 + g.ky .^ 2;
  g.inverse = zeros(n);
  g.inverse(g.k2 > 0) = 1 ./ g.k2(g.k2 > 0);
  g.keep = (abs(g.kx) < n / 3) & (abs(g.ky) < n / 3);
  g.viscosity = viscosity;
  w_hat = fft2(w0) .* g.keep;

  count = floor(steps / every) + 1;
  times = zeros(count, 1);
  enstrophies = times;
  peaks = times;
  first = real(ifft2(w_hat));
  for step = 0:steps
    if mod(step, every) == 0
      last = real(ifft2(w_hat));
      index = step / every + 1;
      times(index) = step * dt;
      enstrophies(index) = 0.5 * mean(last(:) .^ 2);
      peaks(index) = max(abs(last(:)));
    end
    k1 = rhs(w_hat, g);
    k2 = rhs(w_hat + 0.5 * dt * k1, g);
    k3 = rhs(w_hat + 0.5 * dt * k2, g);
    k4 = rhs(w_hat + dt * k3, g);
    w_hat = w_hat + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4);
  end
end

function f = rhs(w_hat, g)
  psi = w_hat .* g.inverse;                  % laplace(psi) = -w
  u = real(ifft2(1i * g.ky .* psi));
  v = real(ifft2(-1i * g.kx .* psi));
  wx = real(ifft2(1i * g.kx .* w_hat));
  wy = real(ifft2(1i * g.ky .* w_hat));
  f = -fft2(u .* wx + v .* wy) .* g.keep - g.viscosity * g.k2 .* w_hat;
end
