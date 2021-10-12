import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TeamJoinCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(100)  #隱式等待100秒
        self.driver.get("https://dev.deephow.net/")
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input'))) #顯示等待
        self.driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input').send_keys("wesley.chen+root@deephow.com")
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        self.driver.find_element_by_class_name("v-btn__content").click()
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input'))) #顯示等待
        self.driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input').send_keys("Pa$$w0rd")
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        self.driver.find_element_by_class_name("v-btn__content").click()

    def test_teamjoin(self):
        driver = self.driver
        #current_time = time.strftime("%Y/%m/%d/ %H:%M:%S", time.localtime(time.time()))
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "tool-bar-icon")))
        driver.find_element_by_class_name("tool-bar-icon").click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "管理")))
        driver.find_element_by_link_text("管理").click()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/section/div/div/div[1]/div/div/button[3]')))
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[1]/div/div/button[3]').click() #點團隊

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/span')))
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/span').click() #點02021团队
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="6100f264e24c97da0be4439c"]/div/div/div[2]/div/div[1]/button[2]')))
        driver.find_element_by_xpath('//*[@id="6100f264e24c97da0be4439c"]/div/div/div[2]/div/div[1]/button[2]').click() #添加用戶
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="6100f264e24c97da0be4439c"]/div/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div/a/div[3]/button').click() #加入用戶
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="6100f264e24c97da0be4439c"]/div/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/div/div/div/div/a/div[3]/button').click() #刪除用戶
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="6100f264e24c97da0be4439c"]/div/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/div[3]/div/div/div/a/div[3]/button').click() #加入用戶
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="6100f264e24c97da0be4439c"]/div/div/div[2]/div/div[3]/div/div/div[2]/div[3]/button[2]').click()  #點添加按鈕
        time.sleep(2)

        Username = driver.find_element_by_xpath('//*[@id="6100f264e24c97da0be4439c"]/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr/td[1]/div/div[2]/div/span').text
        print(Username)
        self.assertEqual("wesley.chen+02021inp", Username, "兩值不對等") #驗證(expected預期在前，actual實際在後)
        time.sleep(2)

        driver.find_element_by_class_name("table-btn").click() #點刪除icon
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "action-btn")))
        driver.find_element_by_class_name("action-btn").click() #點移除按鈕
        time.sleep(2)

        Message = driver.find_element_by_class_name("row-msg-div-loading").text
        print(Message)
        self.assertEqual("还没有用户被添加到团队中。", Message, "兩值不對等")  # 驗證(expected預期在前，actual實際在後)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)