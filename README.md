# csvglance 🔍

A tiny CLI that gives you a quick health report on any CSV file before you start analysing it.

It reports row/column counts, duplicate rows, and per-column dtype, missing values, unique counts, and outliers (IQR rule).

## Install
```bash
pip install .
```

## Usage
```bash
csvglance data.csv
csvglance data.csv --json
csvglance data.tsv --sep "\t"
```

Example output:
```
Rows: 200  Columns: 3  Duplicate rows: 0

column              dtype     missing     unique  outliers
------------------------------------------------------------
coffee_cups         int64     0 (0.0%)    6       0
sleep_hours         float64   0 (0.0%)    58      2
focus_score         float64   0 (0.0%)    160     0
```

## Test
```bash
pip install pytest && pytest
```

## Roadmap
- Correlation warnings for highly correlated columns
- Detect constant and high-cardinality columns
- HTML report output

Contributions welcome. Licensed under MIT.

Made by Urukrama.
