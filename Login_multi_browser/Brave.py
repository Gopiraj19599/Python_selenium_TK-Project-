
# selenium 4
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as BraveService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType

driver = webdriver.Chrome(service=BraveService(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()))
driver.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")
time.sleep(5)
driver.close()
