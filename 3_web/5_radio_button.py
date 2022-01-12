import time
from selenium import webdriver

browser = webdriver.Chrome()
# browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult') #frame 전환

elem = browser.find_element_by_xpath('//*[@id="html"]') #with the above frame id, i can locate this xPath

#if not selected, select
if elem.is_selected() == False:
    print("not selected")
    elem.click()
else:
    print("already selected")
    
time.sleep(5)

browser.quit()