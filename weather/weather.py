from bs4 import BeautifulSoup
import requests

seoul = requests.get('https://search.naver.com/search.naver?query=강남+날씨')

se_soup = BeautifulSoup(seoul.text, 'html.parser')


se_now = se_soup.find('div', {'class' : 'temperature_text'}).text.strip()
se_we = se_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
print(se_now + " " +se_we)
se_today = se_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
print(se_today)
se_tomorow = se_soup.find('li', {'class': 'week_item holiday today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
print(se_tomorow)
