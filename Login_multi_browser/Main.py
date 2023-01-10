# Test case
# 1. User can able to open to chrome
# 2. User can able to open the site on Edge browser
# 3. User can able to open the site on Firefox browser
# 4. User can able to open the site on chrome browser with incognito mode



import time
from selenium import webdriver
from selenium.webdriver.common.by import By



# Try to login  on  Chrome  browser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
options = Options()
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
chrome.implicitly_wait(10)
chrome.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")
element = chrome.find_element(By.NAME, "username")
element.send_keys("gopiraj.tealorca@gmail.com")
element = chrome.find_element(By.NAME, "password")
element.send_keys("monkatwork")
chrome.find_element(By.CLASS_NAME,'MuiButton-textSizeMedium').submit()




#    Trying to login incognito mode on chrome
c = webdriver.ChromeOptions()
c.add_argument("--incognito")
incognito = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=c)
incognito.implicitly_wait(10)
incognito.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")
element = incognito.find_element(By.NAME, "username")
element.send_keys("gopiraj.tealorca@gmail.com")
element = incognito.find_element(By.NAME, "password")
element.send_keys("monkatwork")
incognito.find_element(By.CLASS_NAME,'MuiButton-textSizeMedium').submit() 





# Open Firefox browser 
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
firefox.implicitly_wait(10)
firefox.get('https://travelkit-mvp.boopalankrishnan02.workers.dev/login')
element = firefox.find_element(By.NAME, "username")
element.send_keys("gopiraj.tealorca@gmail.com")
element = firefox.find_element(By.NAME, "password")
element.send_keys("monkatwork")
firefox.find_element(By.CLASS_NAME,'MuiButton-textSizeMedium').submit()





# Open Edge Browser
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
edge.implicitly_wait(10)
edge.get('https://travelkit-mvp.boopalankrishnan02.workers.dev/login')
element = edge.find_element(By.NAME, "username")
element.send_keys("gopiraj.tealorca@gmail.com")
element = edge.find_element(By.NAME, "password")
element.send_keys("monkatwork")
edge.find_element(By.CLASS_NAME,'MuiButton-textSizeMedium').submit()




time.sleep(10)
chrome.close()
firefox.close()
edge.close()



