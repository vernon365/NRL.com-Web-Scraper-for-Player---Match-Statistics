# 🏉 NRL Stats Scraper

A powerful web scraping script that extracts team and player statistics from NRL match pages using Selenium and BeautifulSoup. Data is structured in CSV format for each match, round, and season.

---

#📁 Folder Structure

Example output:

- `data-2024-R1-12`
  - `Round_1`
    - `game_1`
      - `team_list`
        - `game_1_players.csv`
      - `team_players`
        - `team_1_players.csv`
        - `team_2_players.csv`
      - `team_stats`
        - `attack_stats.csv`
        - `defence_stats.csv`
        - `negative_play_stats.csv`
        - `passing_stats.csv`
        - `pos_n_comp_stats.csv`
      - `match_stats_page.html`

---

#🚀 How to Use

#Clone the Repository

```bash
git clone https://github.com/your-username/nrl-stats-scraper.git
cd nrl-stats-scraper
#Create a Virtual Environment

python -m venv venv
#Activate the Virtual Environment


# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
#Install Requirements


pip install -r requirements.txt
#Download Chrome WebDriver

Required for Selenium to control your Chrome browser.

Get it from: https://chromedriver.chromium.org/downloads

Match the driver version with your installed Chrome version.

Add it to system PATH or keep it in the project folder.
