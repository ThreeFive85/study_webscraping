# 웹 스크래핑은 웹에서 원하는 정보를 추출하려는 행위이다.
# 그러기 위해서는 원하는 HTML 문서 정보가 필요하다.
# 원하는 정보를 가져오기 위해서 requests라는 라이브러리가 필요하다.
# 설치는 pip3 install requests 로 설치를 한다.

import requests
# res = requests.get("https://google.com")
# # 해당 웹 페이지의 응답코드를 알고 싶다면
# print("응답코드 :", res.status_code)  # 200이면 정상

# if res.status_code == requests.codes.ok:  # 응답코드가 200이면
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드 {0}]".format(res.status_code))

# 위와 같이 if문을 통해 정보를 잘 가져오는지를 확인할 수도 있지만
# raise_for_status()를 주로 사용한다.
# 정보를 잘 가져왔을 때는 이후 스크래핑을 계속 진행하고 아닌 경우에는 에러를 내고 프로그램을 종료한다.
# res.raise_for_status()

# 그래서 항상 쌍으로 쓴다고 이해하면 될거 같다.
res = requests.get("https://google.com")
res.raise_for_status()

print(len(res.text))  # 가져온 페이지 속 글자 수

# res.text는 터미널 상에서 알아보기 힘들어서 파일로 만들어 볼 수도 있다.
with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
