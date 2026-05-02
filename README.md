# e-grid-agent

一套面向电力电子设备（如逆变器、变流器与电源管理单元）的多 Agent 智能运维与在线优化参考实现。

本仓库提供轻量级演示代码、仿真脚本与复现所需的示例数据，便于快速搭建从数据采集、异常诊断到参数优化建议的端到端流程，实现边缘推理与云端验证的混合工作流。

核心目标

- 为电力电子设备提供可审计的自动诊断与在线优化建议，缩短故障定位时间并提升运行效率。
- 提供可复现的 Demo，使开发者能够在仿真或少量实机上验证策略效果并扩展到 Pilot 部署。

主要特性

- 实时/批量数据采集占位器（`src/gateway.py`）
- 基于统计的快速诊断 Agent（`src/diagnoser.py`）
- 简易优化建议 Agent（`src/optimizer.py`），示例性输出用于策略验证
- 决策日志与结果导出（CSV / JSON），便于审计与离线分析
- 可运行的 Demo（`demo/run_demo.py`）与可视化脚本（`demo/plot_results.py`）

架构概览

1. 边缘网关：负责数据采样、本地预处理与推理触发（示例为 `src/gateway.py`）。
2. 诊断 Agent：对采样波形进行异常检测与根因提示，生成诊断摘要。
3. 优化 Agent：在安全规则层之上提供参数调整建议（如开关频率、死区时间），建议先在数字孪生或仿真中验证再下发真实设备。
4. 日志与回放：所有决策均记录为 `decision_log.json`，并将原始数据导出为 CSV 以供离线分析。

快速开始

Windows PowerShell 示例：

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python demo/run_demo.py --config demo/configs/pilot.yaml
python demo/plot_results.py
```

运行后输出位于 `outputs/demo_run/`，其中包含 `results.csv`（原始波形）和 `decision_log.json`（诊断与建议）。

仓库结构（简要）

- `src/` — 核心 Agent 与数据接口代码（`diagnoser.py`, `optimizer.py`, `gateway.py`）
- `demo/` — 演示脚本、配置与可视化工具
- `data/` — 示例输入数据与日志片段
- `outputs/` — Demo 运行产物（在运行后生成）
- `requirements.txt` — Python 依赖

如何用在真实工程中（建议步骤）

1. 替换网关数据接入为真实采样接口（ADC / CAN / Modbus / IEC61850）。
2. 把示例诊断与优化模块替换为经训练/验证的模型（轻量化网络或规则引擎）。
3. 在数字孪生环境中回放决策并进行安全验证，确保控制建议在边界条件下可回滚。
4. 增加访问控制、审计链与报警策略，保证自动化决策可人工覆盖并生成工单。

贡献

欢迎提交 Issue 与 Pull Request。请在 PR 描述中包含复现步骤、输入数据样例与预期行为。

许可证

本示例模板采用 MIT 许可证（若需更改请在仓库中添加 `LICENSE` 文件）。

