import pandas as pd
import numpy as np
from src import diagnoser


def test_diagnose_no_columns():
    df = pd.DataFrame({"x": [1, 2, 3]})
    res = diagnoser.diagnose(df)
    assert isinstance(res, dict)
    assert "anomalies" in res


def test_diagnose_detect_spike():
    # create voltage with a spike
    v = np.ones(200) * 230
    v[100] = 260
    i = np.ones(200) * 8
    df = pd.DataFrame({"voltage": v, "current": i})
    res = diagnoser.diagnose(df)
    assert isinstance(res, dict)
    assert "anomalies" in res
