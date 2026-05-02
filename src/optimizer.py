from typing import Dict

def optimize(observations) -> Dict:
    """基于观测简单建议开关频率和死区时间的调整（示例逻辑）。
    observations: dict or dataframe
    返回：建议字典
    """
    # 这里是占位逻辑：如果电流波动大，提升开关频率并略微增大死区
    avg_i = None
    try:
        avg_i = observations["current"].abs().mean()
    except Exception:
        avg_i = None
    suggestion = {"set_freq_kHz": 20.0, "deadtime_us": 1.0, "confidence": 0.3}
    if avg_i is not None:
        if avg_i > 10:
            suggestion["set_freq_kHz"] = 25.0
            suggestion["deadtime_us"] = 1.5
            suggestion["confidence"] = 0.75
        else:
            suggestion["set_freq_kHz"] = 18.0
            suggestion["deadtime_us"] = 0.9
            suggestion["confidence"] = 0.6
    return suggestion
