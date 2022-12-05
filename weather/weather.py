from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    print('### 오늘의 날씨')
    print('1.서울, 2.경기, 3.강원, 4.충남, 5.충북, 6.경남, 7.경북, 8.전남, 9.전북, 10.제주')
    
    while True:
        k = input('원하는 지역을 번호로 입력하세요 >> ') 
        if k == '1':
            seoul = requests.get('https://search.naver.com/search.naver?query=강남+날씨')
            se_soup = BeautifulSoup(seoul.text, 'html.parser')
            se_now = se_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            se_we = se_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            se_today = se_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'cell_temperature'}).text.strip()
 #           print('### 오늘의 날씨')
            print()
            print(f'* **{se_now} | {se_we}**')
            print(f'* {se_today}')
        elif k == '2':
            gyeon = requests.get('https://search.naver.com/search.naver?query=수원+날씨')
            gy_soup = BeautifulSoup(gyeon.text, 'html.parser')
            gy_now = gy_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            gy_we = gy_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            gy_today = gy_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
  #          print('### 오늘의 날씨')
            print()
            print(f'* **{gy_now} | {gy_we}**')
            print(f'* {gy_today}')
        elif k == '3':
            gangwon = requests.get('https://search.naver.com/search.naver?query=강원도+날씨')
            ga_soup = BeautifulSoup(gangwon.text, 'html.parser')
            ga_now = ga_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            ga_we = ga_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            ga_today = ga_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
   #         print('### 오늘의 날씨')
            print()
            print(f'* **{ga_now} | {ga_we}**')
            print(f'* {ga_today}')
        elif k == '4':
            chnam = requests.get('https://search.naver.com/search.naver?query=충청남도+날씨')
            cn_soup = BeautifulSoup(chnam.text, 'html.parser')
            cn_now = cn_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            cn_we = cn_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            cn_today = cn_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
    #        print('### 오늘의 날씨')
            print()
            print(f'* **{cn_now} | {cn_we}**')
            print(f'* {cn_today}')
        elif k == '5':
            chbuk = requests.get('https://search.naver.com/search.naver?query=충청북도+날씨')
            cb_soup = BeautifulSoup(chbuk.text, 'html.parser')
            cb_now = cb_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            cb_we = cb_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            cb_today = cb_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
#            print('### 오늘의 날씨')
            print()
            print(f'* **{cb_now} | {cb_we}**')
            print(f'* {cb_today}')
        elif k == '6':
            gynam = requests.get('https://search.naver.com/search.naver?query=경남+날씨')
            gn_soup = BeautifulSoup(gynam.text, 'html.parser')
            gn_now = gn_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            gn_we = gn_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            gn_today = gn_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
     #       print('### 오늘의 날씨')
            print()
            print(f'* **{gn_now} | {gn_we}**')
            print(f'* {gn_today}')
        elif k == '7':
            gybuk = requests.get('https://search.naver.com/search.naver?query=경북+날씨')
            gb_soup = BeautifulSoup(gybuk.text, 'html.parser')
            gb_now = gb_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            gb_we = gb_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            gb_today = gb_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
     #       print('### 오늘의 날씨')
            print()
            print(f'* **{gb_now} | {gb_we}**')
            print(f'* {gb_today}')
        elif k == '8':
            junam = requests.get('https://search.naver.com/search.naver?query=전북+날씨')
            jn_soup = BeautifulSoup(junam.text, 'html.parser')
            jn_now = jn_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            jn_we = jn_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            jn_today = jn_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
     #       print('### 오늘의 날씨')
            print()
            print(f'* **{jn_now} | {jn_we}**')
            print(f'* {jn_today}')
        elif k == '9':
            jubuk = requests.get('https://search.naver.com/search.naver?query=전남+날씨')
            jb_soup = BeautifulSoup(jubuk.text, 'html.parser')
            jb_now = jb_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            jb_we = jb_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            jb_today = jb_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
      #      print('### 오늘의 날씨')
            print()
            print(f'* **{jb_now} | {jb_we}**')
            print(f'* {jb_today}')
        elif k == '10':
            jeju = requests.get('https://search.naver.com/search.naver?query=제주+날씨')
            je_soup = BeautifulSoup(jeju.text, 'html.parser')
            je_now = je_soup.find('div', {'class' : 'temperature_text'}).text.strip()
            je_we = je_soup.find('span', {'class' : 'weather before_slash'}).text.strip()
            je_today = je_soup.find('li', {'class': 'week_item today'}).find('div', {'class':'day_data'}).find('div', {'class':'cell_temperature'}).text.strip()
       #     print('### 오늘의 날씨')
            print()
            print(f'* **{je_now} | {je_we}**')
            print(f'* {je_today}')
        else:
            print('* # 잘못된 번호 입니다.')
            print('### 올바른 번호를 입력하세요')
            
        





