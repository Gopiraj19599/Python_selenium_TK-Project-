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
chrome.implicitly_wait(10)
chrome.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")


#  send string to the username & password input field
element = chrome.find_element(By.NAME, "username")
element.send_keys("karthikeyan.tealorca@gmail.com")
element = chrome.find_element(By.NAME, "password")
element.send_keys("monkatwork")
chrome.find_element(By.CLASS_NAME,'MuiButton-textSizeMedium').submit()
# navigate to dashboad page


#  *************  select product option and one more click experience over view option from drop down  navigate to "Overview screen" *************

chrome.find_element(By.XPATH,'//*[@id="fuse-layout"]/div/div/div/div/ul/ul[2]/li/div/span').click()
chrome.find_element(By.XPATH,'//*[@id="fuse-layout"]/div/div/div/div/ul/ul[2]/div/div/div/div[2]/a/div/span').click()

time.sleep(5)
chrome.close()
