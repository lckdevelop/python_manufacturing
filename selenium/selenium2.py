from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time

browser = webdriver.Chrome()
browser.maximize_window() # 창 키우기

url = "https://flight.naver.com/flights"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 오는 날 선택 클릭
browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

# 제주도 클릭
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

try:
    element = WebDriverWait(browser, 10).until(ec.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[3]")))
    print(element.text)
finally:
    browser.quit()





