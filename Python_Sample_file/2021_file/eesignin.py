import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class eesigninCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(600)  #隱式等待60秒
        self.driver.get("https://eetest.powercam.com.tw/")

    def test_eesingin(self):
        driver = self.driver
        print(driver.current_url)
        print(driver.title)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "登入"))) #顯示等待 30秒內每隔0.5毫秒掃描1次頁面變化
        driver.find_element_by_partial_link_text ("登入").click()
        print(driver.title)
        driver.find_element_by_name("account").send_keys("admin")
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_class_name("btn-primary").click()
        print(driver.title)
        root = driver.find_element_by_partial_link_text("系統管理者").text
        print(root)
        self.assertEqual("系統管理者",root,"管理者姓名錯誤") #驗證(expected在前，actual在後)
        time.sleep(2)
        driver.find_element_by_partial_link_text("登出").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)