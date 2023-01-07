import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


options = Options()
options.add_argument("--start-maximized")
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
chrome.get("https://tealorca.com/")
chrome.find_element(By.XPATH,"/html/body/div/section[1]/div/div/div[1]/div/h1").text


chrome.implicitly_wait(0.5)


time.sleep(5)
chrome.close()

