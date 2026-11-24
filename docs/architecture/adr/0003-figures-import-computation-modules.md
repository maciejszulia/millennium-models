# ADR 0003: Figure scripts import the computation modules

## Status

Accepted (commits `d754911`, `d39d3c9`).

## Context

The repository has 24 static figures and 16 interactive figures. If figure scripts computed their own numbers, a figure could show a value that the checks never verified.

## Decision

`models_check.py` and `simulations.py` are the only sources of numbers. `figures.py`, `animations.py` and `interactive.py` import them (`import models_check as mc`, `import simulations as sim`) and reuse their formatting helpers (`pl`, `thousands`). `animations.py` also imports the style helpers of `figures.py`. The Octave run reads the initial vorticity field that `simulations.py` produces, stored in `matlab/vorticity_initial.csv`.

## Consequences

- Positive: a figure shows the same number as the check and the report.
- Positive: one style module keeps titles, colours and tick formatting consistent.
- Negative: figure scripts rerun the computations, so drawing all figures takes minutes (README: `figures.py` 46 s, `animations.py` 66 s, `interactive.py` 24 s).
- Negative: `models_check.py` and `simulations.py` import each other inside functions to avoid an import cycle.

## Evidence

- `figures.py`, `animations.py`, `interactive.py`: import lines at the top of each file.
- `interactive.py` docstring: "Every number comes from models_check.py or simulations.py."
- `simulations.py`, `initial_vorticity()` docstring about `matlab/vorticity_initial.csv`.
