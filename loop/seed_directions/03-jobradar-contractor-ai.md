# Direction 03 — JobRadar: Contractor 行业 AI Lead Generation

**推荐等级:** 🥉 #3 (Confidence 8/10)
**代币代号:** JobRadar (or trade-specific name)
**目标 MRR:** $10,000/月 (60-90 天可达)
**MVP 上线时间:** 14 天
**营销预算:** $300/30 天

---

## 第一部分:深度调研报告

### 1.1 市场验证证据

#### 关键信号 — NextjobConnect
- **来源:** trustmrr.com/startup/nextjobconnect-llc
- **验证 MRR:** $240/月 (Stripe) — 但 founder 自描述 $5K MRR
- **30 天营收:** $6,556 (验证)
- **付费客户数:** 22 (验证)
- **累计营收:** $115K (估算)
- **定价:** $79-$500/月
- **毛利:** 75%
- **Customer acquisition:** Outbound sales (高 LTV)
- **Tech:** React Native + FastAPI + Stripe
- **ICP:** "Real-time job leads for home service contractors"
- **数据源:** Neighborhood platforms (Nextdoor, Craigslist, Facebook Marketplace)
- **AI:** AI classifies posts by trade
- **交付渠道:** iOS/Android app + SMS
- **Asking Price:** $100K-$200K
- **Listed:** 在售

#### 为什么这是黄金信号
- **22 付费客户 × $240 平均 = $5K MRR** — 已验证付费意愿
- **outbound sales 模式** — B2B 高 LTV
- **75% gross margins** — 健康单位经济
- **真实痛点** — 找本地客户是 contractors 的核心问题
- **数据源稳定** — Nextdoor / Craigslist / Facebook Marketplace 有大量 posts

### 1.2 竞品尽调

#### Contractor AI 玩家(我深入研究)
从 contractor-toolstack.com 等专业评测,我发现:

| 玩家 | 状态 | 模式 | 客户数估计 |
|---|---|---|---|
| **Alivo** | AI worker matching | 平台模式,双向 | 中(估计 100-500) |
| **RoofClaw** | AI roofing sales | 极 vertical(只 roofing) | 早期 |
| **Avoca AI** | AI leads | 综合 lead gen | 中 |
| **Hatch** | AI sales agent | 外呼 AI | 中 |
| **GoHighLevel AI Employee** | 大平台 + AI | 已有 100K+ 用户 | 大(但 AI 功能是附加) |
| **Jobber** | 老牌 field service | 不专门做 AI,但有 AI features | 大(VC) |
| **ServiceTitan** | 老牌(enterprise) | 大公司,中大型 contractor | 巨大(IPO) |
| **Housecall Pro** | 老牌 home service SaaS | 类似的 | 巨大(VC) |

#### 对 solo founder 的机会
- **ServiceTitan / Housecall Pro / Jobber** 是 VC-funded 大玩家,但价格高($100-$500+/mo),目标中大型 contractor
- **小 contractor**(独立 plumber、electrician)被忽略 — 但他们数量最多
- **Alivo / RoofClaw / Hatch** 还在早期,玩家之间市场细分尚未明确
- **Niche trade 细分** 完全无人做(例如:chimney sweep、piano tuner、pest control、appliance repair)

#### 我深入验证的真实竞品缺口
- **专门做 "lead gen for specific niche trades"** 的玩家**几乎没有**
- 每个"AI contractor tool"都太宽泛,没有深度
- **Solo founder 优势**:快速 vertical 化,选一个 niche trade,做深

### 1.3 目标 Vertical 细分选择

我评估的 trades:

| Trade | 美国市场大小 | Tech 采纳 | 痛点强度 | WTP | 竞争 |
|---|---|---|---|---|---|
| HVAC | 大 | 中 | 高(emergency) | 高 | 中 |
| Plumber | 大 | 低 | 高(emergency) | 高 | 中 |
| Electrician | 大 | 低 | 中 | 高 | 低 |
| Roofer | 中 | 低 | 中(季节性) | 高 | 中 |
| Pest control | 中 | 低 | 中 | 中 | 低 |
| Appliance repair | 小 | 极低 | 高(客户找不到) | 中 | **极低** |
| Chimney sweep | 极小 | 极低 | 低 | 中 | **零** |
| Piano tuner | 极小 | 极低 | 低 | 低 | **零** |
| Garage door | 小 | 极低 | 中(紧急) | 中 | 低 |
| Pool service | 小 | 低 | 中 | 中 | 低 |
| Septic service | 极小 | 极低 | 高(紧急) | 中 | **零** |
| Gutter cleaning | 小 | 极低 | 中 | 低 | 低 |
| Window cleaning | 小 | 极低 | 低 | 低 | 低 |
| Carpet cleaning | 小 | 低 | 中 | 中 | 低 |

#### 我的推荐:选 3 个 trades 启动

**推荐组合(每个 trade 都是真实 niche):**

**组合 A — "高频率 emergency trades"**
- HVAC(夏季 emergency)、Plumber(紧急 leak)、Electrician(紧急)
- 这三个是 demand 最稳定的
- Nextdoor 上每天有 100+ emergency posts

**组合 B — "被忽略的 niche trades"**
- Septic service(紧急,pump 需求)
- Garage door repair(紧急,客户被锁外面)
- Appliance repair(refrigerator、washer 坏了)

**组合 C — "季节性 high-ticket"**
- Roofer(冰雹后大批需求)
- Gutter(秋季)
- Chimney(冬季)

**我推荐:组合 A 的 HVAC + Plumber + Electrician**(启动)→ 拓展到组合 B

### 1.4 市场规模

#### TAM
- 美国 home service contractors:**300 万+**(包括 HVAC、plumber、electrician、roofer、pest control 等)
- 中型 contractor(年收入 $100K-$500K):约 100 万
- 平均每年 lead gen 花费:**$5K-$20K**
- **TAM = $5B-$20B/年**

#### SAM
- 美国愿意付费 AI lead gen 的 contractors:**50K-200K**
- @ $200/mo 平均 = **$10M-$40M/年**

#### SOM
- 第一年目标:**50-100 付费 contractor**
- @ $200/mo 平均 = **$10K-$20K MRR**

### 1.5 目标用户画像

#### Primary ICP — "Mike the Plumber"
- 角色:独立 plumber 或 5 人 plumbing 公司
- 收入:$100K-$500K/年
- 痛点:
  - 找新客户是 #1 难题
  - 投 Yelp / Angi 每月 $500-$2000 但 ROI 不稳定
  - Google Ads 越来越贵($20-$50/lead)
  - 想找"现在就需要 plumber" 的客户
- 决策时间:个人决策,1-2 周
- WTP:$79-$299/mo(每月 1-3 个 lead 就能 cover)
- 触达:
  - LinkedIn(plumbing business owner)
  - 本地 contractor Facebook groups
  - Plumbing trade shows
  - Outbound(冷邮件 + 冷电话)
  - YouTube(plumbing business channels)

#### Secondary ICP — "Maria the HVAC Dispatcher"
- 角色:HVAC 公司 dispatcher / office manager
- 决策比 individual plumber 慢,但 LTV 高
- WTP:$299-$500/mo

### 1.6 关键数据源(Tier 1)

#### Nextdoor
- 美国 80M+ MAU
- 大量 "ISO plumber" / "Need HVAC repair" posts
- 没有公开 API,**需要 scraping**
- TOS 灰色地带(小心)

#### Craigslist
- 美国最老 classifieds
- "Services Wanted" 部分大量 contractor posts
- 有官方 API(部分功能)
- 风控相对松

#### Facebook Marketplace
- 大流量
- "Service wanted" 部分有 contractor 需求
- 无公开 API,需要 scraping

#### Google Search Results
- "emergency plumber [city]" — 找广告密度低但有需求的位置
- 可以监控的搜索结果

#### Local subreddit
- r/[cityname] 经常有 "looking for plumber" posts
- 公开 API,免费

#### Homeowner apps
- Angi (前 HomeAdvisor),Thumbtack,Yelp
- 已经是市场,但 contractors 抱怨 lead quality 差 + 平台抽成高

**我的策略:** 选 **Nextdoor + Craigslist + Local Reddit** 起步(免费 + scraping 可行)

### 1.7 风险评估

| 风险 | 概率 | 影响 | 缓解 |
|---|---|---|---|
| Nextdoor TOS 风险 | 中 | 中 | 用代理 + 限速 + 不直接登录 user account |
| Craigslist 风控 | 中 | 中 | 限速 + IP rotation |
| AI 分类准确率低 | 中 | 高 | 用 Claude Opus 提高精度 + 后台人工 review |
| 销售周期长(contractor 慢) | 高 | 中 | Free trial 14 天 + 提供 lead sample |
| 大玩家进入(GoHighLevel 等) | 中 | 高 | 选 vertical 他们不做的 niche trade |
| 数据源平台变化 | 中 | 高 | 多数据源 backup + 不依赖单一平台 |

---

## 第二部分:PRD(产品需求文档)

### 2.1 产品定义

**One-liner:**
> "Plumbers / HVAC techs / electricians 可以在 24 小时内收到本地客户的实时 lead(从 Nextdoor / Craigslist / Reddit),只付给真实 lead,无需每月固定费。"

**Tagline:** "Real-time leads for home service pros — pay only when we deliver."

### 2.2 核心使用流程

#### Contractor 视角
1. 注册账户
2. 选 trade(HVAC / Plumber / Electrician)
3. 选服务区域(zip codes)
4. 设置 lead filter:
   - Urgency level(high / medium / low)
   - Budget range(if mentioned)
   - Property type(residential / commercial)
5. 设置通知渠道(SMS / Email / App push)
6. 收到 lead → click "Interested" → 获得 customer contact
7. (可选)Pay per lead OR pay monthly subscription

#### 启动阶段(MVP)
- 选 **HVAC + Plumber + Electrician** 三个 trades
- 选 **3-5 个 pilot cities**(高 lead 量)
- 3 个 lead delivery channels:SMS (Twilio) + Email + Web dashboard

### 2.3 用户故事(Epic)

#### Epic 1:Contractor onboarding(Day 14)
**US-1.1:** 作为 contractor,我可以注册(邮箱 / Google OAuth)
**US-1.2:** 作为 contractor,我可以选 trade + 服务区域
**US-1.3:** 作为 contractor,我可以设置 lead filter
**US-1.4:** 作为 contractor,我可以选通知渠道
**US-1.5:** 作为 contractor,我可以试用 7 天免费

#### Epic 2:Lead delivery(Day 14)
**US-2.1:** 作为 system,我可以 scraping Nextdoor / Craigslist / Reddit 每小时
**US-2.2:** 作为 system,我可以用 Claude 分类 posts(high / medium / low urgency)
**US-2.3:** 作为 system,我可以在新 lead 匹配 contractor 时 push notification
**US-2.4:** 作为 contractor,我可以在 dashboard 看到所有 leads
**US-2.5:** 作为 contractor,我可以 click "Interested" 看 customer 联系方式
**US-2.6:** 作为 system,我可以 track lead → customer outcome

#### Epic 3:Billing(Day 14)
**US-3.1:** 作为 contractor,我可以选 plan:
  - Starter: $79/mo,最多 30 leads/月
  - Pro: $199/mo,最多 100 leads/月
  - Scale: $499/mo,无限 leads
**US-3.2:** 作为 system,我可以自动超量警告

#### Epic 4:Advanced(Day 30+)
**US-4.1:** 作为 contractor,我可以查看 lead analytics(转化率、ROI)
**US-4.2:** 作为 contractor,我可以暂停 lead delivery(vacation)
**US-4.3:** 作为 contractor,我可以加 zip codes

### 2.4 显式功能范围

#### P0 (MUST - Day 14)
- Contractor 注册 + onboarding
- Trade 选择(HVAC / Plumber / Electrician)
- Service area(zip codes,最多 5)
- Lead filter(urgency, budget)
- 数据 scraping(Nextdoor + Craigslist + Reddit)
- AI 分类(Claude)
- Lead delivery:SMS + Email + Web dashboard
- Subscription:Stripe Checkout
- 基础 admin 后台

#### P1 (SHOULD - Day 21)
- Lead 评分(0-100 score)
- Customer 联系方式 reveal
- Lead analytics(转化率)
- Multi-user(给 office manager)

#### P2 (NICE - Day 30+)
- Mobile native app(react native)
- Zapier 集成
- Auto-response to leads
- CRM 集成(Jobber / Housecall Pro)

#### OUT OF SCOPE (MVP 不做)
- 自己联系 leads(AI outbound)
- 服务工单管理
- 支付处理给客户
- 调度工具

### 2.5 技术架构

#### Stack
| Layer | 技术 | 理由 |
|---|---|---|
| Frontend | Next.js 15 | 模板成熟 |
| UI | Tailwind + shadcn/ui | 现代 |
| Backend | FastAPI (Python) | 同 NextjobConnect |
| Database | PostgreSQL (Supabase) | 主数据 |
| Scraping | Playwright / Selenium | Nextdoor / Craigslist |
| Scraping Scheduler | Cron + BullMQ | 每小时 |
| AI Classification | Claude Sonnet | lead 分类 |
| SMS | Twilio | lead delivery |
| Email | Resend | notification |
| Push (P2) | Firebase | app push |
| Payment | Stripe | Subscription |
| Hosting | Railway (backend) + Vercel (frontend) | 简单 |

#### 数据流
```
[每小时 Cron Job]
   ↓
[Playwright scraping: Nextdoor / Craigslist / Reddit]
   ↓
[Store raw posts in DB]
   ↓
[Claude API: classify (trade, urgency, budget, location)]
   ↓
[Match against contractor preferences]
   ↓
[If match → push to contractor]
   ↓
[Contractor clicks Interested → reveal customer contact]
   ↓
[Track outcome (sold / no-sold / pending)]
```

#### 数据模型
```python
# Simplified for clarity

class Contractor:
    id: str
    email: str
    name: str
    company_name: str
    trades: List[str]  # ["hvac", "plumber", "electrician"]
    zip_codes: List[str]  # service areas
    plan: str  # starter / pro / scale
    stripe_customer_id: str
    stripe_sub_id: str
    monthly_lead_count: int
    notification_channels: List[str]  # ["sms", "email"]
    created_at: datetime

class RawPost:
    id: str
    source: str  # nextdoor / craigslist / reddit
    source_url: str
    source_id: str  # external ID
    title: str
    content: str
    posted_at: datetime
    location: str
    scraped_at: datetime
    status: str  # new / classified / matched / archived

class ClassifiedLead:
    id: str
    raw_post_id: str
    trade: str  # detected
    urgency: str  # high / medium / low
    budget_mentioned: str | None
    property_type: str  # residential / commercial
    confidence_score: float  # 0-1
    customer_email: str | None  # if available
    customer_phone: str | None  # if available
    location: str
    classified_at: datetime

class LeadDelivery:
    id: str
    classified_lead_id: str
    contractor_id: str
    delivered_at: datetime
    channel: str  # sms / email / push
    status: str  # delivered / opened / clicked / ignored

class LeadOutcome:
    id: str
    delivery_id: str
    outcome: str  # contacted / quoted / won / lost / ignored
    revenue_cents: int | None
    noted_at: datetime
```

#### AI Classification Prompt
```
You are classifying a home service lead post for routing to 
relevant contractors.

Given a post from Nextdoor / Craigslist / Reddit:

1. Determine the trade needed:
   - hvac / plumber / electrician / roofer / pest_control / 
     appliance_repair / garage_door / other
2. Determine urgency: high / medium / low
   - "leaking now", "no AC", "locked out" → high
   - "thinking about", "planning" → low
3. Extract budget if mentioned
4. Extract location (city, zip)
5. Extract contact info (email, phone) if present
6. Score confidence (0-1)

Return strict JSON:
{
  "trade": "...",
  "urgency": "...",
  "budget": "...",
  "location": "...",
  "contact": {"email": "...", "phone": "..."},
  "confidence": 0.95
}

Post:
{POST_TITLE}
{POST_CONTENT}
```

### 2.6 定价

| Plan | 价格 | Lead 限制 | 目标 |
|---|---|---|---|
| Starter | $79/mo | 30 leads/月 | 独立 contractor |
| **Pro** | **$199/mo** | 100 leads/月 | 小公司 |
| Scale | $499/mo | 无限 | 中型公司 |

#### Unit Economics

**Pro 客户 (@$199):**
- 收入:$199
- Stripe 抽成:$6.07
- 边际成本(Twilio SMS + Claude API + scraping infra):~$5-$15/客户
- **毛利:$180-$190/客户/月 (90% margin) ✓**

**50 Pro 客户 = $10K MRR ✓**
**25 Pro + 30 Starter = $7.4K MRR**

### 2.7 关键 SLA

- Lead scraping latency:< 1 hour from post to lead delivery
- AI classification accuracy:> 90% on trade, > 80% on urgency
- SMS delivery latency:< 5 seconds
- Notification uptime:99.5%

---

## 第三部分:30 天营销计划(预算 $300)

### 3.1 预算分配

| 项目 | 金额 | 用途 |
|---|---|---|
| 域名 | $12 | jobradar.so / hvacradar.app / prowin.app |
| Vercel Pro | $20 | 前端 |
| Railway | $20 | FastAPI 后端 |
| Supabase Pro | $25 | DB |
| Twilio (SMS) | $20 | lead delivery |
| Resend | $20 | 邮件 |
| ProductHunt boost | $50 | 启动日 |
| 数据采集(代理 IP) | $30 | scraping 必要 |
| Reserve | $103 | 应急 |
| **总计** | **$300** |  |

### 3.2 30 天日历(逐日)

#### Week 1:Day 1-7 — 上线 + 内测

**Day 1 (上线日)**
- ProductHunt 发布:"JobRadar — Real-time home service leads, pay only when we deliver"
- IndieHackers "Show IH"
- X thread:"I built a lead gen tool for plumbers/HVAC/electricians — here's the data"
- 在 r/Plumbing, r/HVAC, r/electricians 发文(每个 subreddit 都不同角度)
- LinkedIn 文章:"Why I'm building for blue-collar pros"

**Day 2-3: 内容准备**
- 3 篇 SEO 文章:
  1. "Best Lead Generation for Plumbers in 2026"(重点关键词)
  2. "How HVAC Companies Get 10+ New Leads per Month Without Yelp"
  3. "AI for Home Service Businesses: The 2026 Playbook"
- Medium, LinkedIn, dev.to

**Day 4-5: Outbound 启动**
- 收集 200 个 contractor email(LinkedIn, Yelp, HomeAdvisor)
- 用 Instantly / Lemlist 发 50 封 cold email / 天
- 跟踪 open / reply rate

**Day 6-7: 第一批客户**
- 给 50 个 interested leads 提供"7 天免费试用 + 我们提供 10 个 lead"
- LinkedIn 私信 20 个 contractor 影响者
- r/Plumbing 发 1 条 "我做了这个工具,免费给前 30 个用户"

**Week 1 KPI:**
- 30 signups
- 5 付费客户 = **$400-$1K MRR**

#### Week 2:Day 8-14 — 案例 + Outbound 加速

**Day 8-9: 客户故事**
- "Case Study: How Plumber Bob Got 8 Leads in Week 1"
- "Case Study: HVAC Company Doubled Bookings"

**Day 10-11: 视频内容**
- YouTube:"I Built a Lead Gen Tool for Plumbers — Demo"
- X 视频:demo

**Day 12-14: 渠道扩张**
- 在 5 个 contractor Facebook groups 发文(Plumbing Pros, HVAC Techs, etc.)
- LinkedIn 文章:"From 0 leads to 50 leads/month — How AI changes contractor marketing"
- 申请 podcast:Service Business Mastery, Contractor Secrets

**Week 2 KPI:**
- 60 signups
- 15 付费客户 = **$2K-$3K MRR**

#### Week 3:Day 15-21 — 规模化

**Day 15-17: 合作伙伴**
- 联系 5 个 contractor 影响者(plumber YouTuber 等)
- 提供 affiliate 30% 终身佣金
- 联系 plumbing trade shows / HVAC 协会

**Day 18-21: 第二轮内容**
- 5 条 X thread
- 5 篇 LinkedIn 文章
- 1 个 lead gen 报告:"State of Home Service Lead Gen 2026"

**Week 3 KPI:**
- 100 signups
- 25 付费客户 = **$4K-$5K MRR**

#### Week 4:Day 22-30 — 收网 + 优化

**Day 22-24: 转化优化**
- Free trial → paid 转化漏斗优化
- Email 序列(nurture)
- Customer success outreach

**Day 25-27: 案例 + 紧迫感**
- "30-day review" 内容
- "Founding Pros Pricing" - 前 50 客户终身 30% off

**Day 28-30: 收网**
- 50 trial 用户 personal outreach
- 在 X 跑 "Free Audit" - 你帮 5 个 contractor 看他们的 lead gen

**Week 4 KPI:**
- 150 signups
- 40 付费客户 = **$6K-$8K MRR**

### 3.3 30 → 90 天路径

| Day | 目标 | 行动 |
|---|---|---|
| Day 30 | $6K MRR | 40 客户 |
| Day 60 | $8K MRR | + 加 trades(pest control、roofer)+ 拓展到 10 cities |
| Day 90 | **$10K MRR** ✓ | 50 客户 × $200 平均 |

---

## 第四部分:执行指南(Day-by-Day)

### 4.1 14 天冲刺计划

#### Day 1-2:基础 + 数据源 PoC
- [ ] 注册域名(选:jobradar.so, leadsforhvac.com, win.app)
- [ ] Next.js + FastAPI 双项目设置
- [ ] Stripe + Twilio + Resend accounts
- [ ] **PoC:Nextdoor scraping 1 个城市 24 小时**(验证可行性)

**Day 1-2 交付物:** 数据流基本跑通

#### Day 3-5:Scraping + AI Classification
- [ ] Playwright scraping 完整 pipeline
- [ ] Nextdoor / Craigslist / Reddit 三源
- [ ] Claude classification API
- [ ] Cron job 每小时运行
- [ ] DB schema 设计

**Day 3-5 交付物:** 系统每小时抓取 + 分类 posts

#### Day 6-8:Contractor Dashboard + Matching
- [ ] Contractor 注册 / onboarding
- [ ] Trade 选择 + zip code 输入
- [ ] Lead filter 设置
- [ ] Lead matching algorithm
- [ ] Contractor dashboard(看到 leads)

**Day 6-8 交付物:** Contractor 可以注册并看到 leads

#### Day 9-10:SMS + Email Delivery
- [ ] Twilio SMS integration
- [ ] Email notification (Resend)
- [ ] Lead reveal mechanism(click → see customer contact)

**Day 9-10 交付物:** Contractor 收到 leads via SMS + Email

#### Day 11-12:Subscription + Stripe
- [ ] Stripe Checkout
- [ ] Subscription webhooks
- [ ] Lead quota tracking
- [ ] 超量警告

**Day 11-12 交付物:** 完整订阅系统

#### Day 13:QA + 内测
- [ ] 3 个真实 contractor 内测
- [ ] Lead quality 检查
- [ ] 修复 bug
- [ ] 文档

**Day 13 交付物:** 生产就绪

#### Day 14:公开上线
- [ ] ProductHunt
- [ ] IndieHackers
- [ ] X thread
- [ ] Reddit (3 个 trades subreddit)
- [ ] Cold email blast

**Day 14 交付物:** 公开上线

### 4.2 完整技术栈(实际成本)

| 服务 | 月成本(初期) | 月成本(50 客户) |
|---|---|---|
| Vercel | $20 | $20 + 超额 |
| Railway (FastAPI) | $20 | $50 (5GB RAM) |
| Supabase | $25 | $25 + 超额 |
| Twilio SMS | $20 (200 SMS) | $100 (1000 SMS) |
| Resend | $20 | $20 |
| OpenAI / Claude API | $20 | $50 |
| 代理 IP (scraping) | $30 | $50 |
| Stripe 抽成 | 2.9% + 30¢ | ~$290 |
| **小计** | **~$175 + Stripe** | **~$315 + Stripe** |

**单位经济(Pro @ $199):**
- 收入:$199
- Stripe 抽成:$6.07
- 边际成本(Twilio + Claude + scraping):~$10-$15/客户
- **毛利:$180-$185/客户/月 (90% margin) ✓**

### 4.3 关键销售流程

因为 contractor 不像 SaaS 用户,他们更保守,**销售周期 1-2 周**。

#### Cold Email 模板
```
Subject: Quick question about your [trade] business

Hi [Name],

I noticed your [trade] company serves the [City] area.

I'm building a tool that surfaces real-time leads from 
Nextdoor/Craigslist/Reddit for [trade] pros — basically 
people posting "Need [trade] ASAP" right now.

Would you be interested in seeing 10 sample leads for 
your service area (free, no commitment)?

If yes, I'll send them over this week.

Best,
[Your name]
```

#### Trial Conversion Strategy
- 7 天免费试用 + 10 个 lead sample
- Day 3:Personal email "How are the leads?"
- Day 6:Call "Want to upgrade? 50% off first month"

### 4.4 数据合规

#### Nextdoor TOS 风险
- Nextdoor 不允许 scraping(TOS)
- **风险:Nextdoor 可能 IP ban / 律师函**
- **缓解:**
  - 用 residential proxy IP
  - 限速(每 30 分钟 1 个)
  - 不登录 user account(只看公开 posts)
  - 准备好 fallback 数据源

#### 隐私 / 合规
- 公开 posts 是公开信息
- 但 contractor 用 lead contact 信息做 cold outreach 可能违反一些平台规则
- **明确告知 contractor:这是公开信息,但用 contact info 时需合规**

---

## 第五部分:风险与缓解(详细)

| 风险 | 概率 | 影响 | 缓解 |
|---|---|---|---|
| Nextdoor 检测 scraping → ban | 中 | 高 | 限速 + residential proxy + 多账户轮换 |
| Craigslist 检测 → ban | 中 | 高 | 类似缓解 |
| Reddit API 政策变化 | 低 | 中 | Reddit data 是公开 + API 免费 |
| AI 分类准确率低 | 中 | 高 | 人工 review + 反馈循环 |
| Lead quality 低 | 中 | 高 | 持续数据优化 + contractor 反馈 |
| Contractor 不续费 | 中 | 中 | Quality 控制 + onboarding |
| 大玩家进入 | 中 | 高 | 选 niche trades |
| 销售周期长 | 高 | 中 | Cold email 自动化 + Loom 视频 |

---

## 第六部分:Unit Economics 总结

| Metric | Value |
|---|---|
| Average ARPU | $180/mo |
| Gross margin | 90% |
| CAC (outbound) | $30-80/customer |
| LTV (12-month average) | $2,160/customer |
| LTV/CAC | 27-72:1 |
| Payback period | 1-3 months |
| $10K MRR 需 | 55 customers |

---

## 第七部分:扩展路径(90 天后)

### 第二阶段 trades(垂直拓展)
1. Pest control
2. Garage door
3. Appliance repair
4. Septic service
5. Roofer(冰雹季节)

### 第三阶段(产品扩张)
1. Mobile native app(react native)
2. Auto-reply to leads(AI 写回复)
3. CRM 集成
4. Multi-marketplace 监控(Angi / Yelp)

---

## 下一步行动

如果你要启动 **JobRadar**:
1. 选 vertical trades(我推荐 HVAC + Plumber + Electrician 启动)
2. 选 pilot city(推荐:Dallas、Houston、Phoenix、Atlanta、Charlotte — high growth, low saturation)
3. 命名(我会执行)
4. 14 天冲刺(我会按 Day-by-Day 执行)

**只需要告诉我"开始 JobRadar",我会立即进入代码执行模式。**

---

## 数据来源

- trustmrr.com/startup/nextjobconnect-llc(主要验证)
- trustmrr.com/startup/nextjobconnect-llc.md(详细)
- contractor-toolstack.com(AI agents for contractors 评测)
- Reddit r/Plumbing, r/HVAC, r/electricians(用户痛点信号)
- Yelp, HomeAdvisor, Nextdoor(数据源验证)
- Alivo / RoofClaw / Avoca / Hatch 网站(竞品)
- Jobber / Housecall Pro / ServiceTitan pricing(参考)
- LinkedIn (contractor 角色验证)
- Twilio SMS pricing