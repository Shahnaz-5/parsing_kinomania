import requests
from bs4 import BeautifulSoup
import pandas as pd
def collect_user_rates(user_login):
   page_num = 1
   data = []
   while True:
      url = f'https://www.kinomania.net/viewer/{user_login}/movies/~{page_num}'
      html_content = requests.get(url).text
      soup = BeautifulSoup(html_content, 'lxml')
      entries = soup.find_all('div', class_='row')
      if len(entries) == 0:  # Признак остановки
         break
      for entry in entries:
         td_film_details = entry.find('td', class_='movie')
         film_name = td_film_details.find('a').text
         release_date = soup.find('span', class_='link-gray')
         date =release_date.text.strip()
         data.append({'film_name': film_name, 'date': date,})
      page_num+= 1
   return data

user_rates = collect_user_rates(user_login='Justmariya')
df = pd.DataFrame(user_rates)
df.to_excel('kinomaniya1_rates.xlsx')