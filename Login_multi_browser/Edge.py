# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://travelkit-mvp.boopalankrishnan02.workers.dev/login')

time.sleep(4)
driver.close()