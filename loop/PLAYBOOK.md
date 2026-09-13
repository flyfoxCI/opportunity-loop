# TrustMRR × X 商机挖掘系统（可重复执行）

**目标：** $10K MRR · 2 周 MVP · 30 天营销 ≤ $300  
**原则：** TrustMRR 负责「有人付钱」；X 负责「有人抱怨、有人在找、竞争有多挤」  
**日期：** 2026-07-19  

> 这不是再挑一个静态方向清单，而是一套你每周可跑的流水线。  
> VibeCheck 只是这套流水线的**一个输出示例**，不是唯一答案。

---

## 总览：6 步流水线

```
1 TrustMRR 粗筛（付费验证）
    ↓
2 竞品与竞争强度过滤（桌面 + 上市产品）
    ↓
3 X 需求验证（抱怨 / 求推荐 / 付费意愿）
    ↓
4 提取 X 用户 ID（获客名单）
    ↓
5 PRD + 2 周 MVP 切片
    ↓
6 30 天 ≤$300 营销执行
```

每一步都有**硬门槛**。过不了就 kill，不要硬做。

---

# 步骤 1：怎么在 TrustMRR 里筛方向 / 产品

## 1.1 数据源（按优先级）

| 源 | URL | 用途 |
|---|---|---|
| 公开 AI 快照 | `https://trustmrr.com/api/ai` | recentlyListed + bestDeals（无需登录） |
| Markdown 详情 | `https://trustmrr.com/startup/{slug}.md` | 验证 MRR、subs、定价、渠道、tech |
| 分类页 | `/category/{ai,saas,...}` | 找同类簇（cluster） |
| 最近上架 | `/recent` | 新鲜信号 / 早期赛道 |
| 统计 | `/stats` | 哪些分类增长快 |

**规则：** listing 自描述 = **不可信**。只信：Stripe/Superwall/RevenueCat 验证的 revenue、MRR、activeSubscriptions。

## 1.2 粗筛公式（5 分钟/条）

对每条 listing 打勾：

| # | 条件 | 通过标准 | 失败就 kill |
|---|---|---|---|
| A | 付费验证 | 近 30 天 revenue ≥ $200 **或** MRR ≥ $100 **或** activeSubs ≥ 20 | 全是 $0 叙事产品 |
| B | 模式 | 数字产品 / SaaS / 订阅 / 可复制软件 | 纯服务 / 实体 / 强本地运营 |
| C | 复杂度 | 1 人 14 天能做出 **可收费 MVP** | 需硬件/合规/重模型训练 |
| D | 营销可达 | ICP 在 Reddit/X/IndieHackers 可免费触达 | 必须企业 BD 冷启动 |
| E | 天花板 | 理论上 100–500 付费用户 × $20–$100 能到 $10K | 只剩 $5 一次性、无续费 |
| F | 非黑箱 | 有网站/描述/可理解的 value prop | Anonymous + 无网站 + 无描述 |

## 1.3 推荐的 TrustMRR 排序策略

**优先看这些「簇」而非单个产品：**

1. **同一类描述 ≥ 3 个独立产品都有收入** → 需求被验证  
2. **MRR $100–$5K 的小产品** → 大厂通常不屑，solo 有缝  
3. **bestDeals 里 multiple 低 + 仍在增长** → 赛道有流动性  
4. **recent 里连续出现同类** → 新热度（也可能过热，要进步骤 2）

**刻意降权：**

- MRR > $50K 且 VC/大厂进场的类别（当灵感，不当对标复制）  
- Faith AI / AEO / Local SEO / Churn 全栈 → 历史尽调已证明**巨挤**  
- 一次性 App 无续费且 ASO 依赖 → $10K MRR 很难

## 1.4 粗筛输出模板

每条保留一行：

```
Name | slug | MRR | last30 | subs | category | 一句话问题 | 一句话方案 | 是否进步骤2
```

**示例（2026-07-19 TrustMRR /api/ai 快照）：**

| 产品 | MRR(约) | 信号 | 进步骤2? |
|---|---|---|---|
| Sermon Scribe 类 / Faith | 高 | 付费真 | 是 → 步骤2 大概率 kill |
| CancelPause 类 / Churn | 低–中 | 付费真 | 是 → 步骤2 大概率 kill |
| AI security / vibe-code scan 簇 | 中 | TrustMRR+X 双强 | **是，重点** |
| DodgePrint 等小 SaaS | ~$105 | 小而真 | 是，看 X |
| Photta / 产品摄影 AI | 中 | 付费真 | 是 → 步骤2 看拥挤度 |
| 铃声 App 等 | 低–中 | 消费级 | 可选，天花板问题 |

---

# 步骤 2：怎么验证产品 + 调研竞争 + 过滤「有需求但对手不强」

## 2.1 三层竞争地图（必须做）

对每个候选方向，列出：

| 层 | 谁 | 问题 |
|---|---|---|
| L1 直接对手 | 同 one-liner | 定价？用户数？融资？ |
| L2 间接对手 | 大平台里的一个功能 | 是否「够用就行」？ |
| L3 替代方案 | Excel / 手工 / 通用 ChatGPT | 用户现在怎么凑合？ |

**信息源：**

- 官网 pricing  
- G2/Capterra 评论数  
- Google：`"{category} alternatives 2026"`  
- Product Hunt 同类  
- TrustMRR 同 category 前 30  
- X：`"{competitor}" (expensive OR alternative OR switched OR cancel)`

## 2.2 竞争强度打分（1–5，越低越好）

| 分数 | 含义 | 例子 |
|---|---|---|
| 1 | 几乎无专门产品 | 极窄 vertical |
| 2 | 1–3 个小玩家 | 早期 TrustMRR 簇 |
| 3 | 3–8 玩家，无巨头独占 | **Vibe-code security 区间** |
| 4 | 8+ 或有强品牌 $100+/mo | Churn tools |
| 5 | VC 巨头 / 免费巨无霸 | AEO Profound、UptimeRobot 免费 SSL |

**你的门槛：** 只保留 **竞争 ≤ 3**。  
**例外：** 竞争 4 但有**清晰 unbundle**（只做一个大厂捆绑功能 + 10 倍简单 + 1/5 价格）。

## 2.3 需求强度打分（1–5）

| 信号 | 加分 |
|---|---|
| TrustMRR ≥2 个独立产品有收入 | +1 |
| X/Reddit 上周 ≥10 条真实抱怨 | +1 |
| 用户明确说「愿付 / looking for / recommend」 | +1 |
| 监管/平台变更制造新痛（API 涨价、breach） | +1 |
| 痛点频率高（每周都发生） | +1 |

**门槛：** 需求 ≥ 3 且 竞争 ≤ 3。

## 2.4 一票否决

- 需要牌照（医疗诊断、金融托管）且你无资质  
- 获客必须付费且 CAC > 1 个月 ARPU  
- 数据源依赖会随时被封的 scraping 且无 plan B  
- 你无法在 14 天交付「用户愿意付钱的最小闭环」

## 2.5 输出：过滤表

| 方向 | 需求分 | 竞争分 | 14天MVP | $300营销 | 结论 |
|---|---|---|---|---|---|
| AI-built app security | 5 | 3 | 是 | 是 | **GO** |
| Failed payment recovery | 4 | 4–5 | 是 | 是 | WATCH / 差异化难 |
| Faith sermon AI | 5 | 5 | 是 | 是 | NO |
| AEO 全栈 | 5 | 5 | 否 | 否 | NO |

---

# 步骤 3：从 X 找需求并判断（核心优势）

## 3.1 四类可操作的 X 搜索

用 **X advanced search**（工具：`x_keyword_search` / 手工 `from:` `since:`）：

### A. 痛点抱怨（Demand）
```
("Lovable" OR "Bolt.new" OR "vibe coding") (security OR "API key" OR exposed OR RLS OR breach)
("Stripe") ("failed payment" OR dunning) (SaaS) (need OR looking OR painful)
```

### B. 求推荐（Intent）
```
("recommend" OR "looking for" OR "anyone use" OR "alternative to") (tool OR SaaS) {keyword}
```

### C. 竞品吐槽（Gap）
```
("{Competitor}") (expensive OR cancel OR switched OR "too complex" OR "enterprise")
```

### D. 刚发船用户（ICP 名单）
```
("just shipped" OR "built with Lovable" OR "built with Bolt") (app OR SaaS)
```

## 3.2 X 验证判定规则（2026-07 实测示例）

### 示例方向：AI-built app security（TrustMRR 有 securenow / Vibe App Scanner 等）

| X 信号 | 证据 | 判断 |
|---|---|---|
| 大规模恐惧/新闻 | @aakashgupta 等帖：Lovable 相关暴露、旋转密钥讨论，10万+ views | **需求极强** |
| 结构性质问题 | @rentierdigital：200 个 vibe-coded app 中 183 泄漏；Supabase RLS `USING (true)` | **不是个例** |
| 解决方案涌入 | @wraithnet0x 推 mitsumono；@heyjaywilson 用 Greptile；@Maeveshee 谈 broken auth | **市场已启动但仍可切入** |
| 竞品心态 | 多为新工具/扩展，无单一垄断 | **竞争 3，可进** |

### 反例方向：Failed payment / dunning

| X 信号 | 证据 | 判断 |
|---|---|---|
| 建设者多 | @IvanBalias Lirova：「找抱怨的人，找到的竞争者比客户多」 | **痛真实但拥挤** |
| 新工具连发 | RetryFix、Revova、Dunlo、Lirova | **竞争 4–5，solo 难差异化** |

### 反例方向：Faith AI

| X 信号 | 证据 | 判断 |
|---|---|---|
| 有产品 | @luke_netti shepherd_docs 等 | 需求在 |
| 结合桌面尽调 | SermonFlow / Pulpit AI / Sermon Shots… | **竞争过强 → NO** |

## 3.3 每周 60 分钟 X 巡检清单

1. 跑 A/B/C/D 四类 query（各 5 分钟）  
2. 记下：痛点原话、频次、对手名、高互动帖  
3. 更新「需求分 / 竞争分」  
4. 若连续 2 周需求 <3 或 竞争升到 4 → 换方向  

---

# 步骤 4：找出潜在 X 用户 ID（获客资产）

## 4.1 用户类型

| 类型 | 用途 | 怎么找 |
|---|---|---|
| **ICP 买家** | 直接 DM / 免费审计 | just shipped + builder 关键词 |
| **分发节点** | RT / 提及 | buildinpublic 大号、newsletter 作者 |
| **竞品用户** | 挖不满 | 竞品名 + 抱怨 |
| **行业 KOL** | 联名 / 试用 | category + founder |

## 4.2 2026-07 实测：与「AI app 安全 / vibe coding」相关的 X ID

### A. 高意向买家 / 同类建设者（可免费 scan 触达）

| Handle | 为何相关 |
|---|---|
| @Chony1290415 | 「just built with Lovable」发船用户 |
| @wraithnet0x | 推 AI-era security tools，同类受众 |
| @heyjaywilson | vibe coding + Greptile 安全工作流 |
| @Maeveshee | 谈 vibe coding 安全债 |
| @haze_vt | 警告 AI 包安全风险 |
| @celeborncode | 强调 plan 里必须有 security |
| @rentierdigital | 发 vibe-coded 泄漏数据，强痛点内容 |
| @paulhartnessuk / @RetryFix | Stripe recovery 建设者（邻域，非主 ICP） |
| @IvanBalias | 失败支付建设者，懂「竞争验证需求」叙事 |
| @shipordie_ | ship 社区，船员刚发船 |

### B. 分发 / 放大节点

| Handle | 为何相关 |
|---|---|
| @aakashgupta | 高浏览安全/Lovable 讨论 |
| @ohryansbelt | Lovable 漏洞拆解，高传播 |
| @weezerOSINT | 漏洞细节传播 |
| @marclou | TrustMRR 生态 / indie 受众（分发） |
| @JulianGoldieSEO | AI 工具传播力强 |
| @levelsio | （查询时可用）indie 分发标杆 |

### C. 名单运营方式（≤$300 营销）

1. **表：** `handle | 类型 | 最近帖链接 | 痛点原话 | 触达状态 | 结果`  
2. **每日 10 个** 高质量回复（先帮后推，禁止硬广）  
3. **每周 20 个** 个性化 DM：「免费帮你扫一次 Lovable URL」  
4. **不买粉、不买量** — 预算留给域名/托管/API  

## 4.3 持续扩展 ID 的查询

```
("built with" OR "shipped with") (Lovable OR Bolt OR "v0" OR Cursor) since:2026-06-01
"security" (Lovable OR "vibe coded" OR Supabase) (exposed OR leak OR RLS)
"looking for" (tool OR SaaS) (security OR scanner OR "API key")
```

保存每次搜索的 author handle → 写入 CRM（Notion/表格即可）。

---

# 步骤 5：构建 PRD 与 MVP（模板 + VibeCheck 实例）

## 5.1 PRD 最小结构（任何方向通用）

1. **One-liner**  
2. **ICP + 付费场景**（一句话何时掏钱）  
3. **Jobs-to-be-done**  
4. **P0 / P1 / P2**（P0 = 14 天内能收费）  
5. **非目标**（防止膨胀）  
6. **成功指标**（Day 14 / Day 30）  
7. **技术切片**（1 栈，不搞微服务）  
8. **定价草案**  

## 5.2 14 天 MVP 时间盒

| 天 | 产出 |
|---|---|
| 1–2 | Landing + 支付/邮箱捕获 + 假数据演示 |
| 3–7 | 核心闭环（输入 → 结果 → 可分享） |
| 8–10 | 计费 + 账户（可先 Lemon/Stripe 链接） |
| 11–12 | 5 个真实用户试用修复 |
| 13–14 | 公开上线材料 + 发布 |

## 5.3 实例：VibeCheck（流水线输出之一）

**已完成：**

- PRD：`vibecheck/vibecheck/PRD.md`  
- 代码 MVP：`vibecheck/vibecheck/`（扫描引擎 + AI 解释 + Landing + Stripe/Clerk 脚手架）  
- 上线文案：`vibecheck/vibecheck/LAUNCH.md`  

**P0 功能：** URL 扫描 → 漏洞列表 → 人话解释 + 修复步骤 → 免费/付费分层  

**非目标：** 企业渗透测试、取代 Snyk 全栈、合规认证  

**Day 30 指标建议：** 500 signup / 30 付费意向 / 10 付费  

---

# 步骤 6：30 天非常具体的营销计划（≤$300）

## 6.1 预算（任何 organic-first 方向通用）

| 项 | 金额 |
|---|---|
| 域名 | $12–15 |
| Vercel / 托管 | $0–20 |
| 邮件 / Resend | $0–20 |
| LLM API | $20–40 |
| Product Hunt 可选 boost | $0–50 |
| 备用 | 其余 → **总计 ≤ $300** |

## 6.2 周历（以 VibeCheck / 同类为例，可替换关键词）

### Week 1：上线与名单启动（$0–80）

| 日 | 动作 | 完成定义 |
|---|---|---|
| D1 | PH + IH 发帖（用 LAUNCH 文案） | 帖出 + 置顶回复 |
| D2 | X thread（12 条模板） | 发完 + 钉选 |
| D3 | Reddit：r/lovable、r/SideProject（遵守版规） | 2 帖 + 回评 |
| D4 | 回复 20 条「just shipped Lovable/Bolt」 | 表更新 20 行 |
| D5 | DM 15 个 ICP：免费扫描 | 发出 15 |
| D6 | 发布 1 篇 SEO：「Lovable API key exposed」 | 上线 |
| D7 | 复盘：扫描次数、注册、回复率 | 周记 |

### Week 2：证据与案例（$20–40 API）

| 日 | 动作 |
|---|---|
| D8–9 | 汇总匿名扫描统计（%）发 thread |
| D10 | 1 个 YouTube/Loom 演示 5 分钟 |
| D11–12 | 再触达 30 个 X ID |
| D13–14 | 根据反馈改 P0 文案 / 误报 |

### Week 3：分发节点（$0）

| 日 | 动作 |
|---|---|
| D15–17 | 给 @aakashgupta 类内容做「补充工具」评论，不硬广 |
| D18–19 | 找 5 个 newsletter 投稿 pitch |
| D20–21 | Affiliate 30% 页（若有付费） |

### Week 4：转化（$0–50）

| 日 | 动作 |
|---|---|
| D22–24 | Founding price（限 50 席）邮件/X |
| D25–27 | 未转化用户 1:1 问「缺什么才付」 |
| D28–30 | 月报 + 下月方向是否仍满足「需求≥3 竞争≤3」 |

## 6.3 每日固定节奏（45–90 分钟）

1. 10 分钟：X 搜 A/B 类 query，记 5 个新 handle  
2. 20 分钟：有价值回复 5–10 条  
3. 15 分钟：产品改进 1 个误报/文案  
4. 10 分钟：更新 CRM  

---

# 把方法固化成「周会模板」

每周日 30 分钟：

```
1. 本周 TrustMRR 新 listing 里出现的新簇？
2. 本周 X 上抱怨最多的关键词 top3？
3. 当前主方向：需求分 / 竞争分？
4. 是否仍 ≤14 天可交付？
5. 获客名单净增多少 handle？
6. 付费 / 试用转化？
7. GO / PIVOT / KILL
```

**KILL 规则：** 连续 14 天 0 付费意向 + 竞争升到 4 → 立刻换簇，不沉没成本。

---

# 示范：本周用流水线跑出的结论（2026-07-19）

| 步骤 | 结果 |
|---|---|
| 1 TrustMRR | 多簇有验证收入；Faith/Churn/AEO 历史强；AI security 簇有早期收入工具 |
| 2 竞争 | Faith/AEO/Churn → 强；Failed payment → X 上建设者挤；**Vibe-code security → 中等** |
| 3 X 需求 | Lovable/vibe coding 安全帖高互动；结构性 RLS/密钥问题被反复验证 |
| 4 用户 ID | 见步骤 4 表（@Chony1290415、@rentierdigital、@Maeveshee…） |
| 5 PRD/MVP | VibeCheck 已落地为可执行实例 |
| 6 30 天营销 | LAUNCH.md + 本节周历 |

**因此：方法优先于单一产品。** 若 VibeCheck 两周后 X 信号变弱或巨头免费送同能力，用同一流水线换下一个「需求≥3 竞争≤3」的簇。

---

# 你每周实际要做的最小动作清单

1. 打开 `trustmrr.com/api/ai` + 2 个 category  
2. 选出 5 条过粗筛的 listing  
3. 对每条做 15 分钟竞品搜索 → 填竞争分  
4. 对幸存 1–2 条跑 X 四类搜索 → 填需求分 + 20 个 handle  
5. 只对 **双门槛通过** 的方向写 1 页 PRD  
6. 14 天只做一个 P0  
7. 30 天严格 ≤$300，按日表执行  

---

# 相关文件

| 文件 | 内容 |
|---|---|
| `reports/trustmrr-direction-report-v1.md` | 初筛大清单 |
| `reports/trustmrr-direction-report-v2.md` | 第一轮竞品纠正 |
| `reports/directions/v3-due-diligence-synthesis.md` | 深度淘汰 |
| `reports/directions/01–06-*.md` | 六方向深研包（方法训练素材） |
| `vibecheck/vibecheck/` | 方法的一个完整落地产物 |
| **本文件** | **可重复的商机系统** |

---

## 一句话

> **TrustMRR 证明「有人付过钱」；X 证明「现在还有人疼、对手有多吵、该 DM 谁」；两者交叉过滤后，才写 PRD、做 14 天 MVP、用 $300 打 30 天有机获客。**
