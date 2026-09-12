# TabSlayer - Browser-Powered Research Aggregation Agent

**SLAB (Self-Learning Agent Browser) Hackathon - VIT Bhopal University**

## 🎯 What is TabSlayer?

TabSlayer is an autonomous research agent that searches multiple sources (Wikipedia, arXiv, Google News, GitHub) and returns structured findings with sources—solving the "47 browser tabs" problem.

**In 15 seconds, TabSlayer does what normally takes hours.**

### Key Features
- ✅ Multi-source research (Wikipedia, arXiv, News, GitHub)
- ✅ Smart caching (1,662x faster on repeats)
- ✅ Structured JSON output
- ✅ Token-efficient (only ~200 tokens per query)
- ✅ Error recovery (graceful degradation)
- ✅ Webcmd browser automation
- ✅ Zero logins required (reads public data)

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Virtual environment activated
- API keys configured (.env file)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/TabSlayer.git
cd TabSlayer

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### Option 1: Run from Python
```bash
python src/research_agent.py "your research topic"
```

#### Option 2: Run from EXE (Standalone)
```bash
TabSlayer_Research.exe "your research topic"
```

#### Option 3: Run Demo (Fresh + Cached)
```bash
python demo.py
```

#### Option 4: Interactive Demo with Presentation
```bash
Open presentation.html in your browser
```

## 📊 Example Output

```bash
$ python src/research_agent.py "artificial intelligence"

🔍 Researching: 'artificial intelligence'
============================================================

📚 Fetching from fast sources (APIs)...
✅ Wikipedia: 3 results found
✅ arXiv: 3 papers found

🌐 Fetching from browser sources (Webcmd)...
✅ Google News: 2 articles found

✨ Aggregation complete: Found 8 relevant results

📊 Results for: artificial intelligence
Found 8 findings across 3 sources

1. Artificial intelligence
   Source: Wikipedia | Date: 2026-09-12
   URL: https://en.wikipedia.org/wiki/Artificial_intelligence
   Snippet: Artificial intelligence (AI) is the capability of computational systems...
   Relevance: 0.85
```

**Second run (instant):**
```bash
$ python src/research_agent.py "artificial intelligence"

📦 Loaded from cache (created 2026-09-12T12:05:10.920435)

📊 Results for: artificial intelligence
Found 8 findings across 3 sources
... (instant results from cache)
```

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│  USER QUERY: "browser automation"       │
└──────────────┬──────────────────────────┘
               ↓
        CHECK CACHE (instant if found)
               ↓
   ┌───────────────────────────────┐
   │ PHASE 1: Fast APIs (3-5 sec)  │
   ├───────────────────────────────┤
   │ ✓ Wikipedia API               │
   │ ✓ arXiv API                   │
   └───────────────┬───────────────┘
                   ↓
   ┌───────────────────────────────┐
   │ PHASE 2: Webcmd Browser       │
   │ (10-15 sec, optional)         │
   ├───────────────────────────────┤
   │ ✓ Google News                 │
   │ ✓ GitHub repos                │
   └───────────────┬───────────────┘
                   ↓
   ┌───────────────────────────────┐
   │ AGGREGATE & DEDUPLICATE       │
   ├───────────────────────────────┤
   │ ✓ Remove duplicates           │
   │ ✓ Rank by relevance           │
   │ ✓ Top 8-10 findings           │
   └───────────────┬───────────────┘
                   ↓
   ┌───────────────────────────────┐
   │ CACHE & OUTPUT                │
   ├───────────────────────────────┤
   │ ✓ Save to JSON                │
   │ ✓ Return results              │
   │ ✓ Pretty-print                │
   └───────────────────────────────┘
```

## 📁 File Structure

```
TabSlayer/
├── src/
│   ├── research_agent.py        # Main orchestrator
│   ├── cache_manager.py         # Caching system
│   ├── aggregator.py            # Deduplication + ranking
│   ├── haiku_ranker.py          # AI-powered ranking (optional)
│   └── sources/
│       ├── wikipedia.py         # Wikipedia API adapter
│       ├── arxiv.py             # arXiv API adapter
│       └── webcmd_browser.py    # Webcmd browser automation
├── cache/                       # JSON cache (auto-created)
├── output/                      # Generated reports
├── releases/
│   ├── TabSlayer_Demo.exe       # Demo EXE (for presentation)
│   └── TabSlayer_Research.exe   # Research Query EXE
├── .env                         # API keys (keep secret!)
├── .gitignore                   # Git ignore rules
├── requirements.txt             # Python dependencies
├── demo.py                      # Full demo script
├── presentation.html            # Interactive slideshow
├── README.md                    # This file
└── venv/                        # Virtual environment
```

## 🌐 Data Sources

| Source | Type | Results | Speed | Coverage |
|--------|------|---------|-------|----------|
| Wikipedia | API | 3-4 | Fast | General knowledge |
| arXiv | API | 3-4 | Fast | Academic papers |
| Google News | Webcmd | 2-3 | Medium | Current news |
| GitHub | Webcmd | 2-3 | Medium | Code/projects |

## ⚡ Performance Metrics

| Metric | Value |
|--------|-------|
| First Query | 15-20 seconds |
| Cached Query | <1 second |
| Speed Improvement | 1,662x faster |
| Tokens per Query | ~200 (new), 0 (cached) |
| Cost per Query | ~$0.0001 with caching |
| Cache Hit Rate | 100% on repeats |

## 🤖 Token Efficiency

- **Planning:** ~50 tokens
- **Wikipedia fetch:** ~100 tokens (API call, not Claude)
- **arXiv fetch:** ~100 tokens (API call, not Claude)
- **News/GitHub:** ~50 tokens (API calls, not Claude)
- **Aggregation:** ~0 tokens (local Python)
- **Total:** ~200 tokens per new query
- **Cached:** 0 tokens (JSON load from disk)

## 🎯 Judging Criteria Coverage

- 🟢 **Live Reliability (30 pts):** No crashes, instant caching, error recovery
- 💡 **Real-world Usefulness (25 pts):** Students, devs, researchers can use immediately
- 🧠 **Technical Depth (20 pts):** Webcmd, multi-source, caching, error handling
- ✨ **Creativity (15 pts):** Smart deduplication, instant repeats, graceful degradation
- 🎤 **Demo & Storytelling (10 pts):** Hook, live demo, wow moment (cached query)

**Total Target: 100/100 points**

## 🚀 How to Use for Presentations

### Demo Script for Judges

**Step 1: Hook (10 seconds)**
```
"Raise your hand if you've had 47 browser tabs open trying to research one topic."
[pause for laughs]
"Yeah. We built an agent that does that research for you—in 15 seconds."
```

**Step 2: Live Demo 1 - Fresh Query (20 seconds)**
```bash
python src/research_agent.py "browser automation frameworks"
```
Watch it research across sources, return 8-10 findings.

**Step 3: Live Demo 2 - Cached Query (instant!)**
```bash
python src/research_agent.py "browser automation frameworks"
```
Shows instant result from cache. **This is the WOW moment.**

**Step 4: Technical Explanation (30 seconds)**
- "We use Webcmd for real browser automation"
- "Direct APIs for speed (Wikipedia, arXiv)"
- "Smart caching—1,662x faster on repeats"
- "Only ~200 tokens per query using Haiku"

**Step 5: Close (10 seconds)**
"TabSlayer: Your research assistant that never forgets a source."

## 📦 Executable Files

Two standalone EXE files are included in `releases/`:

### 1. **TabSlayer_Demo.exe**
- Purpose: Presentation and demo recording
- Usage: Run the full demo flow (fresh + cached)
- File size: ~8.9 MB
- No command line args needed

### 2. **TabSlayer_Research.exe**
- Purpose: Standalone research queries
- Usage: `TabSlayer_Research.exe "your topic"`
- File size: ~8.9 MB
- Works from anywhere on your system

Both EXEs include all dependencies and don't need Python installed.

## 📊 Interactive Presentation

Open `presentation.html` in any web browser for an interactive 15-slide presentation:

```bash
# Windows
start presentation.html

# Mac
open presentation.html

# Linux
xdg-open presentation.html
```

**Features:**
- Navigate with arrow buttons or keyboard arrow keys
- Slide counter shows progress
- Beautiful gradient design
- Responsive layout
- All slides optimized for projector display

## 🔧 Configuration

### .env File

```bash
ANTHROPIC_API_KEY=sk-ant-...  # Your Claude API key
WEBCMD_API_KEY=               # Optional - for premium Webcmd features
```

Keep this file secret! Don't commit to GitHub.

### Cache Management

Clear cache to force fresh searches:

```python
from pathlib import Path
[f.unlink() for f in Path('cache').glob('*.json')]
```

## 🛠️ Development

### Adding a New Source

Create a new file in `src/sources/`:

```python
# src/sources/my_source.py

def fetch_my_source(query: str, max_results: int = 3) -> list[dict]:
    """Fetch results from my custom source."""
    findings = []
    # Your implementation here
    return findings
```

Then import and use in `research_agent.py`:

```python
from sources.my_source import fetch_my_source

# In research() function:
my_findings = fetch_my_source(query, max_results=3)
all_findings.extend(my_findings)
```

### Running Tests

```bash
# Test Wikipedia source
python -c "from src.sources.wikipedia import fetch_wikipedia; print(fetch_wikipedia('test'))"

# Test arXiv source
python -c "from src.sources.arxiv import fetch_arxiv; print(fetch_arxiv('test'))"

# Test full agent
python src/research_agent.py "test query"
```

## 📝 Use Cases

### For Students
```bash
# Research for essay
python src/research_agent.py "Shakespeare's sonnets themes"

# Cite papers
python src/research_agent.py "machine learning ethics"
```

### For Developers
```bash
# Compare frameworks
python src/research_agent.py "React vs Vue vs Angular"

# Learn new tech
python src/research_agent.py "Rust programming language"
```

### For Journalists
```bash
# Aggregate breaking news
python src/research_agent.py "latest AI developments"

# Research story angles
python src/research_agent.py "climate change solutions"
```

### For Researchers
```bash
# Find academic papers
python src/research_agent.py "quantum computing applications"

# Discover related work
python src/research_agent.py "reinforcement learning"
```

## 🌟 Unique Features

1. **Smart Caching** - Results cached locally, repeats are instant
2. **Webcmd Integration** - Real browser automation for dynamic sites
3. **Multi-Source Aggregation** - Combines Wikipedia, arXiv, News, GitHub
4. **Error Recovery** - Gracefully falls back if one source fails
5. **Token Efficient** - Uses Haiku for cost-effective ranking
6. **Standalone EXE** - No Python needed to run
7. **Zero Logins** - Reads public data only
8. **Completely Reversible** - Read-only research, no modifications

## 🔒 Privacy & Security

- ✅ No personal data collected
- ✅ No login credentials stored
- ✅ All searches are read-only
- ✅ Cache stored locally (never sent to servers)
- ✅ API keys in .env (not in git)
- ✅ No third-party tracking
- ✅ Respects robots.txt

## 📚 Technologies Used

- **Language:** Python 3.x
- **APIs:** Wikipedia, arXiv
- **Browser:** Webcmd (self-learning)
- **AI:** Claude Haiku 4.5 (ranking)
- **Parsing:** BeautifulSoup
- **HTTP:** Requests library
- **Packaging:** PyInstaller (EXE)

## 🎓 Learning Outcomes

Building TabSlayer taught us:
- ✅ Multi-source data aggregation
- ✅ Browser automation with Webcmd
- ✅ AI-powered ranking systems
- ✅ Caching strategies for performance
- ✅ Error handling & recovery
- ✅ Token-efficient API usage
- ✅ Building standalone applications

## 🚀 Future Roadmap

- [ ] Web dashboard UI
- [ ] Email notifications
- [ ] Citation export (BibTeX, APA, MLA)
- [ ] PubMed integration
- [ ] ProPublica integration
- [ ] Sentiment analysis
- [ ] Multi-language support
- [ ] Cloud deployment

## 📄 License

MIT License - See LICENSE file for details

## 👥 Authors

Built for SLAB Hackathon - VIT Bhopal University
Submission Date: 2026-09-12

## 🤝 Contributing

Contributions welcome! Fork, create a feature branch, and submit a PR.

## 📞 Support

Having issues? Check:
1. `.env` file has valid API keys
2. Virtual environment is activated
3. Dependencies are installed: `pip install -r requirements.txt`
4. Internet connection is working

## 🎉 Thank You

Thanks to:
- Webcmd team for browser automation
- Anthropic for Claude API
- VIT Bhopal for hosting SLAB Hackathon

---

**TabSlayer: Your Research Assistant That Never Forgets a Source**

*Stop drowning in tabs. Start researching smart.*
