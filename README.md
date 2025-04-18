🏉 NRL Sports Stats Scraper
This Python script scrapes detailed NRL game stats from NRL.com and saves them into well-organized CSV files per game, round, and season. It uses Selenium to handle dynamic content and BeautifulSoup for parsing.

🗂 Output Directory Structure
After running the script, a directory like data-2024-R1-12 will be created with this structure:

kotlin
Copy
Edit
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
Each round contains multiple games, each with team lists, player stats, team stats, and the original match stats HTML page for backup.

✅ Requirements
Python 3.7+

Good internet connection

Google Chrome browser

Chrome WebDriver (matching your Chrome version)

📦 Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/nrl-stats-scraper.git
cd nrl-stats-scraper
2. Create and Activate a Virtual Environment
bash
Copy
Edit
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
4. Install Chrome WebDriver
This script uses Selenium, which requires Chrome WebDriver to automate browsing.

How to install:
Check your Chrome version:

Open Chrome and go to chrome://settings/help

Download the matching WebDriver:

https://sites.google.com/chromium.org/driver/

Add it to your system’s PATH, or provide its path in the script if necessary.

📄 Running the Script
Make sure you are connected to the internet, and simply run:

bash
Copy
Edit
python main.py
You’ll be prompted to enter:

Start and end round numbers

Year of the season

The script will then:

Visit each game’s page

Download and parse stats

Save them in structured folders

🧾 requirements.txt Contents
Include the following:

nginx
Copy
Edit
beautifulsoup4
pandas
requests
selenium
To generate this file, you can also run:

bash
Copy
Edit
pip freeze > requirements.txt
📝 Notes
Match data is fetched live, so ensure stable internet for optimal performance.

HTML files are saved in each game folder for data verification or future reference.

Works best with updated Chrome and compatible WebDriver.

📄 License
MIT License – use and modify freely.
