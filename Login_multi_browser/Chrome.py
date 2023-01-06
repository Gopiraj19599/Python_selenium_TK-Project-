# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome#incognito parameter passed(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")
time.sleep(5)
driver.close()



# Open  incognito  mode
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
c = webdriver.ChromeOptions()
c.add_argument("--incognito")
incognito = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=c)
incognito.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")









