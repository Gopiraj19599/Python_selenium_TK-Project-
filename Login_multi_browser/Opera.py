# selenium 3 & 4
import time
from selenium import webdriver
from webdriver_manager.opera import OperaDriverManager

driver = webdriver.Chrome(executable_path=OperaDriverManager().install())

driver.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")
time.sleep(5)
driver.close()