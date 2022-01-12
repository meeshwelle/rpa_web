import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tag_input.asp')
curr_handle = browser.current_window_handle
print(curr_handle) # Current Windows handle info

# Try it Yourself
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

handles = browser.window_handles # All of handle informations
for handle in handles:
    print(handle)
    browser.switch_to.window(handle) # Switch to each handle
    print(browser.title) # Print current handle (browser)'s Title
    print()

# 새로 이동된 브라우저에서 뭔가 자동화 작업을 수행...
time.sleep(5)

# 그 브라우저를 종료
print('Exiting current handle')
browser.close()

# Return to previous handle
print('returning to original handle')
browser.switch_to.window(curr_handle)

print(browser.title)

# Check for browser controlling
time.sleep(3)
browser.get('https://google.com')

time.sleep(5)
browser.quit()