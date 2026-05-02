import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


def main():
    out_dir = Path("outputs/demo_run")
    csv = out_dir / "results.csv"
    if not csv.exists():
        print("未找到 outputs/demo_run/results.csv — 先运行 demo/run_demo.py")
        sys.exit(1)
    df = pd.read_csv(csv)
    fig, ax = plt.subplots(2, 1, figsize=(10, 6), sharex=True)
    ax[0].plot(df["voltage"], label="voltage")
    ax[0].legend()
    ax[1].plot(df["current"], label="current", color="orange")
    ax[1].legend()
    plt.tight_layout()
    out_png = out_dir / "summary.png"
    plt.savefig(out_png)
    print("已生成", out_png)


if __name__ == '__main__':
    main()
