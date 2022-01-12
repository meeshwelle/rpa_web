import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

browser.get('https://flight.naver.com/')

#Departing Day
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
# browser.find_element_by_link_text('30')[0].click()
time.sleep(2)

# Select day
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[3]/td[4]/button/b').click()
time.sleep(2)

#Arriving Day
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[4]/td[4]/button/b').click()

#Arriving Location
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()

# Type Location
browser.find_element_by_class_name('autocomplete_input__1vVkF').click()
time.sleep(2)

elem = browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[1]/div/input')
time.sleep(2)
elem.send_keys('yvr')
time.sleep(3)

browser.find_element_by_class_name('autocomplete_search_item__2WRSw').click()
browser.implicitly_wait(5)

#항공권 검색 click
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/button/span').click()
time.sleep(20)

# Select the first flight
# Solution 1:
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[3]/div[1]/div/div[1]')))
    print(elem.text)
except:
    print("Fail")

# Solution 2
# select_first_flight = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div[1]/div[4]/div/div[3]/div[1]/div')))
# print(select_first_flight.text)

elem.click()
browser.quit()