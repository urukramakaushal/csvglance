import pandas as pd


def profile(df: pd.DataFrame) -> dict:
    """Return a quick health report for a DataFrame."""
    cols = {}
    for c in df.columns:
        s = df[c]
        info = {
            "dtype": str(s.dtype),
            "missing": int(s.isna().sum()),
            "missing_pct": round(100 * s.isna().mean(), 1),
            "unique": int(s.nunique()),
        }
        if pd.api.types.is_numeric_dtype(s):
            q1, q3 = s.quantile(0.25), s.quantile(0.75)
            iqr = q3 - q1
            info["outliers"] = int(((s < q1 - 1.5 * iqr) | (s > q3 + 1.5 * iqr)).sum())
            info["min"], info["max"] = float(s.min()), float(s.max())
        cols[c] = info
    return {
        "rows": len(df),
        "columns": len(df.columns),
        "duplicate_rows": int(df.duplicated().sum()),
        "columns_detail": cols,
    }


def format_report(rep: dict) -> str:
    lines = [
        f"Rows: {rep['rows']}  Columns: {rep['columns']}  Duplicate rows: {rep['duplicate_rows']}",
        "",
        f"{'column':<20}{'dtype':<10}{'missing':<12}{'unique':<8}{'outliers'}",
        "-" * 60,
    ]
    for name, i in rep["columns_detail"].items():
        miss = f"{i['missing']} ({i['missing_pct']}%)"
        lines.append(f"{name[:19]:<20}{i['dtype']:<10}{miss:<12}{i['unique']:<8}{i.get('outliers', '-')}")
    return "\n".join(lines)
