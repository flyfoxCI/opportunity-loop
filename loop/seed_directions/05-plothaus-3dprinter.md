# Direction 05 — PlotHaus: 3D Printer Hobbyist Tool (Pen Plotter 优化)

**推荐等级:** #5 (Confidence 7/10)
**代币代号:** PlotHaus (or specific tool name)
**目标 MRR:** $10,000/月 (60-90 天可达)
**MVP 上线时间:** 14 天
**营销预算:** $300/30 天

---

## 第一部分:深度调研报告

### 1.1 市场验证证据

#### 关键信号 — 3dplotter.xyz
- **来源:** trustmrr.com/startup/3dplotter
- **30 天营收:** $1,898
- **MRR:** $0(纯一次性)
- **定价:** €29.90 一次性
- **域名:** 3dplotter.xyz(Ahrefs DR 4)
- **30 天访客:** 1,239
- **转化率:** ~3%(假设 39 单 × €29.90)
- **MoM 增长:** +21%
- **国家:** Greece
- **成立年份:** 2025
- **ICP:** "Makers & Etsy Sellers, Studios & Agencies, Educators & STEAM"
- **产品:** "Complete pen plotting platform. Turn any 3D printer into a professional pen plotter. Optimized presets for Bambu Lab printers, plus Custom Board for any printer with custom dimensions. Features STL pen holder database, design gallery, community sharing, G-code generator, 50+ Hershey fonts, layout tools, and visual calibration."

#### 为什么这是黄金信号
- **1239 访客 / 月**, **3% 转化** = 真实 demand
- **Bambu Lab 是 2024-2026 增长最快的 3D 打印机品牌**(估计用户数百万)
- **3D printer hobbyist 社区活跃**:Reddit r/3Dprinting (1.5M+), r/BambuLab (300K+), r/ender3 (200K+)
- **3D 打印用户对 pen plotting 有明确兴趣**(50+ Hershey fonts 是产品亮点)
- **几乎零竞争**(专门做 "pen plotter G-code generator for 3D printers")

### 1.2 竞品尽调

#### 直接竞品(几乎为零)

我搜了 "3D printer pen plotter", "pen plotter G-code", "Bambu Lab pen plotter", "pen plotter software":
- **结论:除了 3dplotter.xyz,没有任何专门做这个的产品**

#### 间接竞品(部分功能重叠)

| 玩家 | 状态 | 关系 |
|---|---|---|
| **3dplotter.xyz** | 主要参考(TrustMRR) | Direct competitor |
| **Inkscape + J Tech Photonics Laser Tool plugin** | 开源 | 需要用户组装,UX 差 |
| **PenPlotterBerlin** | 德国,硬件 + 软件 | 主要硬件,software 部分少 |
| **Axidraw / Eggbot** | 硬件 $200-$500 | 需要专门硬件,不通用 |
| **Makelangelo software** | 开源 | 主要给大型机器,不是 3D 打印机 |
| **GRBL-based CNC software** | 开源 | 不是为 pen plot 设计 |
| **Bambu Lab Studio** | 厂商自带 | 不支持 pen plotter |

#### 真实竞品缺口
- **"pen plotter + 3D printer" + "Bambu Lab presets"** = 完全空白
- Inkscape + 各种 plugin 是 DIY,不是产品
- 没有 SaaS 模式(都是一次性或开源)

### 1.3 市场规模

#### TAM
- 全球 3D 打印机用户:**500 万+**(估计)
- Bambu Lab 用户:**200 万+**(他们增长最快)
- Pen plotting 兴趣者:估计 5-10% = 10 万-50 万
- 工具 WTP:€29.90-$50 一次性 OR $5-$15/mo 订阅

#### SAM
- 美国 + 欧洲 + 澳洲 3D 打印机用户:200 万
- Pen plotter 兴趣:5% = 10 万
- 转化付费:5-10% = 5000-10000 客户

#### SOM
- 第一年目标:**200-1000 付费用户**
- @ €29.90 一次性 OR $9.99/mo 订阅 = **取决于定价**

### 1.4 商业模式选择(关键决策)

#### 选项 A:纯一次性(像 3dplotter)
- €29.90 一次性
- 1000 客户 = €29,900 一次性收入
- 但**月收入 = 0**(无 MRR)
- **不符合 $10K MRR 目标**

#### 选项 B:订阅(SaaS 模式)
- Free:5 G-code generations/月
- Pro: $9.99/mo 无限 + presets + design gallery
- Lifetime: $199 一次性(代替订阅)
- **1000 Pro 订阅 = $10K MRR ✓**

#### 选项 C:混合(推荐)
- Free tier(获客)
- Pro $9.99/mo(月订阅)
- Lifetime $199(替代订阅)
- Design Marketplace(卖家抽成 30%)
- Custom presets(高级功能)

#### 我推荐:**选项 C(混合)**
- Free 获客 + Pro 月订阅
- Lifetime 给不愿订阅的(虽然 LTV 较低)
- Design Marketplace 是 P2 拓展

### 1.5 目标用户画像

#### Primary ICP — "Bambu Ben"
- 角色:Bambu Lab A1 / X1 / P1 拥有者
- 爱好:DIY + 创意 + 手工艺
- 痛点:
  - 想要 pen plotter,但 Axidraw $400 太贵
  - 想要用现有的 3D 打印机做 pen plot
  - 在 Etsy 卖定制 pen plot 作品
- WTP:€29.90-$199 一次性 OR $9.99/mo
- 触达:
  - Reddit r/BambuLab (300K), r/3Dprinting (1.5M)
  - YouTube (3D printing channels)
  - Etsy(pen plot 卖家社区)

#### Secondary ICP — "Etsy Eva"
- 角色:Etsy 卖家,做 custom pen plot 卡片 / 婚礼请帖
- 想要:稳定 G-code generation + 漂亮字体
- WTP:€29.90/mo 订阅(为了业务)

#### Tertiary ICP — "STEAM Steve"
- 角色:学校 STEAM 教师
- 想要:便宜 pen plotter 给学生
- WTP:机构 $99-$299/yr

### 1.6 风险评估

| 风险 | 概率 | 影响 | 缓解 |
|---|---|---|---|
| Bambu Lab 内置类似功能 | 低 | 高 | 持续 niche(pen plotter 是边缘用例) |
| 开源替代 | 中 | 中 | 持续 UX 优势 + presets |
| 一次性天花板低 | 高 | 中 | 转向订阅 + design marketplace |
| 用户增长慢(3D printing 是 niche) | 中 | 中 | Reddit + YouTube + Etsy 多渠道 |

---

## 第二部分:PRD(产品需求文档)

### 2.1 产品定义

**One-liner:**
> "Turn your Bambu Lab (or any) 3D printer into a professional pen plotter in 60 seconds. Upload SVG/text/AI design, get optimized G-code ready to print."

**Tagline:** "From 3D printer to pen plotter in 60 seconds."

### 2.2 核心使用流程

#### 用户视角
1. 注册账户(邮箱 / Google)
2. 选 printer model(Bambu Lab A1/X1/P1, Prusa, Ender, Other)
3. 选 pen holder(各种 STL 选项)
4. 上传 design:
   - SVG file
   - Text(转 SVG)
   - AI 生成图像
   - 模板库(gallery)
5. 设置参数:
   - Pen lift height
   - Drawing speed
   - Layer height(单 layer,simple plot)
6. 预览(side-by-side)
7. 下载 G-code
8. 打印!

### 2.3 用户故事(Epic)

#### Epic 1:Onboarding + Printer Selection(Day 14)
**US-1.1:** 作为 user,我可以注册(邮箱 / Google)
**US-1.2:** 作为 user,我可以选 printer model
**US-1.3:** 作为 user,我可以选 pen holder STL
**US-1.4:** 作为 user,我可以预览 printer + pen 配合

#### Epic 2:Design Upload + Conversion(Day 14)
**US-2.1:** 作为 user,我可以上传 SVG file
**US-2.2:** 作为 user,我可以输入 text(转 SVG)
**US-2.3:** 作为 user,我可以从 gallery 选模板
**US-2.4:** 作为 system,我可以 SVG → G-code 转换
**US-2.5:** 作为 user,我可以预览 G-code 路径

#### Epic 3:Parameters(Day 14)
**US-3.1:** 作为 user,我可以设置 pen lift height
**US-3.2:** 作为 user,我可以设置 drawing speed
**US-3.3:** 作为 user,我可以选 Hershey font(50+)
**US-3.4:** 作为 user,我可以调整布局(centering, margins, scaling)

#### Epic 4:Generation + Download(Day 14)
**US-4.1:** 作为 user,我可以下载 G-code 文件
**US-4.2:** 作为 user,我可以看到 estimated print time
**US-4.3:** 作为 user,我可以保存到 library

#### Epic 5:Design Gallery(Day 21)
**US-5.1:** 作为 user,我可以浏览 community designs
**US-5.2:** 作为 user,我可以 fork 别人的设计
**US-5.3:** 作为 user,我可以上传自己的设计到 gallery(Pro)

#### Epic 6:Subscription(Day 14)
**US-6.1:** 作为 user,我可以选 plan:
  - Free:5 generations/mo
  - Pro: $9.99/mo 无限 + design gallery upload + advanced params
  - Lifetime: $199 一次性
**US-6.2:** 作为 user,我可以管理订阅

### 2.4 显式功能范围

#### P0 (MUST - Day 14)
- 注册 + printer 选择
- SVG upload + text-to-SVG
- Hershey font(50+ 内置)
- G-code 生成 + 下载
- Basic parameters(speed, lift height)
- Free + Pro 订阅

#### P1 (SHOULD - Day 21)
- Design gallery(community)
- Bambu Lab Studio 集成(可选)
- Advanced parameters(layer height, pen pressure)
- Print preview(G-code visualization)

#### P2 (NICE - Day 30+)
- AI 图像生成(text → plot art)
- Etsy 集成(直接卖)
- Mobile app
- Cloud library

#### OUT OF SCOPE (MVP 不做)
- 自定义硬件 pen holder 销售
- Pen plot 服务 marketplace
- CNC 切割(只 pen plot)
- 视频教程库(redirect 到 YouTube)

### 2.5 技术架构

#### Stack
| Layer | 技术 | 理由 |
|---|---|---|
| Frontend | Next.js 15 | 模板成熟 |
| UI | Tailwind + shadcn/ui | 现代 |
| Backend | Next.js API + tRPC | 类型安全 |
| Database | PostgreSQL (Supabase) | 主数据 |
| Auth | Clerk | 简单 |
| File Storage | Cloudflare R2 | SVG + G-code 存储 |
| SVG Processing | svgo + custom | 优化 SVG |
| G-code Generation | Custom (Node.js / Python) | 核心算法 |
| AI Image (P2) | Stable Diffusion / DALL-E | AI art → SVG |
| Payment | Stripe | Subscription |
| Hosting | Vercel | 简单 |

#### 关键算法:SVG → G-code

这是核心技术。我需要实现:

```
INPUT:
- SVG path data (or text converted to SVG via Hershey font)
- Printer model (Bambu Lab A1 / X1 / Prusa / Ender)
- Parameters (lift height, speed, etc.)

PROCESS:
1. Parse SVG path
2. Convert curves to line segments (resolution: 0.1mm)
3. Generate G-code:
   - G0 Z[lift_height] (pen up)
   - G0 X[x] Y[y] (move to start)
   - G1 Z[draw_height] F[speed] (pen down)
   - G1 X[x] Y[y] F[speed] (draw line)
   - Repeat for all paths
4. Add printer-specific headers:
   - Bambu Lab: specific G-code commands
   - Prusa: PrusaSlicer format
   - Ender: Marlin format

OUTPUT:
- .gcode file ready to print
```

#### 数据模型(简化)
```prisma
model User {
  id          String   @id @default(cuid())
  email       String   @unique
  name        String?
  printerModel String?
  plan        String   @default("free")
  stripeCustomerId String?
  stripeSubId String?
  currentPeriodEnd DateTime?
  generations Generation[]
  designs     Design[]
  createdAt   DateTime @default(now())
}

model Generation {
  id          String   @id @default(cuid())
  userId      String
  user        User     @relation(fields: [userId], references: [id])
  inputType   String   // svg, text, template
  inputData   Json     // SVG content or text or template ID
  parameters  Json     // {speed, lift_height, font, etc.}
  outputUrl   String   // G-code file URL
  duration    Int?     // estimated print time (minutes)
  status      String   @default("processing") // done, failed
  createdAt   DateTime @default(now())
}

model Design {
  id          String   @id @default(cuid())
  userId      String
  user        User     @relation(fields: [userId], references: [id])
  title       String
  description String?
  svgUrl      String
  thumbnailUrl String?
  isPublic    Boolean  @default(false)
  forks       Int      @default(0)
  createdAt   DateTime @default(now())
}

model HersheyFont {
  id       String @id @default(cuid())
  name     String  // "Hershey Sans 1"
  category String  // "sans", "serif", "script", "gothic"
  data     Json    // character paths
}
```

#### 关键代码模块

`/lib/gcode-generator.ts`:
```typescript
interface SVGPath {
  d: string;
  // ... parsed path data
}

interface GcodeParams {
  printerModel: 'bambu-a1' | 'bambu-x1' | 'prusa' | 'ender';
  liftHeight: number;  // mm
  drawHeight: number;  // mm
  speed: number;       // mm/min
  penUpCmd?: string;
  penDownCmd?: string;
}

function generateGcode(path: SVGPath[], params: GcodeParams): string {
  let gcode = '';
  
  // Printer-specific header
  gcode += getHeader(params.printerModel);
  
  for (const p of path) {
    // Move to start
    gcode += `G0 X${p.startX} Y${p.startY}\n`;
    // Pen down
    gcode += `G1 Z${params.drawHeight} F${params.speed}\n`;
    // Draw segments
    for (const seg of p.segments) {
      gcode += `G1 X${seg.x} Y${seg.y} F${params.speed}\n`;
    }
    // Pen up
    gcode += `G0 Z${params.liftHeight}\n`;
  }
  
  // Printer-specific footer
  gcode += getFooter(params.printerModel);
  
  return gcode;
}
```

### 2.6 定价

| Plan | 价格 | 功能 | 目标 |
|---|---|---|---|
| Free | $0 | 5 generations/mo, 5 Hershey fonts | 试用 |
| **Pro** | **$9.99/mo** | 无限 generations, 50+ fonts, gallery upload, advanced params | Hobbyist + Etsy sellers |
| Lifetime | $199 一次性 | 永久 Pro | 不愿订阅者 |
| Studio | $29.99/mo | Pro + multi-user + API | 商业用户 |

#### Unit Economics

**Pro 客户 (@$9.99):**
- 收入:$9.99
- Stripe 抽成:$0.59
- 边际成本(API + 存储):~$0.50-$1/客户
- **毛利:$8-$9/客户/月 (85% margin) ✓**

**1000 Pro 客户 = $10K MRR ✓**

### 2.7 关键 SLA

- SVG → G-code 生成:< 5 秒
- 预览加载:< 2 秒
- 文件下载:< 1 秒
- G-code 准确率:> 95%(用户能直接打印)

---

## 第三部分:30 天营销计划(预算 $300)

### 3.1 预算分配

| 项目 | 金额 | 用途 |
|---|---|---|
| 域名 | $12 | plothaus.com / 3dplot.app / gplot.io |
| Vercel Pro | $20 | 性能 |
| Supabase Pro | $25 | DB + Storage |
| Resend Pro | $20 | 邮件 |
| Stripe fees | 按交易 | - |
| ProductHunt boost | $50 | 启动日 |
| YouTube sponsored creator | $100 | 1-2 个 video integration |
| Reserve | $73 | 应急 |
| **总计** | **$300** |  |

### 3.2 30 天日历(逐日)

#### Week 1:Day 1-7 — 上线 + Reddit 渗透

**Day 1 (上线日)**
- ProductHunt 发布:"PlotHaus — Turn your 3D printer into a pen plotter in 60 seconds"
- IndieHackers "Show IH"
- X thread:"I built a tool that turns any 3D printer into a pen plotter"
- **关键:Reddit r/3Dprinting, r/BambuLab, r/ender3, r/prusa3d 发文**(每个 subreddit 不同角度)
- 在 YouTube 联系 5 个 3D printing KOL

**Day 2-3: 内容准备**
- 3 篇 SEO 文章:
  1. "How to Use Your Bambu Lab as a Pen Plotter"
  2. "Pen Plotter G-Code: Complete Guide for 3D Printers"
  3. "Best Pen Plotter Software for 3D Printers 2026"
- Medium + dev.to + 自有博客

**Day 4-5: 社区渗透**
- 在 r/3Dprinting, r/BambuLab 发 15 条 helpful comments
- 加入 5 个 3D printing Discord(3D Printing, Bambu Lab Users, etc.)
- 在 X 关注 100 个 3D printing 影响者

**Day 6-7: 第一批用户**
- 联系 5 个 Etsy 卖家(pen plot 类别)
- 提供"免费 Pro 30 天"换取 review
- 在 Reddit 私信 10 个 "我做了这个工具" 给热帖作者

**Week 1 KPI:**
- 100 signups
- 15 Pro = **$150 MRR**

#### Week 2:Day 8-14 — YouTube + 案例

**Day 8-9: YouTube 集成**
- 联系 3 个 3D printing YouTubers(50K+ subs)
- 提供"终身 Pro + 现金 $50"换取 review video
- 1 个 review 上线 = 200-500 signups

**Day 10-11: 客户故事**
- "Case Study: Etsy Eva Made $2K/mo with Pen Plots"
- "Case Study: Bambu Lab User Turned Hobby into Side Income"

**Day 12-14: 内容爆发**
- X thread:"5 reasons your 3D printer can be a pen plotter"
- LinkedIn 文章
- 在 Reddit 持续 reply helpful comments

**Week 2 KPI:**
- 300 signups
- 80 Pro = **$800 MRR**

#### Week 3:Day 15-21 — 渠道扩张

**Day 15-17: 合作伙伴**
- 联系 5 个 Etsy pen plot 卖家
- Affiliate 30% 终身佣金
- 联系 Bambu Lab 经销商 / community

**Day 18-21: 第二轮内容**
- 5 条 X thread
- 5 篇 LinkedIn 文章
- 1 个 lead gen 报告:"State of Pen Plotting 2026"

**Week 3 KPI:**
- 600 signups
- 250 Pro = **$2.5K MRR**

#### Week 4:Day 22-30 — 收网

**Day 22-24: 转化优化**
- Free trial → paid 转化漏斗优化
- Email 序列

**Day 25-27: 案例 + 紧迫感**
- "30-day review"
- "Founding Maker Pricing" - 前 100 客户终身 30% off

**Day 28-30: 收网**
- 100 trial 用户 personal outreach
- 在 X 跑 "Free Pro for 30 days" 给 10 个 Etsy 卖家

**Week 4 KPI:**
- 1000 signups
- 400 Pro = **$4K MRR**

### 3.3 30 → 90 天路径

| Day | 目标 | 行动 |
|---|---|---|
| Day 30 | $4K MRR | 400 Pro |
| Day 60 | $7K MRR | + Etsy integration + Design marketplace |
| Day 90 | **$10K MRR** ✓ | 1000 Pro |

---

## 第四部分:执行指南(Day-by-Day)

### 4.1 14 天冲刺计划

#### Day 1-2:基础 + G-code PoC
- [ ] 注册域名(`plothaus.com`, `gplot.io`, `3dplot.app`)
- [ ] Next.js + Supabase setup
- [ ] Clerk + Stripe accounts
- [ ] **PoC:SVG → G-code 转换 1 个简单例子**(验证算法)

**Day 1-2 交付物:** 项目骨架 + G-code 生成器 PoC

#### Day 3-5:核心 G-code Generator
- [ ] SVG 解析 + path 处理
- [ ] Hershey font library(50+ fonts,内置)
- [ ] G-code 生成器(完整版)
- [ ] Bambu Lab presets(优化)
- [ ] Preview UI(G-code 路径可视化)

**Day 3-5 交付物:** SVG/text → G-code 工作

#### Day 6-8:UI + Printer Selection
- [ ] Printer model selection(Bambu Lab A1/X1/P1, Prusa, Ender, Custom)
- [ ] Pen holder selection
- [ ] Parameters UI(speed, lift height, etc.)
- [ ] Generation + download

**Day 6-8 交付物:** 完整生成流程

#### Day 9-10:User Account + Generation History
- [ ] Clerk auth
- [ ] User library(generations 历史)
- [ ] Email 通知

**Day 9-10 交付物:** 用户系统

#### Day 11-12:Subscription + Stripe
- [ ] Stripe Checkout
- [ ] Free tier 限制(5 generations/mo)
- [ ] Pro upgrade flow

**Day 11-12 交付物:** 完整订阅系统

#### Day 13:QA + 内测
- [ ] 5 个真实 3D printer user 内测
- [ ] 修复 bug
- [ ] 优化 UX

**Day 13 交付物:** 生产就绪

#### Day 14:公开上线
- [ ] ProductHunt
- [ ] IndieHackers
- [ ] X thread
- [ ] Reddit(r/3Dprinting, r/BambuLab)
- [ ] Email blast

**Day 14 交付物:** 公开上线

### 4.2 完整技术栈(实际成本)

| 服务 | 月成本(初期) | 月成本(1000 客户) |
|---|---|---|
| Vercel Pro | $20 | $20 + 超额 |
| Supabase Pro | $25 | $25 + 超额 |
| Clerk | Free | $25 |
| Cloudflare R2 | $0.15/GB | $5 |
| Stripe | 2.9% + 30¢ | ~$290 |
| Resend | $20 | $20 |
| **小计** | **~$65 + Stripe** | **~$95 + Stripe** |

**单位经济(Pro @ $9.99):**
- 收入:$9.99
- Stripe 抽成:$0.59
- 边际成本(API + 存储):~$0.50-$1/客户
- **毛利:$8-$9/客户/月 (85% margin) ✓**

### 4.3 关键 Hershey Font Library

Hershey fonts 是 SVG-based vector fonts,1967 年 NASA 发布,完全开源。

- **50+ fonts** 内置:
  - Sans:Hershey Sans 1, Futura Medium, etc.
  - Serif:Hershey Serif 1, Times, etc.
  - Script:Hershey Script 1, Script Simplex, etc.
  - Gothic:Gothic English, Gothic Italian, etc.
  - Cyrillic, Greek, Japanese 等

可以**免费获取 Hershey font data**:
- https://github.com/evil-mad/plotink/blob/master/HersheyFont.py
- 转换格式:`{char_code: {path: "...", width: 5}}`

---

## 第五部分:风险与缓解

| 风险 | 概率 | 影响 | 缓解 |
|---|---|---|---|
| Bambu Lab 内置 pen plotter 功能 | 低 | 高 | 持续 niche 优化 + 跨品牌 |
| 开源替代(更友好 UX) | 中 | 中 | 持续 UX 优势 + presets |
| 一次性天花板低 | 中 | 中 | 转向订阅模式 |
| Etsy pen plot 市场萎缩 | 低 | 中 | 多渠道:STEAM 教师、爱好者 |
| 3D printing 用户增长放缓 | 低 | 高 | 拓展到激光雕刻、cutting |

---

## 第六部分:Unit Economics 总结

| Metric | Value |
|---|---|
| Average ARPU | $9.99/mo |
| Gross margin | 85% |
| CAC (organic) | $2-5/customer |
| LTV (24-month average) | $240/customer |
| LTV/CAC | 48-120:1 |
| Payback period | < 1 month |
| $10K MRR 需 | 1000 customers |

---

## 第七部分:扩展路径(90 天后)

### 第二阶段(功能扩张)
1. Laser cutting(激光雕刻)支持
2. CNC routing 集成
3. Direct Etsy integration(自动 list)
4. AI image generation(DALL-E → plot art)

### 第三阶段(社区扩张)
1. Marketplace(卖家抽成)
2. Marketplace for pen plot services(printed cards 销售)
3. Education tier(school plans)
4. White-label for pen plot services

---

## 下一步行动

如果你要启动 **PlotHaus**:
1. 选 printer 启动组(我推荐 Bambu Lab 启动 + Prusa 拓展)
2. 命名(我会执行)
3. 14 天冲刺(我会按 Day-by-Day 执行)

**只需要告诉我"开始 PlotHaus",我会立即进入代码执行模式。**

---

## 数据来源

- trustmrr.com/startup/3dplotter(主要验证)
- trustmrr.com/category/design-tools(EasyMockups, Komposo, Sleek 等)
- Reddit r/3Dprinting, r/BambuLab, r/ender3(用户信号)
- Bambu Lab official website(用户基数估算)
- Hershey font 文档(技术参考)
- Inkscape + J Tech plugins(竞品分析)
- Etsy pen plot search(卖家数量估算)