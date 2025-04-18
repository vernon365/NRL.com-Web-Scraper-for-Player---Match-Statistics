# 🏉 **NRL Stats Scraper**

A powerful web scraping script that extracts team and player statistics from NRL match pages using **Selenium** and **BeautifulSoup**. Data is saved in structured **CSV files** for every match, round, and season.

---

## 📁 **Folder Structure**

Example output:

```
data-2024-R1-12/
└── Round_1/
    └── game_1/
        ├── team_list/
        │   └── game_1_players.csv
        ├── team_players/
        │   ├── team_1_players.csv
        │   └── team_2_players.csv
        ├── team_stats/
        │   ├── attack_stats.csv
        │   ├── defence_stats.csv
        │   ├── negative_play_stats.csv
        │   ├── passing_stats.csv
        │   └── pos_n_comp_stats.csv
        └── match_stats_page.html
```

---

## 🚀 **How to Use**

### 🔁 **Clone the Repository**

```bash
git clone https://github.com/your-username/nrl-stats-scraper.git
cd nrl-stats-scraper
```

---

### 💻 **Create a Virtual Environment**

```bash
python -m venv venv
```

---

### ⚙️ **Activate the Virtual Environment**

```bash
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

---

### 📦 **Install Requirements**

```bash
pip install -r requirements.txt
```

---

### 🌐 **Download Chrome WebDriver**

> Required for Selenium to control your Chrome browser.

- Download it from: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
- Match the driver version with your installed Chrome version.
- Add it to your **system PATH** or keep it in the **project folder**.

---

## ⚠️ **Requirements**

- 🐍 Python 3.8 or above installed
- 📶 Good internet speed is required to fetch all pages smoothly
- ✅ Install dependencies from `requirements.txt`



## 🧠 **How It Works**

1. The script scrapes stats for all matches in a range of NRL rounds and seasons.
2. For each season, a folder like `data-2024-R1-12` is created.
3. Inside, each round has its own folder like `Round_1`, `Round_2`, etc.
4. Each match folder contains:
   - `team_list/game_1_players.csv`
   - `team_players/team_1_players.csv`, `team_2_players.csv`
   - `team_stats/*.csv` for various stats:
     - `attack_stats.csv`
     - `defence_stats.csv`
     - `negative_play_stats.csv`
     - `passing_stats.csv`
     - `pos_n_comp_stats.csv`
   - `match_stats_page.html` (original HTML snapshot of the match page)

---

## 📄 **License**

**MIT License** – Use, share, and modify freely.
