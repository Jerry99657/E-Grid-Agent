import os
import argparse
import json
import pandas as pd
from pathlib import Path

import src.gateway as gateway
import src.diagnoser as diagnoser
import src.optimizer as optimizer


def ensure_outdir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def run(config_path: str):
    cfg = {}
    try:
        import yaml
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = yaml.safe_load(f)
    except Exception:
        cfg = {}

    out_dir = Path("outputs/demo_run")
    ensure_outdir(out_dir)

    # 1) 收集示例数据
    df = gateway.collect_sample(num=cfg.get("num_samples", 1000))

    # 2) 诊断
    diag = diagnoser.diagnose(df)

    # 3) 优化建议
    suggestion = optimizer.optimize(df)

    # 4) 写出结果
    results_path = out_dir / "results.csv"
    df.to_csv(results_path, index=False)

    decision_log = {
        "diagnosis": diag,
        "suggestion": suggestion,
        "meta": {"config": cfg}
    }
    with open(out_dir / "decision_log.json", "w", encoding="utf-8") as f:
        json.dump(decision_log, f, indent=2)

    print("Demo 完成，输出保存在:", out_dir)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument("--config", default="demo/configs/pilot.yaml")
    args = p.parse_args()
    run(args.config)
