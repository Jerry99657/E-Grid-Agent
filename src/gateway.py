def collect_sample(num=1000):
    """生成示例采样数据的占位函数（真实场景由边缘网关替换）。"""
    import numpy as np
    import pandas as pd
    t = np.arange(num)
    voltage = 230 + 5 * np.sin(2 * 3.1415 * t / 50) + np.random.normal(0, 0.5, size=num)
    current = 8 + 2 * np.sin(2 * 3.1415 * t / 40) + np.random.normal(0, 0.8, size=num)
    df = pd.DataFrame({"voltage": voltage, "current": current})
    return df
