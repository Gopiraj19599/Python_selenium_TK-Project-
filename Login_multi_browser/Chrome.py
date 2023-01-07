import time
from selenium import webdriver
from selenium.webdriver.common.by import By



# Try to login  on  Chrome  browser

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
options.add_argument("--start-maximized")
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
chrome.implicitly_wait(10)
chrome.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")


#  send string to the username & password input field

element = chrome.find_element(By.NAME, "username")
element.send_keys("gopiraj.tealorca@gmail.com")
element = chrome.find_element(By.NAME, "password")
element.send_keys("monkatwork")
chrome.find_element(By.CLASS_NAME,'MuiButton-textSizeMedium').submit()


# login to Dashboad 





time.sleep(5)
chrome.close()