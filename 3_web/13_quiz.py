import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/')

# Click Learn HTML
browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[1]/a[1]').click()
time.sleep(2)

# Click How To
browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()
time.sleep(3)

# Select Contact Form on left
# browser.find_element_by_link_text('Contact Form').click()
browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()
# browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[contains(text(), "Contact")]').click()

#Input Form
fname = browser.find_element_by_id('fname').send_keys('Mich')

lname = browser.find_element_by_id('lname')
lname.send_keys('Lee')

country = "Canada"
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
# browser.find_element_by_name('country').click()
# country = browser.find_element_by_xpath('//*[@id="country"]/option[2]').click()

# Write sth in Subject
subject = browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea')
subject.send_keys('Finished the Quiz')
time.sleep(5)

# Submit
browser.find_element_by_link_text('Submit').click()
time.sleep(5)

browser.quit()