# ADR 0001: Report numbers checked by code

## Status

Accepted (commit `d754911`).

## Context

`REPORT.md` quotes many computed numbers: bounds, eigenvalues, slopes, ratios. A number copied by hand into the report can drift from the code after a change, and a reader cannot tell which numbers are current.

## Decision

`models_check.py` computes every quoted number and, when `REPORT.md` exists next to it, builds a list of the numbers formatted as the report writes them (decimal comma, thousands separators, LaTeX for scientific notation). It reads `REPORT.md`, normalises the LaTeX decimal comma `{,}` and asserts that each number appears in the text. A missing number ends the run with `REPORT.md does not quote: [...]`. `matlab/run_all.m` asserts the Octave results against the values in the report in the same way.

## Consequences

- Positive: CI fails when the report and the code disagree.
- Positive: the report and the checks share one formatting function (`pl()`), so the comparison is exact.
- Negative: the check is a substring search; it confirms that a number appears, not that it appears in the right sentence.
- Negative: rewording a number in the report (for example, rounding) needs a matching code change.

## Evidence

- `models_check.py`, the block after `report = Path(__file__).with_name("REPORT.md")`.
- `matlab/run_all.m`, header comment "compare the numbers with REPORT.md" and the `assert` calls.
- `.github/workflows/ci.yml`, step "Run the 16 checks and compare the numbers quoted in REPORT.md".
