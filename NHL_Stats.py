from bs4 import BeautifulSoup
import requests
import pandas as pd

column_names = ['Team','Year','Wins','Losses','OT_Losses','Win%','Goals_For','Goals_Against','Difference']
df = pd.DataFrame(columns=column_names)


def find_teams(html):
    soup = BeautifulSoup(html_text, 'lxml')
    teams = soup.find_all('tr', class_='team')
    for item, team in enumerate(teams):
        # try excepts are for class_ where can be 'success' or 'danger'
        try:
            win_pct = team.find('td', class_='pct text-success').text.replace(' ', '').replace('\n', '')
        except:
            win_pct = team.find('td', class_='pct text-danger').text.replace(' ', '').replace('\n', '')
        try:
            dif = team.find('td', class_='diff text-success').text.replace(' ', '').replace('\n', '')
        except:
            dif = team.find('td', class_='diff text-danger').text.replace(' ', '').replace('\n', '')
        name = team.find('td', class_='name').text.replace('  ', '').replace('\n', '')
        year = team.find('td', class_='year').text.replace(' ', '').replace('\n', '')
        wins = team.find('td', class_='wins').text.replace(' ', '').replace('\n', '')
        losses = team.find('td', class_='losses').text.replace(' ', '').replace('\n', '')
        ot_losses = team.find('td', class_='ot-losses').text.replace(' ', '').replace('\n', '')
        if ot_losses == '':
            ot_losses = 0
        gf = team.find('td', class_='gf').text.replace(' ', '').replace('\n', '')
        ga = team.find('td', class_='ga').text.replace(' ', '').replace('\n', '')
        df.loc[len(df.index)] = [name,year,wins,losses,ot_losses,win_pct,gf,ga,dif]


if __name__ == '__main__':
    # Hard coded number of pages
    # uses loop to scrape all info from each page
    for page in range(1, 25):
        html_text = requests.get(f'https://www.scrapethissite.com/pages/forms/?page_num={page}').text
        find_teams(html_text,)
    print(df.head())
    print(df.describe())
