#import requests library
import requests
#imports the lxml parser
from lxml import html


from bs4 import BeautifulSoup

website_root = "https://fbref.com"
result = requests.get("https://fbref.com/en/comps/8/2012-2013/2012-2013-Champions-League-Stats")
src = result.content

soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")

matchup_divs = soup.find_all("div", class_="matchup")

# final-match-lists
final_divs = ""
final_matches = []

# semi-final-match-lists
semi_finals_divs = ""
semi_final_matches = []

#quarter-final-match-lists
quarter_finals_divs = ""
quarter_final_matches = []

# playoff-match-lists
playoff_divs = ""
playoff_matches = []


# final-link-parser
if len(matchup_divs) >= 2:
    final_divs = matchup_divs[0]
else:
    print("There are fewer than 2 instances of divs with the class 'matchup'.")

final_match_divs = final_divs.find_all("div", class_="match-detail")

for div in final_match_divs:
    list = div.find_all("a")
    for item in list:
        href_value = item.get('href')
        final_matches.append(href_value)

# semi-final-link-parser
if len(matchup_divs) >= 2:
    semi_finals_divs = matchup_divs[1]
else:
    print("There are fewer than 2 instances of divs with the class 'matchup'.")

semi_final_match_divs = semi_finals_divs.find_all("div", class_="matches")

for div in semi_final_match_divs:
    list = div.find_all("a")
    for item in list:
        href_value = item.get('href')
        semi_final_matches.append(href_value)

# quarter-final-link-parser
if len(matchup_divs) >= 2:
    quarter_finals_divs = matchup_divs[2]
else:
    print("There are fewer than 2 instances of divs with the class 'matchup'.")

quarter_final_match_divs = quarter_finals_divs.find_all("div", class_="matches")

for div in quarter_final_match_divs:
    list = div.find_all("a")
    for item in list:
        href_value = item.get('href')
        quarter_final_matches.append(href_value)

# playoff-link-parser
if len(matchup_divs) >= 2:
    playoff_divs = matchup_divs[3]
else:
    print("There are fewer than 2 instances of divs with the class 'matchup'.")

playoff_match_divs = playoff_divs.find_all("div", class_="matches")

for div in playoff_match_divs:
    list = div.find_all("a")
    for item in list:
        href_value = item.get('href')
        playoff_matches.append(href_value)


print(len(final_matches))
print(len(semi_final_matches))
print(len(quarter_final_matches))
print(len(playoff_matches))
