import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class NewDirectory1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get("http://autofms.devtest.tk/")
        cls.driver.title
        print(cls.driver.current_url)
        print(cls.driver.title)

    def test_Create_Directory(self):
        driver = self.driver
        current_time = time.strftime("%Y/%m/%d/ %H:%M:%S", time.localtime(time.time()))
        driver.find_element_by_link_text("admin").click()
        driver.get("http://autofms.devtest.tk/km/")
        driver.find_element_by_class_name("fs-iconfont").click()
        DO = driver.find_element_by_xpath('//div[@id="xbox-inline"]/div[3]/div[1]/h2/div[1]').text
        print(DO)
        self.assertEqual(DO, "目錄總覽", "目錄總覽名稱不正確")
        driver.find_element_by_xpath('//*[@id="xbox-inline"]/div[3]/div[1]/h2/div[2]/div[2]/span[2]/ul/li[1]/span/a').click()
        driver.find_element_by_xpath('//*[@id="xbox-inline"]/div[3]/div[1]/h2/div[2]/div[2]/span[2]/ul/li[1]/ul/li[1]/a').click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "/html/body")))
        title = driver.find_element_by_name("name")
        title.send_keys(current_time)
        driver.switch_to.frame(0)
        editbox = driver.find_element_by_xpath("/html/body")
        editbox.send_keys("Hello")
        driver.switch_to.parent_frame()
        time.sleep(1)
        driver.find_element_by_css_selector("button[data-role=form-submit]").click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="1236"]/div[1]/span/ul/li[2]/span[2]').click()
        driver.find_element_by_xpath('//*[@id="1236"]/div[1]/span/ul/li[2]/ul/li[4]').click()
        a1 = driver.switch_to.alert
        time.sleep(1)
        print(a1.text)
        a1.dismiss()


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)