# Opportunity Loop (fixed method → schedulable)

TrustMRR × competition × X 验证 的**固定流水线**。  
你只需要挂定时任务跑 `run.sh`；需要深度判断时再跑 Agent 阶段。

```
loop/
├── README.md              ← 本文件
├── SCHEDULE.md            ← cron / launchd / GitHub Actions / Claude /loop
├── config.json            ← 阈值与关键词（唯一策略旋钮）
├── pipeline.py            ← Stage A：拉 TrustMRR + 粗筛 + 聚类 + 报告
├── run.sh                 ← 调度入口
├── AGENT_PROMPT.md        ← Stage B：X 验证 + GO 方向完整包
├── templates/
│   └── direction.md       ← GO 方向输出模板（PRD+14d+30d）
├── state/
│   └── last_run.json      ← 上次运行指针（pipeline 自动写）
└── runs/
    └── YYYY-MM-DD_HHMMSS/ ← 每次运行只增不改
        ├── trustmrr_raw.json
        ├── filtered.json
        ├── candidates.csv
        ├── handles.csv
        ├── REPORT.md
        ├── VERDICT.md          (agent)
        └── directions/*.md     (agent, GO only)
```

## 一键跑 Stage A

```bash
cd /Users/jerry/code/10k-in-month/loop
chmod +x run.sh
./run.sh
```

输出：`runs/<id>/REPORT.md` + 更新 `state/last_run.json`。

## Stage B（完整 GO 包）

用 Claude / 其他 agent 执行：

```text
Read loop/state/last_run.json and execute loop/AGENT_PROMPT.md exactly.
```

## 与旧文档关系

| 旧文档 | 角色 |
|---|---|
| `reports/trustmrr-x-opportunity-playbook.md` | 方法论长文（人读） |
| `reports/METHOD-AND-RESULTS.md` | 摸索史 + 一次实跑 |
| `reports/directions/*` | 历史方向深研包 |
| **`loop/`** | **可调度的固定系统** |

方法正文不重复维护两份：改阈值只改 `config.json`；改 agent 行为只改 `AGENT_PROMPT.md`。

## 硬门槛（写死）

- demand ≥ 3 且 competition ≤ 3 → 纯 **GO**  
- competition=4 仅允许 **GO_NARROW**（必须写清 wedge）  
- **每次 Stage B 必须输出 3–5 个可选方向**（`config.json`: min 3 / target 5）  
- 14 天 solo MVP · 30 天营销 ≤ $300  
- 连续 14 天 0 付费意向或竞争升到 5 → KILL  

## 定时

见 **`SCHEDULE.md`**（cron 示例已写好）。

## 本轮完整结果示例

```
loop/runs/2026-07-19_161905/
├── SELECTABLES.md          ← 5 选一入口
├── VERDICT.md
└── directions/             ← 5 个完整包（PRD+14d+30d）
```
