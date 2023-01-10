# Test Case
# 1. Login chrome broser  navigate to dashboad page
# 3. select product option and one more click experience over view option from drop down 
# 4. select "Creare Experience" Button
# 5. navigate to "Title nad type screen" nad put the title and proguct code and slect check box finaly submit the form


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# ****************************       Login chrome broser  navigate to dashboad page      ********************************


# Try to login  on  Chrome  browser
options = Options()
options.add_argument("--start-maximized")
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
chrome.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")
chrome.implicitly_wait(10)

#  send string to the username & password input field
element = chrome.find_element(By.NAME, "username")
element.send_keys("karthikeyan.tealorca@gmail.com")
element = chrome.find_element(By.NAME, "password")
element.send_keys("monkatwork")
chrome.find_element(By.CLASS_NAME,'MuiButton-textSizeMedium').submit()
# navigate to dashboad page
chrome.implicitly_wait(3)

#  *************  select product option and one more click experience over view option from drop down  navigate to "Overview screen" *************

chrome.find_element(By.XPATH,'//*[@id="fuse-layout"]/div/div/div/div/ul/ul[2]/li/div/span').click()
chrome.implicitly_wait(3)
chrome.find_element(By.XPATH,'//*[@id="fuse-layout"]/div/div/div/div/ul/ul[2]/div/div/div/div[2]/a/div/span').click()
chrome.implicitly_wait(3)
chrome.find_element(By.XPATH,'//*[@id="fuse-main"]/div/div/div[2]/div/div/div[1]/div/header/div/button').click()
chrome.implicitly_wait(3)


#  put the title,product code and selct checkbox and submit 
# Title 
chrome.find_element(By.NAME,"title").send_keys('Title of this experience')
# Product code
chrome.find_element(By.NAME,"experience_code").send_keys('ABC')
# radio buttoon
chrome.find_element(By.XPATH,'//*[@id="fuse-main"]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[4]/div/div[2]/label/span[1]/input').click()
#  check bix
chrome.find_element(By.XPATH,'/html/body/div[1]/div/div/main/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[5]/label[2]/span/span[1]/input').click()
#  submit button
chrome.find_element(By.XPATH,'//*[@id="fuse-main"]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[6]/button').submit()
chrome.implicitly_wait(3)


#  Durations screen
chrome.find_element(By.XPATH,'//*[@id="fuse-main"]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[1]/div[1]/label/span[1]/input').click()
chrome.find_element(By.XPATH,'/html/body/div/div/div/main/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[1]/div[1]/div[1]/div/input').send_keys(4)
chrome.find_element(By.XPATH,'//*[@id="fuse-main"]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[2]/button[2]').submit()
chrome.implicitly_wait(3)


#  Recurrence  screen

chrome.find_element(By.XPATH,'//*[@id="fuse-main"]/div/div/div[2]/div/div[2]/div[1]/div/div/div/form/div[2]/button[2]').submit()



time.sleep(5)
chrome.close()