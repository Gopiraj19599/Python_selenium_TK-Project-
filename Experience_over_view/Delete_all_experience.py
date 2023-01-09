import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


# Try to login  on  Chrome  browser
options = Options()
options.add_argument("--start-maximized")
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
chrome.implicitly_wait(10)
chrome.get("https://travelkit-mvp.boopalankrishnan02.workers.dev/login")


#  send string to the username & password input field
element = chrome.find_element(By.NAME, "username")
element.send_keys("karthikeyan.tealorca@gmail.com")
# element.send_keys("gopiraj.tealorca@gmail.com")
element = chrome.find_element(By.NAME, "password")
element.send_keys("monkatwork")
chrome.find_element(By.CLASS_NAME,'MuiButton-textSizeMedium').submit()
# navigate to dashboad page

# click the Product botton on actove bar
chrome.find_element(By.XPATH,"//span[normalize-space()='Products']").click()
#  click the drop down option (Experince overview)
chrome.find_element(By.XPATH,"//span[normalize-space()='Experiences Overview']").click()
# The list of experiences is not properly listed: Experience Overview screen 



delete = chrome.find_elements(By.XPATH,"//*[contains(@id,'MUIDataTableBodyRow-')]/td[5]/div/div/button[2]")





# delete = chrome.find_elements(By.XPATH,"//*[contains(@id,'MUIDataTableBodyRow-')]/td[5]/div/div/button[2]")



while True:
    chrome.refresh()
    delete = chrome.find_elements(By.XPATH,"//*[contains(@id,'MUIDataTableBodyRow-')]/td[5]/div/div/button[2]")
    if(len(delete) != 0):
        for i in range(len(delete)):
            chrome.find_element(By.XPATH,"//*[contains(@id,'MUIDataTableBodyRow-')]/td[5]/div/div/button[2]").click()
            chrome.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[2]/button[2]").click()
            time.sleep(4)
    else:
        print("deleted all experiecse")
        break

time.sleep(5)
chrome.close()

