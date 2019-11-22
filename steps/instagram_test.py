from selenium import webdriver

import time

browser = webdriver.Chrome()

browser.get("https://www.instagram.com")
# //*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a (instagam`in xpath)

time.sleep(5)
Signin = browser.find_element_by_xpath("//*[@id='react-root']/section/main/article/div[2]/div[2]/p/a")
Signin.click()
time.sleep(5)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("xxxxxxx")
password.send_keys("xxxxxx")

time.sleep(5)

login = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/div/div[1]/div/form/div[4]")
login.click()
time.sleep(10)

browser.close()

