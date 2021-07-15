import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WorkspacesCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(600)  #隱式等待60秒
        self.driver.get("https://dev.deephow.net/")
        #time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input'))) #顯示等待
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input').send_keys("wesley.chen+root@deephow.com")
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        self.driver.find_element_by_class_name("v-btn__content").click()
        #time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input'))) #顯示等待
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input').send_keys("Pa$$w0rd")
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        self.driver.find_element_by_class_name("v-btn__content").click()

    def test_workspaces(self):
        driver = self.driver
        current_time = time.strftime("%Y/%m/%d/ %H:%M:%S", time.localtime(time.time()))
        #time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "tool-bar-icon")))
        driver.find_element_by_class_name("tool-bar-icon").click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "管理")))
        driver.find_element_by_link_text("管理").click()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/section/div/div/div[1]/div/div/button[2]/span')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/div[1]/div/div/button[2]/span').click() #點工作空間

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/section/div/div/div[2]/div/div[1]/button/div')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/div[2]/div/div[1]/button/div').click() #點邀請用戶

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[6]/section/div/div/section/div/div/form/div[1]/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/section/div/div/form/div[1]/div/div[1]/div/input').send_keys(current_time + " 工作空间") #填寫工作空間名稱

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[6]/section/div/div/section/div/div/form/div[2]/div/div[1]/div[1]/div[1]')))
        driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/section/div/div/form/div[2]/div/div[1]/div[1]/div[1]').click()
        driver.find_element_by_link_text("02021業務").click() #選業務
        driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/section/div/div/div[2]/button/div').click() #點新建按鈕
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/div[2]/div/div[2]/div[2]/div/div[1]/table/thead/tr[1]/th[1]/i').click() #點排序
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "btn-hover")))
        driver.find_element_by_class_name("btn-hover").click() #編輯工作空間

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "title-text")))
        WorkspacesTitle = driver.find_element_by_class_name("title-text").text
        print(WorkspacesTitle)
        self.assertEqual(WorkspacesTitle, current_time + " 工作空间", "兩值不對等") #驗證(expected預期在前，actual實際在後)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)