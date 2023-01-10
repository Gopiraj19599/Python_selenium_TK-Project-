import HtmlTestRunner
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager



class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(10)

    


    def title_test(self):
        print('three')
    


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/tealorca/Authomation/Python_selenium_TK/Html_Report'))