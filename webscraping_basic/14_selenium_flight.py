# 네이버 항공권 스크래핑

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    '/Users/hyuk/Desktop/study_webscraping/chromedriver')
browser.maximize_window()  # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click()  # [0] -> 이번달

# 이번달 27일, 다음달 28일 선택
browser.find_elements_by_link_text("27")[0].click()  # [0] -> 이번달
browser.find_elements_by_link_text("28")[1].click()  # [0] -> 다음달

# 제주도 선택
browser.find_element_by_xpath(
    "//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 항공권을 검색하면서 로딩 시간이 있다. 그래서 로딩 시간을 기다려주는 작업이 필요하다.
# webDriverWait를 통해서 브라우저를 10초동안 기다리는데 해당 xpath가 나타나면 후속 작업을 한다. 10초가 넘으면 에러 발생
# 에러가 발생하면 그 뒤 작업은 의미가 없기때문에 일반적으로는 try구문을 사용한다.
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located(
        (By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행
    print(elem.text)  # 첫번째 결과 출력
finally:
    browser.quit()
