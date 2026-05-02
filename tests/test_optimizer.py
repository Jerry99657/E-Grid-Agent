import pandas as pd
import numpy as np
from src import optimizer


def test_optimize_keys():
    df = pd.DataFrame({"current": [1, 2, 3]})
    s = optimizer.optimize(df)
    assert isinstance(s, dict)
    assert "set_freq_kHz" in s and "deadtime_us" in s


def test_optimize_high_current():
    df = pd.DataFrame({"current": [20, 22, 19, 21]})
    s = optimizer.optimize(df)
    assert s["set_freq_kHz"] >= 20
    assert s["confidence"] >= 0.7
