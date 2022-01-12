from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult') #frame 전환

# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elem.click()


#selecting through text value
# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
# elem.click()

#when text value is partially similar
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()