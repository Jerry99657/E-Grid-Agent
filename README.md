# E-Grid Agent — 电力电子智能运维与优化 Agent

本仓库为 E-Grid Agent 的轻量模板，演示如何在本地仿真与边缘环境中运行一个简单的诊断（diagnoser）与优化（optimizer） Agent 流程。

快速说明：

- 特性：示例数据采集、异常检测、参数优化建议、决策日志输出
- 目录：`src`（Agent 代码）、`demo`（演示脚本）、`data`（示例输入）、`outputs`（演示产物）

快速开始：

1. 创建虚拟环境并安装依赖：

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
pip install -r requirements.txt
```

2. 运行仿真 Demo：

```bash
python demo/run_demo.py --config demo/configs/pilot.yaml
```

3. 查看输出：`outputs/demo_run/results.csv` 和 `outputs/demo_run/decision_log.json`。

说明：此模板为展示用途。真实项目请替换模型与数据采集模块，并在部署前完成安全约束与仿真验证。
