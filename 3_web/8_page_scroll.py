import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
# browser.maximize_window()
browser.get('https://shopping.naver.com/home/p/index.naver')

# type '무선마우스'
elem = browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]')
elem.send_keys('무선마우스')
time.sleep(2)
elem.send_keys(Keys.ENTER)
# browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# Scroll to the specified location
browser.execute_script('window.scrollTo(0, 1080)') # 1920 * 1080 모니터 회상도 (x, y) y사이즈 만큼 내리기
browser.execute_script('window.scrollTo(0, 2080)')

# Scroll way to the bottom
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 페이지에 대해서 마지막까지 스크롤 반복 수행
interval = 2 # 2초에 한번씩 스크롤 내리기

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script('return document.body.scrollHeight')

# Repeat
while True:
    #keep scrolling till the bottom
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    
    # Page loading
    time.sleep(interval) # 2 seconds
    
    #현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == prev_height: 
        break #if both heights are the same => no change in height difference (end of the page)
    
    prev_height = curr_height #update the height to recent (to prev_height)
    print('아아아아아아')

# back to top
browser.execute_script('window.scrollTo(0, 0)')

time.sleep(5)
browser.quit()