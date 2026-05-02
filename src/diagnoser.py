import numpy as np
import pandas as pd

def diagnose(df: pd.DataFrame) -> dict:
    """简单基于电压/电流滚动统计的异常检测，返回异常摘要。"""
    window = 50
    res = {"anomalies": []}
    if "voltage" not in df.columns or "current" not in df.columns:
        return res
    v_std = df["voltage"].rolling(window=window, min_periods=1).std()
    i_std = df["current"].rolling(window=window, min_periods=1).std()
    thr_v = v_std.mean() + 3 * v_std.std()
    thr_i = i_std.mean() + 3 * i_std.std()
    v_idx = df.index[v_std > thr_v].tolist()
    i_idx = df.index[i_std > thr_i].tolist()
    if v_idx:
        res["anomalies"].append({"type": "voltage_spike", "count": len(v_idx), "indices": v_idx[:10]})
    if i_idx:
        res["anomalies"].append({"type": "current_spike", "count": len(i_idx), "indices": i_idx[:10]})
    return res
