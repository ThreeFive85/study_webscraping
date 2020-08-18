'''
웹 사이트에서는 header를 통해 사용자가 어떤 식으로 접근을 하는지 알 수가 있다.
예를 들어 같은 네이버를 접속하였을때 pc에서 접속한 화면과 mobile에서 접속한 화면은 다르다.
이것이 바로 브라우저가 웹 사이트에 접속할 때 주는 header 정보에 따라서 사이트 화면이 변경된다.
하지만 사람이 아니라 프로그램이 접속하여 어떠한 정보를 마구잡이로 긁어오려고 할 때 해당 사이트는 
서버에 부담이 생길 수도 있고, 정보를 빼앗길 수도 있기 때문에 그런 정보를 확인해서 접속을 차단할 수 있다.
웹 스크래핑에서는 user agent를 통해서 차단된 사이트에 접속할 수가 있다.
'''

# import requests
# res = requests.get("https://ThreeFive85.tistory.com")
# res.raise_for_status()
# with open("tistory.html", "w", encoding="utf8") as f:
#     f.write(res.text)

# 현재 위 코드로 해당 사이트를 접속하려고 했을 때는 응답코드 403을 받고 프로그램이 종료된다.

# 자신의 user agent 확인 방법
# 1. google에서 user agent string을 검색한다.
# 2. what is my user agent 제목을 가지는 사이트로 접속한다.
# 3. 파란색 블록으로 표시된 곳을 확인
# 접속하는 브라우저에 따라 자신의 user agent는 다르다는걸 참고

import requests
url = "https://three-five.tistory.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("tistory.html", "w", encoding="utf8") as f:
    f.write(res.text)
