"""Direction taxonomy: the niches every product, thread and package is filed under.

Each direction carries
  keywords    matched (lower-case substring) against name + description + category
  subreddits  where its buyers talk; used for Reddit demand via Arctic Shift
  queries     intent phrases searched inside those subreddits
  fit         0-1 prior for "a solo builder can ship + sell this in 14 days on $300"
  genres      Apple genre ids whose top charts are checked for this direction

Keep slugs stable: pages, follows and history hang on them.
"""

from __future__ import annotations

import re

DIRECTIONS: list[dict] = [
    {"slug": "ai-photo", "name": "AI photo & headshots", "group": "Creator",
     "keywords": ["headshot", "photo edit", "photo editor", "image edit", "ai photo", "product photo", "background remov",
                  "virtual staging", "mannequin", "image generat", "upscal", "ai image", "portrait", "try-on", "try on", "outfit"],
     "subreddits": ["photography", "Entrepreneur", "ecommerce"], "queries": ["headshot app", "ai photo editor", "product photos"],
     "fit": 0.7, "genres": [6008, 6027]},
    {"slug": "ai-video", "name": "AI video & UGC ads", "group": "Creator",
     "keywords": ["ugc", "video ad", "ai video", "faceless", "shorts", "reels", "tiktok", "clip", "video edit", "avatar video", "subtitles", "caption"],
     "subreddits": ["NewTubers", "TikTokCreators", "marketing"], "queries": ["ugc ads", "video editing tool", "faceless channel"],
     "fit": 0.6, "genres": [6008]},
    {"slug": "content-repurpose", "name": "AI writing & content repurposing", "group": "Creator",
     "keywords": ["repurpos", "copywrit", "blog post", "ai writer", "linkedin post", "content calendar", "ghostwrit", "thread", "carousel"],
     "subreddits": ["content_marketing", "socialmedia", "copywriting"], "queries": ["repurpose content", "ai writing tool", "linkedin posts"],
     "fit": 0.65, "genres": []},
    {"slug": "seo-aeo", "name": "SEO & AI-search visibility", "group": "Marketing",
     "keywords": ["seo", "aeo", "geo ", "backlink", "keyword", "serp", "rank tracker", "chatgpt visibility", "ai search", "perplexity", "llm visibility", "search console"],
     "subreddits": ["SEO", "bigseo", "juststart"], "queries": ["seo tool", "ai overviews", "rank tracker"],
     "fit": 0.6, "genres": []},
    {"slug": "social-scheduling", "name": "Social media management", "group": "Marketing",
     "keywords": ["schedul post", "social media manag", "instagram", "post scheduler", "social scheduler", "buffer", "hootsuite", "x growth", "twitter growth"],
     "subreddits": ["socialmedia", "SocialMediaMarketing", "smallbusiness"], "queries": ["scheduling tool", "social media tool", "alternative to buffer"],
     "fit": 0.55, "genres": []},
    {"slug": "newsletter-email", "name": "Newsletters & email marketing", "group": "Marketing",
     "keywords": ["newsletter", "email marketing", "beehiiv", "substack", "mailchimp", "email list", "cold email", "deliverab"],
     "subreddits": ["Emailmarketing", "Newsletters", "coldemail"], "queries": ["newsletter tool", "email marketing", "deliverability"],
     "fit": 0.6, "genres": []},
    {"slug": "lead-gen", "name": "Lead gen & sales outreach", "group": "Sales",
     "keywords": ["lead gen", "leads", "outreach", "prospect", "crm", "sales pipeline", "linkedin automation", "b2b data", "intent data", "lead", "contact data", "email finder"],
     "subreddits": ["sales", "LeadGeneration", "smallbusiness"], "queries": ["lead generation tool", "find leads", "crm for"],
     "fit": 0.6, "genres": [6000]},
    {"slug": "reddit-community", "name": "Reddit & community marketing", "group": "Marketing",
     "keywords": ["reddit", "subreddit", "community monitor", "brand mention", "social listening", "mention"],
     "subreddits": ["SaaS", "startups", "Entrepreneur"], "queries": ["reddit marketing", "social listening", "brand mentions"],
     "fit": 0.7, "genres": []},
    {"slug": "support-chatbot", "name": "Support & AI chatbots", "group": "Ops",
     "keywords": ["chatbot", "customer support", "helpdesk", "help desk", "live chat", "support agent", "ai agent for support", "faq bot", "ai receptionist", "voice agent"],
     "subreddits": ["CustomerSuccess", "smallbusiness", "SaaS"], "queries": ["ai chatbot", "customer support tool", "ai receptionist"],
     "fit": 0.55, "genres": [6000]},
    {"slug": "payments-churn", "name": "Payments, billing & churn", "group": "Ops",
     "keywords": ["churn", "dunning", "failed payment", "billing", "invoice", "subscription analytics", "stripe", "payment link", "checkout", "revenue recovery"],
     "subreddits": ["SaaS", "stripe", "smallbusiness"], "queries": ["failed payments", "churn", "invoicing tool"],
     "fit": 0.55, "genres": [6000, 6015]},
    {"slug": "analytics", "name": "Web & product analytics", "group": "Dev",
     "keywords": ["analytics", "dashboard", "tracking", "heatmap", "session replay", "uptime", "monitoring", "status page"],
     "subreddits": ["webdev", "SaaS", "analytics"], "queries": ["analytics tool", "alternative to google analytics", "uptime monitoring"],
     "fit": 0.55, "genres": [6026]},
    {"slug": "devtools", "name": "Developer tools & APIs", "group": "Dev",
     "keywords": ["api", "developer", "sdk", "cli", "code review", "github", "deploy", "boilerplate", "starter kit", "mcp", "llm", "agent framework", "open source", "self-host"],
     "subreddits": ["webdev", "programming", "selfhosted"], "queries": ["tool for developers", "alternative to", "self-hosted"],
     "fit": 0.6, "genres": [6026]},
    {"slug": "security", "name": "Security & compliance scanning", "group": "Dev",
     "keywords": ["security", "vulnerab", "pentest", "security scan", "ssl", "api key", "soc 2", "soc2", "gdpr", "compliance", "rls", "vibe cod"],
     "subreddits": ["cybersecurity", "netsec", "SaaS"], "queries": ["security scanner", "soc 2", "vulnerability scan"],
     "fit": 0.5, "genres": []},
    {"slug": "nocode-sites", "name": "Website & app builders", "group": "Dev",
     "keywords": ["website builder", "landing page", "no-code", "nocode", "no code", "site builder", "web builder", "app builder", "template", "waitlist", "link in bio", "website"],
     "subreddits": ["nocode", "webdev", "SideProject"], "queries": ["landing page builder", "no code", "website builder"],
     "fit": 0.55, "genres": []},
    {"slug": "forms-surveys", "name": "Forms, surveys & feedback", "group": "Ops",
     "keywords": ["form builder", "forms", "web form", "contact form", "form backend", "survey", "feedback", "testimonial", "review collect", "nps", "quiz", "poll"],
     "subreddits": ["SaaS", "smallbusiness", "webdev"], "queries": ["form builder", "collect testimonials", "survey tool"],
     "fit": 0.7, "genres": []},
    {"slug": "booking-scheduling", "name": "Booking & appointments", "group": "Ops",
     "keywords": ["booking", "appointment", "calendar", "scheduling", "calendly", "reservation", "meeting"],
     "subreddits": ["smallbusiness", "Entrepreneur", "freelance"], "queries": ["booking app", "appointment scheduling", "alternative to calendly"],
     "fit": 0.6, "genres": [6000, 6007]},
    {"slug": "productivity", "name": "Notes, tasks & productivity", "group": "Consumer",
     "keywords": ["productivity", "to-do", "todo", "task", "notes", "note-taking", "focus", "pomodoro", "planner", "journal", "second brain", "transcri", "meeting notes", "voice note"],
     "subreddits": ["productivity", "ObsidianMD", "Notion"], "queries": ["productivity app", "note taking app", "planner app"],
     "fit": 0.6, "genres": [6007]},
    {"slug": "habit-fitness", "name": "Fitness & habits", "group": "Health",
     "keywords": ["fitness", "workout", "gym", "habit", "running", "steps", "strength", "yoga", "pilates", "coach", "training plan"],
     "subreddits": ["Fitness", "loseit", "getdisciplined"], "queries": ["workout app", "habit tracker", "fitness app"],
     "fit": 0.6, "genres": [6013]},
    {"slug": "nutrition", "name": "Nutrition & calorie tracking", "group": "Health",
     "keywords": ["calorie", "nutrition", "diet", "meal plan", "macro", "food log", "fasting", "recipe", "glp-1", "ozempic", "weight loss"],
     "subreddits": ["loseit", "nutrition", "MealPrepSunday"], "queries": ["calorie app", "meal planner", "food tracking"],
     "fit": 0.6, "genres": [6013, 6023]},
    {"slug": "mental-health", "name": "Mental health, sleep & meditation", "group": "Health",
     "keywords": ["meditat", "mental health", "anxiety", "therapy", "mood", "sleep", "breath", "mindful", "stress", "adhd"],
     "subreddits": ["Anxiety", "ADHD", "Meditation"], "queries": ["app for anxiety", "sleep app", "adhd app"],
     "fit": 0.5, "genres": [6013]},
    {"slug": "health-medical", "name": "Health conditions & care", "group": "Health",
     "keywords": ["health", "symptom", "medical", "doctor", "clinic", "patient", "gout", "diabetes", "blood pressure", "pregnan", "fertility", "period", "skin", "hair loss", "dental"],
     "subreddits": ["AskDocs", "Health", "diabetes"], "queries": ["tracking app", "app for", "health app"],
     "fit": 0.4, "genres": [6013, 6020]},
    {"slug": "language", "name": "Language learning", "group": "Education",
     "keywords": ["language", "vocabulary", "duolingo", "learn spanish", "learn japanese", "flashcard", "pronunciation", "fluency", "translation", "translator", "jlpt", "heritage"],
     "subreddits": ["languagelearning", "LearnJapanese", "Spanish"], "queries": ["app for learning", "alternative to duolingo", "flashcards"],
     "fit": 0.6, "genres": [6017]},
    {"slug": "study-edtech", "name": "Study, exams & tutoring", "group": "Education",
     "keywords": ["study", "exam", "student", "tutor", "homework", "course", "teacher", "classroom", "certification", "test prep", "math"],
     "subreddits": ["GetStudying", "Teachers", "college"], "queries": ["study app", "exam prep", "ai tutor"],
     "fit": 0.55, "genres": [6017]},
    {"slug": "faith", "name": "Faith & religious apps", "group": "Consumer",
     "keywords": ["bible", "prayer", "church", "sermon", "quran", "faith", "christian", "devotional", "muslim", "islam", "catholic", "scripture"],
     "subreddits": ["Christianity", "TrueChristian", "islam"], "queries": ["bible app", "prayer app", "church software"],
     "fit": 0.65, "genres": [6018, 6012]},
    {"slug": "personal-finance", "name": "Budgeting & personal finance", "group": "Finance",
     "keywords": ["budget", "expense", "personal finance", "money manag", "spending", "savings", "net worth", "debt", "bill", "subscription tracker", "receipt"],
     "subreddits": ["personalfinance", "ynab", "povertyfinance"], "queries": ["budget app", "alternative to ynab", "expense tracker"],
     "fit": 0.55, "genres": [6015]},
    {"slug": "trading-investing", "name": "Trading & investing tools", "group": "Finance",
     "keywords": ["trading", "trader", "stock", "crypto", "invest", "portfolio", "options", "forex", "prop firm", "backtest", "signals", "journal trades"],
     "subreddits": ["Daytrading", "options", "algotrading"], "queries": ["trading journal", "backtesting tool", "stock screener"],
     "fit": 0.45, "genres": [6015]},
    {"slug": "real-estate", "name": "Real estate & property", "group": "Vertical",
     "keywords": ["real estate", "realtor", "property", "landlord", "rental", "tenant", "mortgage", "listing", "airbnb", "short-term rental", "home inspection"],
     "subreddits": ["realtors", "Landlord", "airbnb_hosts"], "queries": ["tool for realtors", "landlord software", "airbnb host"],
     "fit": 0.55, "genres": [6000, 6012]},
    {"slug": "trades-field", "name": "Trades & field service", "group": "Vertical",
     "keywords": ["contractor", "hvac", "plumb", "roofing", "roofer", "electrician", "landscap", "field service", "estimate", "quote", "cleaning business", "handyman", "construction"],
     "subreddits": ["Construction", "HVAC", "sweatystartup"], "queries": ["software for contractors", "estimating app", "field service"],
     "fit": 0.6, "genres": [6000]},
    {"slug": "ecommerce", "name": "E-commerce & seller tools", "group": "Commerce",
     "keywords": ["shopify", "ecommerce", "e-commerce", "amazon seller", "etsy", "dropship", "store", "product listing", "reseller", "inventory", "pricing", "poshmark", "ebay"],
     "subreddits": ["shopify", "ecommerce", "Etsy"], "queries": ["shopify app", "etsy tool", "inventory app"],
     "fit": 0.6, "genres": [6024]},
    {"slug": "jobs-career", "name": "Job search & careers", "group": "Consumer",
     "keywords": ["resume", "cv", "job search", "interview", "career", "cover letter", "job board", "hiring", "recruit", "applicant"],
     "subreddits": ["jobs", "resumes", "cscareerquestions"], "queries": ["resume builder", "job search tool", "interview prep"],
     "fit": 0.6, "genres": [6000]},
    {"slug": "dating-social", "name": "Dating & social", "group": "Consumer",
     "keywords": ["dating", "relationship", "couple", "friends", "social app", "chat app", "match", "rizz", "people search", "face search"],
     "subreddits": ["dating", "Tinder", "relationship_advice"], "queries": ["dating app", "app for couples", "rizz"],
     "fit": 0.45, "genres": [6005]},
    {"slug": "family-kids", "name": "Parenting & kids", "group": "Consumer",
     "keywords": ["parent", "kids", "baby", "child", "family", "toddler", "screen time", "parental control", "bedtime story", "homeschool"],
     "subreddits": ["Parenting", "Mommit", "homeschool"], "queries": ["app for kids", "parental control", "baby tracker"],
     "fit": 0.55, "genres": [6012, 6017]},
    {"slug": "pets", "name": "Pets & vets", "group": "Consumer",
     "keywords": ["pet", "dog", "cat", "vet", "veterinar", "puppy", "horse"],
     "subreddits": ["dogs", "cats", "AskVet"], "queries": ["dog app", "pet tracker", "vet software"],
     "fit": 0.6, "genres": [6012]},
    {"slug": "travel", "name": "Travel & trips", "group": "Consumer",
     "keywords": ["travel", "trip", "itinerary", "flight", "hotel", "visa", "nomad", "packing", "air traffic", "airport"],
     "subreddits": ["travel", "digitalnomad", "solotravel"], "queries": ["travel app", "trip planner", "itinerary"],
     "fit": 0.5, "genres": [6003]},
    {"slug": "legal-docs", "name": "Legal, contracts & documents", "group": "Vertical",
     "keywords": ["legal", "contract", "lawyer", "attorney", "pdf", "e-sign", "signature", "document", "notary", "will ", "immigration", "tax"],
     "subreddits": ["smallbusiness", "legaladvice", "tax"], "queries": ["contract tool", "pdf editor", "tax app"],
     "fit": 0.45, "genres": [6000, 6007]},
    {"slug": "audio-voice", "name": "Audio, music & voice", "group": "Creator",
     "keywords": ["audio", "music", "song", "voice", "podcast", "ringtone", "sound", "volume", "tts", "text to speech", "dictation", "beat", "dj"],
     "subreddits": ["podcasting", "WeAreTheMusicMakers", "audioengineering"], "queries": ["podcast tool", "voice app", "music app"],
     "fit": 0.6, "genres": [6011]},
    {"slug": "design-tools", "name": "Design & creative tools", "group": "Creator",
     "keywords": ["design", "logo", "icon", "font", "mockup", "figma", "canva", "vector", "svg", "illustration", "3d", "pen plot", "print on demand", "tattoo", "slides", "presentation"],
     "subreddits": ["graphic_design", "Design", "web_design"], "queries": ["design tool", "alternative to canva", "logo maker"],
     "fit": 0.6, "genres": [6027]},
    {"slug": "mobile-utility", "name": "Phone utilities", "group": "Consumer",
     "keywords": ["widget", "wallpaper", "cleaner", "storage", "vpn", "scanner", "qr", "battery", "keyboard", "iphone", "android", "lock screen", "blocker", "screen time"],
     "subreddits": ["iphone", "ios", "androidapps"], "queries": ["app for iphone", "widget app", "best app for"],
     "fit": 0.65, "genres": [6002]},
    {"slug": "ai-agents", "name": "AI assistants & agents", "group": "AI",
     "keywords": ["ai assistant", "ai agent", "gpt", "chatgpt", "claude", "automation", "workflow", "zapier", "n8n", "copilot", "agentic"],
     "subreddits": ["ChatGPT", "automation", "n8n"], "queries": ["ai agent for", "automate", "workflow automation"],
     "fit": 0.55, "genres": [6007]},
]

BY_SLUG = {d["slug"]: d for d in DIRECTIONS}
OTHER = {"slug": "other", "name": "Unclassified", "group": "Other", "keywords": [], "subreddits": [], "queries": [], "fit": 0.5, "genres": []}

# Names of TrustMRR categories mapped straight to a direction, used when keywords miss.
CATEGORY_HINTS = {
    "productivity": "productivity", "health & fitness": "habit-fitness", "health": "health-medical",
    "education": "study-edtech", "finance": "personal-finance", "fintech": "personal-finance",
    "marketing": "seo-aeo", "sales": "lead-gen", "developer tools": "devtools", "security": "security",
    "e-commerce": "ecommerce", "ecommerce": "ecommerce", "analytics": "analytics", "design": "design-tools",
    "real estate": "real-estate", "travel": "travel", "social media": "social-scheduling",
    "customer support": "support-chatbot", "legal": "legal-docs", "music": "audio-voice",
    "artificial intelligence": "ai-agents", "content creation": "content-repurpose", "no-code": "nocode-sites",
    "photo & video": "ai-photo", "lifestyle": "mobile-utility", "utilities": "mobile-utility",
    "graphics & design": "design-tools", "medical": "health-medical", "food & drink": "nutrition",
    "social networking": "dating-social", "business": "lead-gen", "reference": "study-edtech", "books": "faith",
}

_WORD = re.compile(r"[a-z0-9]+")


def _hits(text: str, kw: str) -> bool:
    # Keywords match at a word start ("form" hits "forms", not "platform");
    # short ones (<=3 chars) must be a whole word.
    k = kw.strip()
    tail = r"\b" if len(k) <= 3 else ""
    return re.search(rf"\b{re.escape(k)}{tail}", text) is not None


def classify(name: str = "", description: str = "", category: str = "") -> tuple[str, float]:
    """Return (direction slug, confidence 0-1). Name hits count double."""
    name_l = (name or "").lower()
    body = f"{name_l} {(description or '').lower()}"
    best, best_score = "other", 0.0
    for d in DIRECTIONS:
        score = 0.0
        for kw in d["keywords"]:
            if _hits(body, kw):
                score += 1.0 + (1.0 if _hits(name_l, kw) else 0.0)
        if score > best_score:
            best, best_score = d["slug"], score
    if best_score == 0 and category:
        hint = CATEGORY_HINTS.get(category.strip().lower())
        if hint:
            return hint, 0.3
    return best, min(1.0, best_score / 3.0)


def _scores(name: str, description: str) -> dict[str, float]:
    name_l = (name or "").lower()
    body = f"{name_l} {(description or '').lower()}"
    out = {}
    for d in DIRECTIONS:
        sc = sum(1.0 + (1.0 if _hits(name_l, kw) else 0.0) for kw in d["keywords"] if _hits(body, kw))
        if sc:
            out[d["slug"]] = sc
    return out


GENRE_HINTS = {6000: "lead-gen", 6002: "mobile-utility", 6005: "dating-social", 6007: "productivity",
               6008: "ai-photo", 6011: "audio-voice", 6012: "mobile-utility", 6013: "habit-fitness",
               6015: "personal-finance", 6017: "study-edtech", 6018: "faith", 6020: "health-medical",
               6023: "nutrition", 6024: "ecommerce", 6026: "devtools", 6027: "design-tools", 6003: "travel"}


def classify_app(name: str, description: str, genre_id) -> tuple[str, float]:
    """Apps: prefer directions that list the app's App Store genre; otherwise need a strong keyword hit,
    else fall back to the genre's default direction. Only the first 300 chars of the store text count."""
    sc = _scores(name, (description or "")[:300])
    try:
        gid = int(genre_id) if genre_id is not None else None
    except (TypeError, ValueError):
        gid = None
    in_genre = {k: v for k, v in sc.items() if gid is not None and gid in BY_SLUG[k]["genres"]}
    if in_genre:
        best = max(in_genre, key=in_genre.get)
        return best, min(1.0, in_genre[best] / 3.0)
    if sc:
        best = max(sc, key=sc.get)
        if sc[best] >= 3:
            return best, min(1.0, sc[best] / 4.0)
    if gid in GENRE_HINTS:
        return GENRE_HINTS[gid], 0.25
    return "other", 0.0
