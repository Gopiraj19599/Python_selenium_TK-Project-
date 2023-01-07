# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://travelkit-mvp.boopalankrishnan02.workers.dev/login')


time.sleep(5)
driver.close()