# daum에서 인기 영화 이미지들 가져오기

import requests
from bs4 import BeautifulSoup


# 2015년부터 2019년까지의 인기 영화 이미지 받기
for year in range(2015, 2020):

    url = f"https://search.daum.net/search?w=tot&q={year}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"):  # image_url이 //으로 시작을 한다면
            image_url = "https:" + image_url

        # print(image_url)
        # 받은 image_url로 접속해서 페이지 정보를 파일로 저장
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open(f"{year}move{idx + 1}.jpg", "wb") as f:
            f.write(image_res.content)  # image_res가 가지고 있는 content 정보를 쓰기

        # 상위 5개의 영화 이미지만 파일로 저장
        if idx >= 4:
            break
