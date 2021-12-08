from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


name = "testing-admin"
password = "testing-admin"

link = "https://portal-staging.advcloud.ru/campaigns"
#USER_EMAIL = (By.CSS_SELECTOR, "#mail")
#USER_PASS = (By.CSS_SELECTOR, "#password")
#LOGIN_BTN = (By.CSS_SELECTOR, ".Auth-module_FormButton_33oas1VJ77STNXmaFXNJMN")

browser = webdriver.Chrome()
browser.get(link)
browser.maximize_window()


input1 = browser.find_element_by_css_selector("#mail")
input1.send_keys(name)
input2 = browser.find_element_by_css_selector("#password")
input2.send_keys(password)
input3 = browser.find_element_by_css_selector(".Auth-module_FormButton_33oas1VJ77STNXmaFXNJMN")
input3.click()

time.sleep(4)
input4 = browser.find_element_by_css_selector("#main_content > div > header > div.Header-module_AdvertiserContainer_1lE9tNxbfGG-eKaFRDnRJY > div > div > div.css-1wy0on6.react-select__indicators > div > i")
input4.click()
time.sleep(2)
input5 = browser.find_element_by_css_selector("#react-select-3-input")
time.sleep(1)
input5.click()
time.sleep(1)
input5.send_keys("Rec")
time.sleep(1)
input5.send_keys(Keys.ENTER)
time.sleep(4)

input6 = browser.find_element_by_css_selector("#main_content > div > header > div.Header-module_User_2Rj6kcRxQQedhnZXdlrqWG > div > img")
input6.click()
time.sleep(1)
input7 = browser.find_element_by_css_selector("#main_content > div > header > div.Header-module_User_2Rj6kcRxQQedhnZXdlrqWG > ul > li:nth-child(1) > a")
input7.click()
time.sleep(2)
input8 = browser.find_element_by_css_selector("#main_content > div > main > div > aside > ul > li:nth-child(5) > a")
input8.click()
time.sleep(5)
#browser.execute_script("window.scrollBy(0, document.body.scrollHeight);")

time.sleep(1)
#browser.execute_script("window.scrollBy(300, 0);")

link = browser.find_element_by_css_selector("#react-tabs-1 > div > div:nth-child(3) > div > button")
browser.execute_script("return arguments[0].scrollIntoView(true);", link)
link.click()
time.sleep(1)

