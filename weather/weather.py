from bs4 import BeautifulSoup
import requests

seoul = requests.get('https://search.naver.com/search.naver?query=강남+날씨')
gyeon = requests.get('https://search.naver.com/search.naver?query=수원+날씨')
gangwon = requests.get('https://search.naver.com/search.naver?query=강원도+날씨')

se_soup = BeautifulSoup(seoul.text, 'html.parser')
gy_soup = BeautifulSoup(gyeon.text, 'html.parser')
ga_soup = BeautifulSoup(gangwon.text, 'html.parser')

se_now = se_soup.find('div', {'class' : 'temperature_text'}).text.strip()
se_we = se_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
print(se_now + " " +se_we)
se_today = se_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
print(se_today)
se_tomorow = se_soup.find('li', {'class': 'week_item holiday today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
print(se_tomorow)


gy_now = gy_soup.find('div', {'class' : 'temperature_text'}).text.strip()
gy_we = gy_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
gy_today = gy_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
gy_tomorow = gy_soup.find('li', {'class': 'week_item holiday today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
print(gy_now + " " +gy_we)
print(gy_today)
print(gy_tomorow)

ga_now = ga_soup.find('div', {'class' : 'temperature_text'}).text.strip()
ga_we = ga_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
ga_today = ga_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
ga_tomorow = ga_soup.find('li', {'class': 'week_item holiday today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
print(ga_now + " " +ga_we)
print(ga_today)
print(ga_tomorow)