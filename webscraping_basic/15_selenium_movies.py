# 구글 무비 인기 차트 리스트

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "ko-kr,ko"
}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class": "ImZGtf mpg5gc"})
print(len(movies))

with open("movies.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())

for movie in movies:
    title = movie.find("div", attrs={"class": "WsMG1c nnK0zc"}).get_text()
    print(title)

# 위 코드에서는 Beautifulsoup을 통해서 무비 제목 10개들을 가져올 수 있지만 구글 페이지는 동적 페이지이기 때문에
# 스크롤을 내릴수록 더 많은 영화들이 나온다. 이를 해결하기 위해서는 selenium을 사용하여야 한다.
