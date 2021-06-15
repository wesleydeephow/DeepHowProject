import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class eesignupCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(600)  #隱式等待600秒
        self.driver.get("http://eeauto.devtest.tk/")

    def test_eesingup(self):
        driver = self.driver
        that_day = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time())) #當天日期時間
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "註冊"))) #顯示等待 30秒內每隔0.5毫秒掃描1次頁面變化
        driver.find_element_by_link_text("註冊").click()
        print(driver.current_url)
        print(driver.title)
        time.sleep(1)
        driver.find_element_by_name("account").send_keys("user" + that_day)
        print(that_day)
        driver.find_element_by_name("fullName").send_keys("使用者" + that_day)
        driver.find_element_by_name("password").send_keys("111111")
        driver.find_element_by_name("password2").send_keys("111111")
        driver.find_element_by_name("email").send_keys("dair370" + "+" + that_day + "@powercam.com.tw")
        driver.find_element_by_xpath('//*[@value="1"]').click()
        #checkboxs = driver.find_elements_by_css_selector('input[type=checkbox]') #將目前所有的CheckBox選取
        #for checkbox in checkboxs:
            #checkbox.click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-primary")))
        driver.find_element_by_class_name("btn-primary").click()
        time.sleep(1)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "fs-infobox-title")))
        text = driver.find_element_by_class_name("fs-infobox-title").text
        print(text)
        self.assertEqual("註冊成功", text, "註冊過程有問題")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)
