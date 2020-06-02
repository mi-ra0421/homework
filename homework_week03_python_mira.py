
import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

#제목경로 : body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis 
#rank 경로: body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number

for song in songs :
    a_tag = song.select_one('td.info > a.title.ellipsis')
    if a_tag is not None:
        rank =song.select_one('td.number').text  
        title = a_tag.text  
        artist = song.select_one('td.info > a.artist.ellipsis').text                     
        print(a_tag.text)



 
        