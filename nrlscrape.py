import pandas as pd
import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs


# List of URLs
# Change the season and round number accordingly to which year you prefer
url_list = [
    'https://www.nrl.com/draw/?competition=111&round=1&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=2&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=3&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=4&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=5&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=6&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=8&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=9&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=10&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=11&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=12&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=13&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=14&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=15&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=16&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=17&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=18&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=19&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=20&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=21&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=22&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=23&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=24&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=25&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=26&season=2024',
    'https://www.nrl.com/draw/?competition=111&round=27&season=2024'
]

# Folder path to save HTML files
folder_path = "data"

# Chrome options for headless browsing
chrome_options = Options()
chrome_options.add_argument("--headless")

# Function to extract round number from URL
def extract_round_number(url):
    return url.split('&round=')[1].split('&')[0]

# Function to save HTML file
def save_html_file(html_code, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html_code)

# Loop through URLs
for url in url_list:
    # Extract round number from URL
    round_number = extract_round_number(url)
    
    # Create folder for the round
    round_folder_path = os.path.join(folder_path, f"Round_{round_number}")
    if not os.path.exists(round_folder_path):
        os.makedirs(round_folder_path)
        

    # Check if main page HTML file already exists
    main_page_html_file_path = os.path.join(round_folder_path, "main_page.html")
    if os.path.exists(main_page_html_file_path):
        with open(main_page_html_file_path, 'r', encoding='utf-8') as f:
            main_page_code = f.read()
    else:
        # Use Selenium to load the page and save it as HTML
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(url)
        main_page_code = driver.page_source
        
        # Save the main page HTML
        save_html_file(main_page_code, main_page_html_file_path)
        
        driver.quit()
    
    # Parse the main page with BeautifulSoup
    main_page_soup = bs(main_page_code, 'html.parser')
    
    # Find section container
    section_container = main_page_soup.find(id='draw-content')
    
    # Check if section container exists
    if section_container:
        sections = section_container.find_all('section')[:8]  # Get first 8 sections

        # Loop through sections
        for i, section in enumerate(sections):
            # Find link in section
            a_element = section.find('a', href=True)
            
            # Check if link exists
            if a_element:
                link = urljoin(url, a_element['href'])
                print("Link:", link)
                
                # Create folder for additional page HTML
                additional_page_folder_path = os.path.join(round_folder_path, f"game_{i+1}")
                if not os.path.exists(additional_page_folder_path):
                    os.makedirs(additional_page_folder_path)
                    
                player_stats_folder_path = os.path.join(additional_page_folder_path, f"team_players")
                if not os.path.exists(player_stats_folder_path):
                    os.makedirs(player_stats_folder_path)
                
                team_stats_folder = os.path.join(additional_page_folder_path, f"team_stats")
                if not os.path.exists(team_stats_folder):
                    os.makedirs(team_stats_folder)

                team_list_folder_path = os.path.join(additional_page_folder_path, f"team_list")
                if not os.path.exists(team_list_folder_path):
                    os.makedirs(team_list_folder_path)
                    
                    
                # Check if additional page HTML file already exists
                additional_page_html_file_path = os.path.join(additional_page_folder_path, "match_stats_page.html")
                if os.path.exists(additional_page_html_file_path):
                    with open(additional_page_html_file_path, 'r', encoding='utf-8') as f:
                        additional_page_code = f.read()
                else:
                    # Use Selenium to load the page and save it as HTML
                    driver = webdriver.Chrome(options=chrome_options)
                    driver.get(link)  
                    additional_page_code = driver.page_source  

                    # Save the additional page HTML
                    save_html_file(additional_page_code, additional_page_html_file_path)
                    
                    driver.quit()
                
                # Parse the additional page with BeautifulSoup
                additional_page_soup = bs(additional_page_code, 'html.parser')
                
                # Extracting text from additional page
                team_a_stats = {}
                team_b_stats = {}
                
                match_header = additional_page_soup.find(class_="match-header")
                
                if match_header:
                    round_number_div = match_header.find('p', class_='match-header__title')

                    if round_number_div:
                        print(f"Round Number div found!")

                        match_title = round_number_div.get_text(strip=True)
                        match = re.search(r'Round (\d+)', match_title)

                        if match:
                            figure = match.group(1)
                            team_a_stats['Round_Number'] = figure
                            team_b_stats['Round_Number'] = figure


                    team_a = additional_page_soup.find(class_="match-team--home").find(class_="match-team__name--home").get_text(
                        strip=True)
                    score_home_text = additional_page_soup.find(class_="match-team--home").find(
                        class_="match-team__score--home").get_text(strip=True)
                    score_a = ''.join(filter(str.isdigit, score_home_text))  # Extract digits only

                    # Extracting away team and score
                    team_b = additional_page_soup.find(class_="match-team--away").find(class_="match-team__name--away").get_text(
                        strip=True)
                    score_away_text = additional_page_soup.find(class_="match-team--away").find(
                        class_="match-team__score--away").get_text(strip=True)
                    score_b = ''.join(filter(str.isdigit, score_away_text))  # Extract digits only

                    team_a_stats['Home_Team'] = team_a
                    team_a_stats['Home_Score'] = score_a
                    team_a_stats['Away_Team'] = team_b
                    team_a_stats['Away_Score'] = score_b

                    team_b_stats['Away_Team'] = team_b
                    team_b_stats['Away_Score'] = score_b
                    team_b_stats['Home_Team'] = team_a
                    team_b_stats['Home_Score'] = score_a

                    team_list_div = additional_page_soup.find(
                        class_='l-grid__cell l-grid__cell--100 l-grid__cell--padding-16-at-600 l-grid__cell--padding-24-at-960')
                    if team_list_div:
                        print("team List div found!")

                    if team_list_div:
                        team_list = team_list_div.find_all(class_="team-list__container")
                        if team_list:
                            first_set = team_list[0]
                            second_set = team_list[1]

                            first_set_names = first_set.find_all(class_="team-list-profile__name")
                            second_set_names = second_set.find_all(class_="team-list-profile__name")
                            if first_set_names:
                                players = [re.sub(r'\s+', ' ', name.text.strip()) for name in first_set_names]
                                players.extend([re.sub(r'\s+', ' ', name.text.strip()) for name in second_set_names])

                                team_a_stats['Player'] = players[::2]  # Players at even indices belong to Team A
                                team_b_stats['Player'] = players[1::2]  # Players at odd indices belong to Team B

                                # Create DataFrame
                                team_a_df = pd.DataFrame(team_a_stats)
                                team_b_df = pd.DataFrame(team_b_stats)

                                # Concatenate DataFrames
                                concatenated_df = pd.concat([team_a_df, team_b_df], ignore_index=True)

                                # Save DataFrame to CSV
                                csv_file = os.path.join(team_list_folder_path, f"game_{i+1}_players.csv")
                                if not os.path.exists(csv_file):
                                    concatenated_df.to_csv(csv_file, index=False)
                else:
                    print("No match header found in the second section.")

#---------------TEAM STATISTICS STARTS HERE-------------------------------------------------------------------------------------------------
                team_stats = additional_page_soup.find(id='tabs-match-centre-3')
                if team_stats:
                    print("team FOUnD")
                    team_stats_all_div = team_stats.find_all(class_="u-spacing-mb-24")

                    pos_and_comp_div = team_stats_all_div[0]
                    attack_div = team_stats_all_div[1]
                    passing_div = team_stats_all_div[2]
                    defence_div = team_stats_all_div[4]
                    negative_play_div = team_stats_all_div[5]
                    
                    #-------------NEGATIVE PLAY-----------------------------------
                    if negative_play_div:      
                        print("Negative Play Div Found!")
                        combined_negativeplay_stats = []
                        team_list = []
                        negative_play_inner_div = negative_play_div.find_all(class_='u-display-flex')
                        if negative_play_inner_div:
                            

                            home_np_stats = []
                            away_np_stats = []
                            
                            n1 = negative_play_inner_div[0]
                            n2 = negative_play_inner_div[2]
                            n3 = negative_play_inner_div[4]

                            
                            if len(negative_play_inner_div) >= 7:

                                print("greater than 6")
                                n4 = negative_play_inner_div[6]
                                n4s = re.findall(r'\d+', n4.text.strip())    
                                
                            else:
                                n4s = ['0', '0']
                                print('Less than 6')

                                
                            n1s = re.findall(r'\d+', n1.text.strip())
                            n2s = re.findall(r'\d+', n2.text.strip())
                            n3s = re.findall(r'\d+', n3.text.strip())

                            
                            combined_negativeplay_stats.append(n1s)
                            combined_negativeplay_stats.append(n2s)
                            combined_negativeplay_stats.append(n3s)
                            combined_negativeplay_stats.append(n4s)
                        

                            home_np_stats = [pair[0] for pair in combined_negativeplay_stats]
                            away_np_stats = [pair[1] for pair in combined_negativeplay_stats]
                            
                            combined_negativeplay_stats = home_np_stats + away_np_stats
                            negative_play_df = pd.DataFrame([combined_negativeplay_stats], columns=[
                                'Home_Errors', 'Home_Penalties', 'Home_Ruck_Infrigments', 'Home_Inside_10M',
                                'Away_Errors', 'Away_Penalties', 'Away_Ruck_infrigments', 'Away_Inside_10M',
                                ])

                            csv_file_path = os.path.join(team_stats_folder, f"negative_play_stats_{i+1}.csv")
                            if not os.path.exists(csv_file_path):
                                negative_play_df.to_csv(csv_file_path, index=False)

                    else:
                        print("Negative play div not found")
                    #--------------defence div-----------------------------------------------------
                    if defence_div:
                        print("Defence div found")
                        home_defence_stats = []
                        away_defence_stats = []
                        combined_defence_stast = []
                    
                        effective_tackle_percent = defence_div.find_all(class_='donut-chart-svg__text')

                        if effective_tackle_percent:
                            
                            etp_list = []
                            for i in effective_tackle_percent:
                                etp_list.append(i.text.strip()[:-1])
                            combined_defence_stast.append(etp_list)

                        defence_innder_divs = defence_div.find_all(class_='u-spacing-pb-24 u-spacing-pt-16 u-width-100')

                        if defence_innder_divs:
                            print("innder Divs found!")
    
                            dl = len(defence_innder_divs)
                            
                            combined_defence_stast.append(re.findall(r'\d+', defence_innder_divs[1].text.strip())) 
                            combined_defence_stast.append(re.findall(r'\d+', defence_innder_divs[2].text.strip())) 
                            if dl < 5:
                                print(f"dl less than four")
                                combined_defence_stast.append(re.findall(r'\d+', defence_innder_divs[3].text.strip())) 
                            else:
                                combined_defence_stast.append(re.findall(r'\d+', defence_innder_divs[4].text.strip()))

                
                            home_defence_stats = [pair[0] for pair in combined_defence_stast]
                            away_defence_stats = [pair[1] for pair in combined_defence_stast]
                            
                            combined_defence_stats = home_defence_stats + away_defence_stats

                            defence_stats_df = pd.DataFrame([combined_defence_stats], columns=[
                                'Home_Effective_Tackles %', 'Home_Tackles_Made', 'Home_Missed_Tackles', 'Home_Ineffective_Tackles',
                                'Away_Effective_Tackles %', 'Away_Tackles_Made', 'Away_Missed_Tackles', 'Away_Ineffective_Tackles'
                            ])
                            
                            csv_file_path = os.path.join(team_stats_folder, "defence_stats.csv")
                            if not os.path.exists(csv_file_path):
                                 defence_stats_df.to_csv(csv_file_path, index=False)
                    else:
                        print("Defence div not found")
                    #-------------------PASSING STATS---------------------------------------------------------
                    if passing_div:
                        print("Passing div found")
                        home_pass_stats = []
                        away_pass_stast = []

                        passing_inner_divs = passing_div.find_all(class_='u-display-flex')
                        if passing_inner_divs:
                            c1 = passing_inner_divs[0]
                            c2 = passing_inner_divs[2]
                            c3 = passing_inner_divs[4]
                            c4 = passing_inner_divs[6]

                            attack_list = []

                            v = re.findall(r'\d+', c1.text.strip())
                            v2 = re.findall(r'\d+', c2.text.strip())
                            v3 = re.findall(r'\d+', c3.text.strip())
                            v4 = re.findall(r'\d+', c4.text.strip())

                            attack_list.append(v)
                            attack_list.append(v2)
                            attack_list.append(v3)
                            attack_list.append(v4)
                            

                            home_pass_stats = [pair[0] for pair in attack_list]
                            away_pass_stats = [pair[1] for pair in attack_list]
                            

                            combined_pass_stats = home_pass_stats + away_pass_stats
                            passing_stats_df = pd.DataFrame([combined_pass_stats], columns=[
                                'Home_Offloads', 'Home_Receipts', 'Home_Total_Passes', 'Home_Dummy_Passes',
                                'Away_Offloads', 'Away_Receipts', 'Away_Total_Passes', 'Away_Dummy_Passes'
                            ])
                            
                            csv_file_path = os.path.join(team_stats_folder, "passing_stats.csv")
                            if not os.path.exists(csv_file_path):
                                passing_stats_df.to_csv(csv_file_path, index=False)

                        
                    else:
                        print("Passing div not found")
  
                    #--------------ATTACK STATS---------------------------------------------------------------
                    if attack_div:
                        print("attack div found")
                        home_attack_stats = []
                        away_attack_stats = []

                        all_attack_child = attack_div.find_all('div', class_='u-spacing-pb-24 u-spacing-pt-16 u-width-100')

                        x = all_attack_child[0].findChildren()
                        x2 = all_attack_child[1].findChildren()
                        x3 = all_attack_child[2].findChildren()
                        x4 = all_attack_child[3].findChildren()
                        x5 = all_attack_child[4].findChildren()
                        x6 = all_attack_child[5].findChildren()
                        x7 = all_attack_child[6].findChildren()
                        x8 = all_attack_child[7].findChildren()

                    
                        home_attack_stats.append(x[5].text.strip())
                        home_attack_stats.append(x2[5].text.strip())
                        home_attack_stats.append(x3[5].text.strip())
                        home_attack_stats.append(x4[5].text.strip())
                        home_attack_stats.append(x5[5].text.strip())
                        home_attack_stats.append(x6[5].text.strip())
                        home_attack_stats.append(x7[5].text.strip())
                        home_attack_stats.append(x8[13].text.strip())
                        
                        away_attack_stats.append(x[13].text.strip())
                        away_attack_stats.append(x2[13].text.strip())
                        away_attack_stats.append(x3[13].text.strip())
                        
                        try:
                            away_attack_stats.append(x4[13].text.strip())
                        except IndexError:
                            away_attack_stats.append(0)
                        
                        
                        away_attack_stats.append(x5[13].text.strip())
                        away_attack_stats.append(x6[13].text.strip())
                        away_attack_stats.append(x7[13].text.strip())
                        away_attack_stats.append(x8[16].text.strip()[:-1])

                        combined_attacked_stats = home_attack_stats + away_attack_stats
                        attack_stats_df = pd.DataFrame([combined_attacked_stats], columns=[
                            'Home_All_Runs', 'Home_All_Run_Meters', 'Home_Post_Contact_Meters', 'Home_Line_Breaks',
                            'Home_Tackle_Breaks', 'Home_Average_Distance', 'Home_Kick_Return_Meters', 'Home_Average_Ball_Play_Speed',
                            'Away_All_Runs', 'Away_All_Run_Meters', 'Away_Post_Contact_Meters', 'Away_Line_Breaks',
                            'Away_Tackle_Breaks', 'Away_Average_Distance', 'Away_Kick_Return_Meters', 'Away_Average_Ball_Play_Speed'
                        ])
                        
                        csv_file_path = os.path.join(team_stats_folder, "attack_stats.csv")
                        if not os.path.exists(csv_file_path):
                            attack_stats_df.to_csv(csv_file_path, index=False)

                        
                    else:
                        print("attack div not found")
                    
                    #--------------------POSSESION AND COMPLETION STATS---------------------------------------------
                    if pos_and_comp_div:
                        print("Possesion and completion div found")
                        pos_and_comp_list = []
                        home_pnc = []
                        away_pnc = []

                        pos_and_comp_inner_divs = pos_and_comp_div.find_all(class_='u-spacing-pb-24 u-spacing-pt-16 u-width-100')
                        if pos_and_comp_inner_divs:
                            pc1 = pos_and_comp_inner_divs[0]
                            pc2 = pos_and_comp_inner_divs[1]
                            pc3 = pos_and_comp_inner_divs[2]
                            
                            if pc3:
                                print('pc3 found!')

                            home_team_percentage = pc1.find('p', class_='match-centre-card-donut__value--home').get_text(strip=True)[:-1]
                            away_team_percentage = pc1.find('p', class_='match-centre-card-donut__value--away').get_text(strip=True)[:-1]
                            pos_and_comp_list.append(home_team_percentage)
                            pos_and_comp_list.append(away_team_percentage)
                            
                            home_team_time = pc2.find('dd', class_='stats-bar-chart__label--home').get_text(strip=True)
                            away_team_time = pc2.find('dd', class_='stats-bar-chart__label--away').get_text(strip=True)
                            pos_and_comp_list.append(home_team_time)
                            pos_and_comp_list.append(away_team_time)
                            
                            
                            home_percent = pc3.find_all('div', class_='match-centre-card-donut')[0].find('span', class_='').get_text(strip=True)[:-1]

                            
                            away_percent = pc3.find_all('div', class_='match-centre-card-donut')[1].find('span', class_='').get_text(strip=True)


                            pos_and_comp_list.append(home_percent)
                            pos_and_comp_list.append(away_percent)
                            split_lists = [pos_and_comp_list[i:i+2] for i in range(0, len(pos_and_comp_list), 2)]

                            home_pnc = [pair[1] for pair in split_lists]
                            away_pnc = [pair[0] for pair in split_lists]
                            
                            combined_pnc_stats = home_pnc + away_pnc
                            posseion_n_completion_df = pd.DataFrame([combined_pnc_stats], columns=[
                                'Home_Possesion', 'Home_Time_Possesion', 'Home_Completion_Rate',
                                'Away_Possesion', 'Away_Time_Possesion', 'Away_Completion_Rate',
                            ])
                            
                            csv_file_path = os.path.join(team_stats_folder, "pos_n_comp_stats.csv")
                            if not os.path.exists(csv_file_path):
                                posseion_n_completion_df.to_csv(csv_file_path, index=False)

                            
                    else:
                        print("Possesion and completion div not found")
                        
                player_stats = additional_page_soup.find('div', id='player-stats')
                if player_stats:
                    print("Player Stats Found")
                    player_tables = []
                    tables = player_stats.find_all(class_='table table--max-cell-width-100 table--base u-text-align-center')
                    if tables:
                        print("Tables FOund!")
                        player_tables.append(tables[0])
                        player_tables.append(tables[1])
                        table_count = 1
                        
                        for tb in player_tables:
                            theads = tb.find('thead').findChildren(recursive=False)[1]
                            headers = []
                            for th in theads.find_all('th'):
                                headers.append(th.text.strip())

                            filtered_list = list(filter(lambda item: item.strip(), headers))
                            
                            data = []
                            
                            # Initialize a counter
                            row_count = 0

                            for tr in tb.find_all('tr'):
                                row = []
                                for td in tr.find_all('td'):
                                    # Extract text data from the cell without stripping whitespace
                                    cell_text = re.sub(r'\s+', ' ', td.get_text()).strip()  # Replace multiple whitespaces with a single space
                                    row.append(cell_text)

                                # Append the row to data list
                                if row:
                                    # Find the full name cell and extract the full name
                                    full_name_cell = tr.find('td', class_='table__cell table__cell--fixed table-tbody__td table-tbody__td--player-name')
                                    if full_name_cell:
                                        full_name = full_name_cell.find('a').text.strip() + ' ' + full_name_cell.find('span').text.strip()
                                        row.append(full_name)
                                    data.append(row)
                                    
                                    # Increment the row count
                                    row_count += 1
                                    if row_count == 13:
                                        break
                                    
                                    # Break the loop if 13 rows have been processed
                            tdf = pd.DataFrame(data, columns=headers)
                            
                            tb_name = f"team_{table_count}_players.csv"
                            table_count+=1
                            
                            csv_file_path = os.path.join(player_stats_folder_path, tb_name)
                            if not os.path.exists(csv_file_path):
                                tdf.to_csv(csv_file_path, index=False)
                            
                            print("Check table")

                               
                                                                 
 
                
                    
                       

                    
