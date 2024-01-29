from bs4 import BeautifulSoup
import requests

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find_all('div', class_='tit3')

for idx, movie in enumerate(movie_list):
    print('{}위: {}'.format(idx + 1, movie.text.strip()))
