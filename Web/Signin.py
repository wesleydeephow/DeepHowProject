import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SigninCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(100)  #隱式等待10秒
        self.driver.get("https://dev.deephow.net/")

    def test_singin(self):
        driver = self.driver
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input'))) #顯示等待
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input').send_keys("wesley.chen+root@deephow.com")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        driver.find_element_by_class_name("v-btn__content").click()
        acct = driver.find_element_by_class_name("log-in-title").text
        print(acct)
        self.assertEqual(acct, "你好, Wesley.Chen+root!", "acct Error") #驗證(expected預期在前，actual實際在後)
        time.sleep(2)
        driver.find_element_by_class_name("back-btn").click()
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        driver.find_element_by_class_name("v-btn__content").click()
        acct = driver.find_element_by_class_name("log-in-title").text
        print(acct)
        self.assertEqual(acct, "你好, Wesley.Chen+root!", "acct Error") #驗證(expected預期在前，actual實際在後)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input').send_keys("Pa$$w0rd")
        time.sleep(2)
        driver.find_element_by_class_name("v-btn__content").click()
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-avatar")))
        driver.find_element_by_class_name("v-avatar").click()
        time.sleep(2)
        name = driver.find_element_by_class_name("text-xs-center").text
        email = driver.find_element_by_class_name("email-id-text").text
        print(name)
        print(email)
        self.assertEqual(name, "R管理者", "Name Error") #驗證(expected預期在前，actual實際在後)
        self.assertEqual(email, "wesley.chen+root@deephow.com", "email Error") #驗證(expected預期在前，actual實際在後)
        time.sleep(2)
        driver.find_element_by_class_name("logout-text").click()
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)