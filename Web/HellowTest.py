import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HellowTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(600)  #隱式等待60秒
        self.driver.get("https://dev.deephow.net/")

    def test_HellowTest(self):
        driver = self.driver
        print(driver.current_url)
        print(driver.title)
        time.sleep(3)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)