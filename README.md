# 🏉 NRL Stats Scraper

A powerful web scraping script that extracts team and player statistics from NRL match pages using Selenium and BeautifulSoup.  
Data is structured in CSV format for each match, round, and season.

---

## 📁 Folder Structure

Example output:

```
data-2024-R1-12/
├── Round_1/
│   └── game_1/
│       ├── team_list/
│       │   └── game_1_players.csv
│       ├── team_players/
│       │   ├── team_1_players.csv
│       │   └── team_2_players.csv
│       ├── team_stats/
│       │   ├── attack_stats.csv
│       │   ├── defence_stats.csv
│       │   ├── negative_play_stats.csv
│       │   ├── passing_stats.csv
│       │   └── pos_n_comp_stats.csv
│       └── match_stats_page.html
```

---

## 🚀 How to Use

### 🔁 Clone the Repository

```bash
git clone https://github.com/vernon365/NRL.com-Web-Scraper-for-Player---Match-Statistics.git
cd NRL.com-Web-Scraper-for-Player---Match-Statistics
```

### 🧪 Create a Virtual Environment

```bash
python -m venv venv
```

### ✅ Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 📦 Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🌐 Download Chrome WebDriver

This script uses **Selenium** to automate Chrome.  
You’ll need the correct Chrome WebDriver:

- Download from: https://chromedriver.chromium.org/downloads
- Match the driver version to your Chrome browser version.
- Add it to your system `PATH` or place it inside the project folder.

---

## 🌍 Set Which Seasons and Rounds to Scrape

You can customize which NRL season and round(s) to scrape by modifying the `url_list` in the script.

Here’s an example of how to scrape rounds 1 to 27 of the 2024 season:

```python
url_list = [
    'https://www.nrl.com/draw/?competition=111&round=1&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=2&season=2024',
    ...
    'https://www.nrl.com/draw/?competition=111&round=27&season=2024'
]
```

You can edit this list to include only the rounds/seasons you want.

---

## ⚠️ Requirements

- Python 3.8+
- Good internet speed (script loads dynamic web pages)
- Chrome browser installed
- Chrome WebDriver installed

---

## 🪪 License

**MIT License** – free to use, modify, and distribute.

---

Made with ❤️ for NRL stat nerds.
