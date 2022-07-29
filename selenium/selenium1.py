import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") # chrome driver 가져오기
browser.get("http://naver.com") # 네이버로 이동

# 로그인 버튼 클릭
element = browser.find_element_by_class_name("link_login")
element.click()

# id, pw 입력
browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("pw").send_keys("my_pswd")

# 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep()

# 아이디 새로 입력
browser.find_element_by_id("id").claer()
browser.find_element_by_id("id").send_keys("new_id")

# html문서 정보 출력
print(browser.page_source)

# 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit() # 모든 탭 종료
