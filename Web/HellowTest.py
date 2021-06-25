import unittest
from selenium import webdriver
import time

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
        url = driver.current_url
        title = driver.title
        self.assertEqual(url, "https://dev.deephow.net/", "URL Error")  # 驗證(expected預期在前，actual實際在後)
        self.assertEqual(title, "DeepHow", "Title Error")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)