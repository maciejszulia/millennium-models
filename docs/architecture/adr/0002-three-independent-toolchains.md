# ADR 0002: Three independent toolchains

## Status

Accepted (commit `91e2ff7`).

## Context

Numerical checks in one language can share one bug. Proof cores written in prose are not machine-checked. The author's computer has no MATLAB (`REPORT.md`, "Decyzje i braki", row 11).

## Decision

Three toolchains check different parts of the work:

- Python (`models_check.py`, `simulations.py`) computes the 16 checks.
- Lean 4 with Mathlib (`lean/MillenniumModels/Proofs.lean`) checks 16 theorems on the cores of the short proofs; geometry and analysis facts enter as hypotheses.
- GNU Octave 11.3.0 runs 3 simulations written in MATLAB (`matlab/`) and compares them with the report; `x2y2_levels.m` computes the lower bound by a different method (Airy function zero).

CI runs each toolchain as its own job.

## Consequences

- Positive: a mistake must appear in two languages, or in the prose and in Lean, to pass unnoticed.
- Positive: the MATLAB files run without a MATLAB licence.
- Negative: three environments to maintain; Mathlib needs about 7.3 GB of disk.
- Negative: the MATLAB files are not tested in MATLAB itself.
- Negative: Lean depends on release candidate `v4.36.0-rc2`.

## Evidence

- `.github/workflows/ci.yml`, jobs `checks`, `lean`, `octave`.
- `lean/lakefile.toml`, `lean/lean-toolchain`.
- `matlab/run_all.m`.
- Commit `91e2ff7`: "Add Lean proofs, MATLAB simulations run by GNU Octave".
