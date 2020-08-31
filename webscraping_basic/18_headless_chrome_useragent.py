# headless를 사용할 때에는 user-agent 값을 설정을 해주어야 한다.
# 설정해 주지 않으면 해당 사이트에서 headlessChrome 인것을 인지하고 접속을 막을 수도 있기 때문에

# selenium 레퍼런스 : https://selenium-python.readthedocs.io/

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36")

browser = webdriver.Chrome(
    '/Users/hyuk/Desktop/study_webscraping/chromedriver', options=options)
browser.maximize_window

# 페이지 이동
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

# Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6)
# AppleWebKit/537.36 (KHTML, like Gecko)
# Chrome/84.0.4147.135 Safari/537.36

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()
