# Opportunity Loop (fixed method → schedulable)

TrustMRR × competition × X 验证 的**固定流水线**。  
你只需要挂定时任务跑 `run.sh`；需要深度判断时再跑 Agent 阶段。

```
loop/
├── README.md              ← 本文件
├── SCHEDULE.md            ← cron / launchd / GitHub Actions / Claude /loop
├── config.json            ← 阈值与关键词（唯一策略旋钮）
├── pipeline.py            ← Stage A：拉 TrustMRR + 粗筛 + 聚类 + 报告
├── starterstory.py        ← Stage A Track B：Starter Story 灵感池（独立轨道）
├── run.sh                 ← 调度入口
├── AGENT_PROMPT.md        ← Stage B：X 验证 + GO 方向完整包
├── templates/
│   └── direction.md       ← GO 方向输出模板（PRD+14d+30d）
├── cache/starterstory/    ← 详情页缓存（14 天）
├── state/
│   └── last_run.json      ← 上次运行指针（pipeline 自动写）
└── runs/
    └── YYYY-MM-DD_HHMMSS/ ← 每次运行只增不改
        ├── trustmrr_raw.json
        ├── filtered.json          ← 只含 TrustMRR（Track B 不混入）
        ├── candidates.csv         ← 只含 TrustMRR
        ├── starterstory_raw.json  ← Track B 全量原始数据
        ├── starterstory_candidates.csv ← Track B 带收入带的候选
        ├── STARTERSTORY.md        ← Track B 灵感池报告
        ├── handles.csv
        ├── REPORT.md
        ├── VERDICT.md          (agent)
        ├── llm_raw/            ← 每次 LLM 调用的原始返回（调试用，不发布）
        └── directions/*.md     (agent, GO only)
```

## 两条轨道

| | Track A — TrustMRR | Track B — Starter Story |
|---|---|---|
| 数据 | 真实 MRR（已核验） | 研究估算收入（站点自述 "not self-reported"） |
| 用途 | **参与打分**，可产出 GO 方向包 | **仅作灵感/市场背景**，不打分、不产出方向包 |
| 产物 | `filtered.json` · `candidates.csv` · `VERDICT.md` | `STARTERSTORY.md` · `starterstory_candidates.csv` |

Track B 绝**不**并入 Track A 的候选池——估算收入一旦混入打分，一个错数字就能变成 GO_CANDIDATE。
要看 Track B 里的点子，由人工手动提升。

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

或用自动化脚本 `python3 stage_b.py`（CI 走这条）。它把 B2 拆成多次调用：
先出 `VERDICT.md`（可选方向表），再**每个可选方向一次调用**并行生成方向包 ——
一次调用同时要 VERDICT + 5 个完整方向包会超出 provider 的生成时限和 `max_tokens`。

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
