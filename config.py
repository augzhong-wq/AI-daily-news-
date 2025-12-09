"""
AI Daily News System - 配置文件
增强版：50+新闻源，100+原始信息采集
"""
import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI API配置
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

# ==================== 新闻源配置 ====================
# 要求：每日采集100+条原始信息

NEWS_SOURCES = {
    # ==================== 国内新闻源 (15+) ====================
    "domestic": [
        # 科技媒体
        {
            "name": "36氪",
            "type": "rss",
            "url": "https://36kr.com/feed",
            "category": "domestic",
            "priority": "high"
        },
        {
            "name": "机器之心",
            "type": "rss",
            "url": "https://www.jiqizhixin.com/rss",
            "category": "domestic",
            "priority": "high"
        },
        {
            "name": "量子位",
            "type": "rss",
            "url": "https://www.qbitai.com/feed",
            "category": "domestic",
            "priority": "high"
        },
        {
            "name": "新智元",
            "type": "rss",
            "url": "https://www.xinzhiyuan.com/feed",
            "category": "domestic",
            "priority": "high"
        },
        {
            "name": "AI科技评论",
            "type": "rss",
            "url": "https://www.leiphone.com/feed",
            "category": "domestic",
            "priority": "medium"
        },
        {
            "name": "PaperWeekly",
            "type": "rss",
            "url": "https://www.paperweekly.site/rss",
            "category": "domestic",
            "priority": "medium"
        },
        # 财经媒体
        {
            "name": "财新网科技",
            "type": "rss",
            "url": "https://www.caixin.com/rss/tech.xml",
            "category": "domestic",
            "priority": "high"
        },
        {
            "name": "第一财经",
            "type": "rss",
            "url": "https://www.yicai.com/rss/feed.xml",
            "category": "domestic",
            "priority": "medium"
        },
        # 官方渠道
        {
            "name": "工信部",
            "type": "web",
            "url": "https://www.miit.gov.cn/",
            "category": "domestic",
            "priority": "high"
        },
        {
            "name": "科技部",
            "type": "web",
            "url": "https://www.most.gov.cn/",
            "category": "domestic",
            "priority": "high"
        },
        # 企业官方
        {
            "name": "百度AI",
            "type": "rss",
            "url": "https://ai.baidu.com/feed",
            "category": "domestic",
            "priority": "medium"
        },
        {
            "name": "阿里达摩院",
            "type": "web",
            "url": "https://damo.alibaba.com/",
            "category": "domestic",
            "priority": "medium"
        },
        {
            "name": "腾讯AI Lab",
            "type": "web",
            "url": "https://ai.tencent.com/",
            "category": "domestic",
            "priority": "medium"
        },
        {
            "name": "华为云AI",
            "type": "web",
            "url": "https://www.huaweicloud.com/product/ai.html",
            "category": "domestic",
            "priority": "medium"
        },
        {
            "name": "智谱AI",
            "type": "web",
            "url": "https://www.zhipuai.cn/",
            "category": "domestic",
            "priority": "medium"
        },
    ],
    
    # ==================== 国际新闻源 (35+) ====================
    "international": [
        # ========== 顶级科技媒体 ==========
        {
            "name": "TechCrunch AI",
            "type": "rss",
            "url": "https://techcrunch.com/category/artificial-intelligence/feed/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "The Verge AI",
            "type": "rss",
            "url": "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "VentureBeat AI",
            "type": "rss",
            "url": "https://venturebeat.com/category/ai/feed/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Wired AI",
            "type": "rss",
            "url": "https://www.wired.com/feed/tag/ai/latest/rss",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Ars Technica AI",
            "type": "rss",
            "url": "https://feeds.arstechnica.com/arstechnica/technology-lab",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "ZDNet AI",
            "type": "rss",
            "url": "https://www.zdnet.com/topic/artificial-intelligence/rss.xml",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "The Information",
            "type": "rss",
            "url": "https://www.theinformation.com/feed",
            "category": "international",
            "priority": "high"
        },
        
        # ========== 顶级财经媒体 ==========
        {
            "name": "华尔街日报WSJ Tech",
            "type": "rss",
            "url": "https://feeds.a]wsj.com/rss/RSSWorldNews.xml",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Bloomberg Technology",
            "type": "rss",
            "url": "https://feeds.bloomberg.com/technology/news.rss",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Reuters Technology",
            "type": "rss",
            "url": "https://www.reutersagency.com/feed/?best-topics=tech",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Financial Times Tech",
            "type": "rss",
            "url": "https://www.ft.com/technology?format=rss",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "CNBC Tech",
            "type": "rss",
            "url": "https://www.cnbc.com/id/19854910/device/rss/rss.html",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Forbes AI",
            "type": "rss",
            "url": "https://www.forbes.com/ai/feed/",
            "category": "international",
            "priority": "medium"
        },
        
        # ========== 学术与研究机构 ==========
        {
            "name": "MIT Technology Review",
            "type": "rss",
            "url": "https://www.technologyreview.com/feed/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "MIT News AI",
            "type": "rss",
            "url": "https://news.mit.edu/topic/artificial-intelligence2-rss.xml",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Stanford HAI",
            "type": "rss",
            "url": "https://hai.stanford.edu/news/feed",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Berkeley AI Research",
            "type": "rss",
            "url": "https://bair.berkeley.edu/blog/feed.xml",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Carnegie Mellon AI",
            "type": "rss",
            "url": "https://www.cs.cmu.edu/news/feed",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Oxford AI",
            "type": "rss",
            "url": "https://www.ox.ac.uk/news-and-events/rss-feeds",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Nature AI",
            "type": "rss",
            "url": "https://www.nature.com/subjects/artificial-intelligence.rss",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Science Magazine",
            "type": "rss",
            "url": "https://www.science.org/rss/news_current.xml",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "arXiv AI",
            "type": "rss",
            "url": "https://rss.arxiv.org/rss/cs.AI",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Google AI Blog",
            "type": "rss",
            "url": "https://blog.research.google/feeds/posts/default",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "DeepMind Blog",
            "type": "rss",
            "url": "https://deepmind.com/blog/feed/basic/",
            "category": "international",
            "priority": "high"
        },
        
        # ========== 智库与政策研究 ==========
        {
            "name": "RAND Corporation AI",
            "type": "rss",
            "url": "https://www.rand.org/topics/artificial-intelligence.html/feed",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Brookings AI",
            "type": "rss",
            "url": "https://www.brookings.edu/topic/artificial-intelligence/feed/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "CSIS Technology",
            "type": "rss",
            "url": "https://www.csis.org/programs/technology-policy-program/feed",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Council on Foreign Relations",
            "type": "rss",
            "url": "https://www.cfr.org/rss.xml",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Center for AI Safety",
            "type": "web",
            "url": "https://www.safe.ai/",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "AI Now Institute",
            "type": "rss",
            "url": "https://ainowinstitute.org/feed",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Future of Life Institute",
            "type": "rss",
            "url": "https://futureoflife.org/feed/",
            "category": "international",
            "priority": "medium"
        },
        
        # ========== 政府与监管机构 ==========
        {
            "name": "White House AI",
            "type": "web",
            "url": "https://www.whitehouse.gov/ostp/ai-bill-of-rights/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "EU AI Policy",
            "type": "rss",
            "url": "https://digital-strategy.ec.europa.eu/en/rss.xml",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "US Commerce Dept",
            "type": "web",
            "url": "https://www.commerce.gov/news",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "FTC Tech",
            "type": "rss",
            "url": "https://www.ftc.gov/feeds/press-release-consumer-protection.xml",
            "category": "international",
            "priority": "medium"
        },
        
        # ========== AI公司官方 ==========
        {
            "name": "OpenAI Blog",
            "type": "rss",
            "url": "https://openai.com/blog/rss/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Anthropic",
            "type": "rss",
            "url": "https://www.anthropic.com/feed.xml",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Meta AI",
            "type": "rss",
            "url": "https://ai.meta.com/blog/rss/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Microsoft AI Blog",
            "type": "rss",
            "url": "https://blogs.microsoft.com/ai/feed/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "NVIDIA AI",
            "type": "rss",
            "url": "https://blogs.nvidia.com/feed/",
            "category": "international",
            "priority": "high"
        },
        {
            "name": "Amazon AWS AI",
            "type": "rss",
            "url": "https://aws.amazon.com/blogs/machine-learning/feed/",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "IBM AI",
            "type": "rss",
            "url": "https://www.ibm.com/blogs/research/feed/",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Hugging Face",
            "type": "rss",
            "url": "https://huggingface.co/blog/feed.xml",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Stability AI",
            "type": "web",
            "url": "https://stability.ai/news",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Mistral AI",
            "type": "web",
            "url": "https://mistral.ai/news/",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "xAI",
            "type": "web",
            "url": "https://x.ai/",
            "category": "international",
            "priority": "high"
        },
        
        # ========== 芯片与硬件 ==========
        {
            "name": "AMD AI",
            "type": "rss",
            "url": "https://www.amd.com/en/rss/press-releases.xml",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Intel AI",
            "type": "rss",
            "url": "https://newsroom.intel.com/feed/",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "Qualcomm AI",
            "type": "rss",
            "url": "https://www.qualcomm.com/news/feed",
            "category": "international",
            "priority": "medium"
        },
        
        # ========== 行业分析 ==========
        {
            "name": "Gartner AI",
            "type": "rss",
            "url": "https://www.gartner.com/en/topics/artificial-intelligence/feed",
            "category": "international",
            "priority": "medium"
        },
        {
            "name": "McKinsey AI",
            "type": "rss",
            "url": "https://www.mckinsey.com/featured-insights/artificial-intelligence/rss",
            "category": "international",
            "priority": "medium"
        },
    ]
}

# ==================== 影响力评估关键词权重 ====================
# 用于建立影响力评估模型

IMPACT_KEYWORDS = {
    # ===== 重大政策与法规 (权重最高) =====
    "policy_high": {
        "weight": 100,
        "keywords": [
            # 英文
            "executive order", "presidential order", "federal regulation",
            "sanctions", "export ban", "trade restriction", "chip ban",
            "AI Act", "AI regulation", "AI law", "AI bill", "legislation",
            "antitrust", "investigation", "lawsuit", "penalty", "fine",
            "national security", "CFIUS", "entity list", "blacklist",
            # 中文
            "行政令", "总统令", "制裁", "出口禁令", "贸易限制",
            "芯片禁令", "反制", "反制裁", "国家安全", "实体清单",
            "立法", "法案", "监管", "罚款", "反垄断"
        ]
    },
    
    # ===== 重大产品发布 (权重高) =====
    "product_high": {
        "weight": 90,
        "keywords": [
            # 旗舰产品关键词
            "GPT-5", "GPT-6", "GPT5", "GPT6", "o3", "o4",
            "Gemini 2", "Gemini 3", "Gemini Ultra", "Gemini Pro",
            "Claude 4", "Claude 5", "Opus", "Sonnet",
            "Llama 4", "Llama 5",
            "Grok 3", "Grok 4",
            "Sora", "DALL-E 4", "Midjourney V7",
            # 产品动作
            "launches", "releases", "announces", "unveils", "introduces",
            "officially released", "general availability", "public release",
            "发布", "上线", "开源", "开放", "正式推出", "全面开放",
            # 芯片产品
            "H200", "B100", "B200", "Blackwell", "GB200",
            "MI400", "MI500", "昇腾", "Ascend"
        ]
    },
    
    # ===== 学术突破 (权重高) =====
    "academic_high": {
        "weight": 85,
        "keywords": [
            # 突破性词汇
            "breakthrough", "state-of-the-art", "SOTA", "surpasses",
            "outperforms", "beats", "exceeds", "new record",
            "first ever", "world first", "revolutionary",
            "Nobel", "Turing Award", "breakthrough prize",
            # 重要领域
            "AGI", "artificial general intelligence", "superintelligence",
            "consciousness", "reasoning", "multimodal",
            "突破", "超越", "领先", "首次", "创新", "革命性",
            "诺贝尔", "图灵奖", "通用人工智能"
        ]
    },
    
    # ===== 重大投融资与并购 (权重中高) =====
    "business_high": {
        "weight": 75,
        "keywords": [
            "billion", "B funding", "IPO", "acquisition", "merger",
            "partnership", "strategic investment", "valuation",
            "十亿", "百亿", "融资", "收购", "并购", "合作",
            "估值", "上市", "投资"
        ]
    },
    
    # ===== 安全与伦理 (权重中) =====
    "safety_medium": {
        "weight": 60,
        "keywords": [
            "AI safety", "alignment", "existential risk", "x-risk",
            "deepfake", "misinformation", "bias", "fairness",
            "privacy", "surveillance", "autonomous weapons",
            "AI安全", "对齐", "风险", "伦理", "隐私", "监控"
        ]
    },
    
    # ===== 重要人物动态 (权重中) =====
    "people_medium": {
        "weight": 55,
        "keywords": [
            "Sam Altman", "Elon Musk", "Sundar Pichai", "Satya Nadella",
            "Jensen Huang", "Demis Hassabis", "Dario Amodei",
            "李彦宏", "马化腾", "任正非", "雷军",
            "CEO", "founder", "chief", "leaves", "joins", "appointed"
        ]
    },
    
    # ===== 一般AI新闻 (基础权重) =====
    "general": {
        "weight": 30,
        "keywords": [
            "AI", "artificial intelligence", "machine learning",
            "deep learning", "neural network", "LLM", "large language model",
            "人工智能", "机器学习", "深度学习", "大模型", "大语言模型"
        ]
    }
}

# ==================== 重要来源权重加成 ====================
SOURCE_WEIGHTS = {
    # 顶级来源 (1.5x 加成)
    "tier1": {
        "multiplier": 1.5,
        "sources": [
            "华尔街日报WSJ Tech", "Bloomberg Technology", "Reuters Technology",
            "Financial Times Tech", "MIT Technology Review", "Nature AI",
            "Science Magazine", "OpenAI Blog", "DeepMind Blog", "Google AI Blog",
            "White House AI", "EU AI Policy", "RAND Corporation AI",
            "Stanford HAI", "机器之心", "量子位"
        ]
    },
    # 高级来源 (1.3x 加成)
    "tier2": {
        "multiplier": 1.3,
        "sources": [
            "TechCrunch AI", "The Verge AI", "VentureBeat AI", "Wired AI",
            "The Information", "Anthropic", "Meta AI", "Microsoft AI Blog",
            "NVIDIA AI", "Brookings AI", "CSIS Technology", "36氪", "新智元"
        ]
    },
    # 标准来源 (1.0x)
    "tier3": {
        "multiplier": 1.0,
        "sources": []  # 其他所有来源
    }
}

# ==================== 数据存储路径 ====================
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CSV_FILE = os.path.join(DATA_DIR, "news.csv")
DAILY_DIR = os.path.join(DATA_DIR, "daily")
RAW_DIR = os.path.join(DATA_DIR, "raw")  # 原始数据存储

# ==================== 采集与输出配置 ====================
# 原始采集目标：100+条
MIN_RAW_NEWS_TARGET = 100

# 最终输出配置
MIN_NEWS_PER_CATEGORY = 5   # 每类最少5条
MAX_NEWS_PER_CATEGORY = 20  # 每类最多20条

# 时区配置
TIMEZONE = "Asia/Shanghai"
SCHEDULE_TIME = "16:00"
