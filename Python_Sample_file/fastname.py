import unittest
from selenium import webdriver
import time


class OpenTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://autofms.devtest.tk/')


    def testCase(self):
        driver = self.driver
        print(driver.current_url)
        print(driver.title)
        self.assertEqual(driver.title, "autofms 網頁標題 | autofms 導覽列", "網站標題不正確")

        driver.find_element_by_partial_link_text("admin").click()
        time.sleep(1)
        driver.get('http://autofms.devtest.tk/user/admin/info')
        time.sleep(1)

        name = driver.find_element_by_css_selector(".app-user-info>.fs-description:nth-child(1)>dl>dd:nth-child(4)").text
        print(name)
        self.assertEqual(name, "系統管理者", "比對名字不正確")


    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)