# 웹 스크래핑으로 가져온 정보를 csv 형태로 저장해보기
# 네이버 금융 사용해서 코스피 시가 총액 순위

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
# newline=""은 한 줄 띄우고 줄바꿈을 방지
# 혹시 엑셀 파일을 열었는데 한글이 깨진다면 encoding="utf-8-sig"로 변경
f = open(filename, "w", encoding="utf8", newline="")
writer = csv.writer(f)

title = "N 종목명 현재가 전일비 등락률 액면가 시가총액 상장주식수 외국인비율 거래량 PER ROE".split(" ")
# print(type(title))
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class": "type_2"}).find(
        "tbody").find_all("tr")
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1:  # 의미 없는 데이터는 skip
            continue
        data = [column.get_text().strip() for column in columns]
        # .get_text().strip()은 불필요한 문자열 제거 ex) \n\n\t\t100\n\t\t와 같은 문자열
        # print(data)
        writer.writerow(data)  # 리스트 형태로 넣어주어야한다. 현재 data는 리스트
