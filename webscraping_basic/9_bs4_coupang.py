# 쿠팡 사이트에서 광고 상품을 제외한 노트북 상품들을 스크래핑 하기

import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&\
channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&\
minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&\
brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(res.text)
items = soup.find_all("li", attrs={"class": re.compile("^search-product")})
# print(items[0].find("div", attrs={"class": "name"}).get_text())
for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class": "ad-badge-text"})
    if ad_badge:
        print(" <광고 상품은 제외합니다>")
        continue

    name = item.find("div", attrs={"class": "name"}).get_text()  # 제품명
    # 특정 회사 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다>")
        continue

    price = item.find(
        "strong", attrs={"class": "price-value"}).get_text()  # 가격

    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
    rate = item.find("em", attrs={"class": "rating"})  # 평점
    # 제품 중 평점이 없는 것도 있다.
    if rate:
        rate = rate.get_text()
    else:
        # rate = "평점 없음"
        print(" <평점 없는 상품 제외합니다>")
        continue

    rate_cnt = item.find(
        "span", attrs={"class": "rating-total-count"})
    if rate_cnt:
        rate_cnt = rate_cnt.get_text()[1:-1]  # ex) (30)라서 슬라이싱을 해줌
    else:
        rate_cnt = "평점 갯수 없음"

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)
