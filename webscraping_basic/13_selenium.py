# pip3 install selenium 으로 셀레니움 설치
# 현재 PC에 설치되어 있는 버전과 호환이 되는 크롬드라이버 설치
# 크롬 주소창에서 chrome://version 으로 확인
# https://chromedriver.chromium.org/downloads 에서 버전에 맞는 크롬드라이버 다운
# 해당 폴더에 압축해제

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # Keys.ENTER와 같은 기능을 사용하기 위해 필요

browser = webdriver.Chrome(
    '/Users/hyuk/Desktop/study_webscraping/chromedriver')
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")  # 로그인 엘리먼트로 이동
elem.click()  # 해서 클릭

# id, pw 입력
# browser.find_element_by_id("id").send_keys("kaje0god@naver.com")
# # browser.find_element_by_id("id").clear()는 id 엘리먼트에 입력되어있는 것을 지워준다.
# browser.find_element_by_id("pw").send_keys("qkrtjdxo1")
# # 로그인 버튼 클릭
# browser.find_element_by_id("log.login").click()
# 위 17번에서 22번사이의 코드로 실행했을때는 자동입력방지때문에 로그인에 문제가 생겼다. 그래서 밑의 코드로 활성

id = '아이디'
pw = '비밀번호'
browser.execute_script(
    "document.getElementsByName('id')[0].value=\'" + id + "\'")

browser.execute_script(
    "document.getElementsByName('pw')[0].value=\'" + pw + "\'")

browser.find_element_by_id("log.login").click()


# browser.back() # 이전 페이지로 이동
# browser.forward() # 다음 페이지로 이동
# browser.refresh() # 새로고침

# 네이버 창에서 검색어를 입력하고 엔터까지
# elem = browser.find_element_by_id("query")
# elem.send_keys("월드오브워크래프트")
# elem.send_keys(Keys.ENTER)

# 태그 가져오기
# elem = browser.find_element_by_tag_name("a")
# 태그들 가져오기
# elem = browser.find_elements_by_tag_name("a")
# for e in elem: # a태그들에 해당하는 속성들 중 href를 출력
#     e.get_atrribute("href")

# browser.close() # 현재 탭만 종료
# browser.quit() # 전체 브라우저 종료
