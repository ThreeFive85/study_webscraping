import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# 해당 페이지에 모든 만화 제목들을 가져오기
cartoons = soup.find_all("a", attrs={"class": "title"})
for cartoon in cartoons:
    print(cartoon.get_text())
