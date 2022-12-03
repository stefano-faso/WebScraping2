from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.nfl.com/stats/player-stats/').text
soup = BeautifulSoup(html_text,'lxml')
players = soup.find_all('table', class_='d3-o-table d3-o-table--detailed d3-o-player-stats--detailed d3-o-table--sortable')
for player in players:
    data = player.tbody.tr.text.split()
    name = ' '.join(data[0:2])
    print(name)