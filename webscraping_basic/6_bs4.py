# beautifulsoup 레퍼런스 : https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/

# beautifulsoup4, lxml 설치
# pip3 install beautifulsoup4
# pip3 install lxml

# beautifulsoup4는 스크래핑을 위한 패키지, lxml은 스크래핑한 것을 분석하기 위한 parser

# 네이버 웹툰 스크래핑

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

# 가져온 HTML 문서를 lxml parser를 통해서 BeautifulSoup 객체로 만듬
soup = BeautifulSoup(res.text, "lxml")
# 이를 통해 soup은 모든 정보를 담고 있다.
# print(soup.title)  # soup 객체를 통해서 해당 HTML 엘리먼트들에 접근을 할 수 있다.
# print(soup.title.get_text()) # title 안의 내용만 출력
# print(soup.a) # HTML 엘리먼트들 중 첫 번째 a 태그 내용을 출력
# print(soup.a.attrs) # 첫 번째 a 태그 안에 있는 속성들의 정보를 출력(딕션너리 형태)
# print(soup.a["href"]) # 첫 번째 a 태그의 속성들 중 href의 내용을 출력

# soup 객체에 모든 a 태그들 중에 속성이 "class":"Nbtn_upload"인 것을 출력
# print(soup.find("a", attrs={"class": "Nbtn_upload"}))
# 만약 웹툰 올리기라는 속성이 유일하다면 soup.find(attrs={"class": "Nbtn_upload"})도 가능하다.

# 인기급상승 만화 리스트 중 1위인 만화 제목 가져오기
rank1 = soup.find("li", attrs={"class": "rank01"})
print(rank1.a.get_text())

# 태그 간의 이동은 parent, next_sibling, previous_sibling으로 할 수 있다.
# rank1.parent는 현재 rank1의 상위 태그
# rank1.next_sibling은 현재 rank1의 다음 태그
# rank1.previous_sibling은 현재 rank1의 이전 태그

rank2 = rank1.find_next_sibling("li")  # rank1에서 다음 li 태그를 찾음
print(rank2.a.get_text())
rank1 = rank2.find_previous_sibling("li")  # rank2에서 이전 li 태그를 찾음
print(rank1.a.get_text())

# rank1.find_next_siblings("li")를 통해 rank1의 다음 모든 li 태그 내용을 가져올 수도 있다.

# soup 객체 중 a 태그이고, 텍스트 내용이 소녀의 세계-2부 16화인 정보 출력
webtoon = soup.find("a", text="소녀의 세계-2부 16화")
print(webtoon)
