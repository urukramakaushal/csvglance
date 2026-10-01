import pandas as pd
from csvglance.core import profile


def test_profile_basic():
    df = pd.DataFrame({"a": [1, 2, 2, 100], "b": ["x", None, "y", "y"]})
    r = profile(df)
    assert r["rows"] == 4
    assert r["columns_detail"]["b"]["missing"] == 1
    assert r["columns_detail"]["a"]["outliers"] == 1


def test_duplicates():
    df = pd.DataFrame({"a": [1, 1], "b": [2, 2]})
    assert profile(df)["duplicate_rows"] == 1
