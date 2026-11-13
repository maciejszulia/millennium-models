function [levels, bound, density, grid] = x2y2_levels(m)
% X2Y2_LEVELS  Lowest levels of -Laplace + x^2 y^2 and the lower bound for the ground level.
%   The same construction as models_check.py, check 5: an m x m basis of oscillator states.
%   levels   the 4 lowest levels over the 4 parity sectors
%   bound    lowest level of -d^2/dx^2 + |x|, the first zero of the derivative of the Airy function
%   density  |psi_0(x, y)|^2 of the ground state on grid x grid
  if nargin < 1, m = 20; end
  levels = [];
  for px = 0:1
    for py = 0:1
      e = sort(eig(hamiltonian(m, px, py)));
      levels = [levels; e(1:3)];
    end
  end
  levels = sort(levels);
  levels = levels(1:4);
  bound = -fzero(@(z) airy(1, z), -1);

  [vectors, values] = eig(hamiltonian(m, 0, 0));
  [~, lowest] = min(diag(values));
  coefficients = reshape(vectors(:, lowest), m, m).';   % row index: state in x, column index: state in y
  grid = linspace(-5, 5, 201);
  phi = zeros(2 * m, numel(grid));                      % normalised eigenfunctions of p^2 + x^2
  phi(1, :) = pi^(-0.25) * exp(-grid .^ 2 / 2);
  phi(2, :) = sqrt(2) * grid .* phi(1, :);
  for n = 1:(2 * m - 2)
    phi(n + 2, :) = sqrt(2 / (n + 1)) * grid .* phi(n + 1, :) - sqrt(n / (n + 1)) * phi(n, :);
  end
  even = phi(1:2:end, :);
  density = (even.' * coefficients * even) .^ 2;
end

function [n, a] = x2_matrix(m, parity)
% <n|x^2|n'> between eigenstates n = 2k + parity (k < m) of h = p^2 + x^2.
  n = 2 * (0:m - 1).' + parity;
  off = sqrt((n(1:end - 1) + 1) .* (n(1:end - 1) + 2)) / 2;
  a = diag(n + 0.5) + diag(off, 1) + diag(off, -1);
end

function h = hamiltonian(m, px, py)
% -Laplace + x^2 y^2 in the product basis with parities px, py.
  [nx, ax] = x2_matrix(m, px);
  [ny, ay] = x2_matrix(m, py);
  kx = diag(2 * nx + 1) - ax;                           % p_x^2 = h_x - x^2
  ky = diag(2 * ny + 1) - ay;
  h = kron(kx, eye(m)) + kron(eye(m), ky) + kron(ax, ay);
end
