import argparse
import json
import pandas as pd
from .core import profile, format_report


def main():
    p = argparse.ArgumentParser(prog="csvglance", description="Quick health report for a CSV file.")
    p.add_argument("path", help="Path to CSV file")
    p.add_argument("--json", action="store_true", help="Output as JSON")
    p.add_argument("--sep", default=",", help="Delimiter (default ',')")
    a = p.parse_args()
    rep = profile(pd.read_csv(a.path, sep=a.sep))
    print(json.dumps(rep, indent=2) if a.json else format_report(rep))


if __name__ == "__main__":
    main()
