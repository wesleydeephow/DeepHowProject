import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WorkflowCategoriesCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(10)  #隱式等待10秒
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

    def test_workflowcategories(self):
        driver = self.driver
        current_time = time.strftime("%Y/%m/%d/ %H:%M:%S", time.localtime(time.time()))
        #time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "tool-bar-icon")))
        driver.find_element_by_class_name("tool-bar-icon").click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "管理")))
        driver.find_element_by_link_text("管理").click()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/section/div/div/div[1]/div/div/button[5]')))
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[1]/div/div/button[5]').click() #點設置

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/div[1]/div[3]/button')))
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/div[1]/div[3]/button').click() #新建分類
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/section/div[1]/div/div/div[2]/form/div/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/section/div[1]/div/div/div[2]/form/div/div/div[1]/div/input').send_keys(current_time + " 分类")

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/section/div[1]/div/div/div[3]/button')))
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/section/div[1]/div/div/div[3]/button').click() #點新建按鈕
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/table/thead/tr/th[1]/div/div/button/i').click() #點排序
        time.sleep(2)

        driver.find_element_by_class_name("name-text").click() #點第一個分類
        Categories = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/span').text
        print(Categories)
        self.assertEqual(Categories, "项目于 " + current_time + " 分类", "兩值不對等")  #驗證(expected預期在前，actual實際在後)
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]/button')))
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[3]/div/div[1]/div[2]/button').click() #點創建項目

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[3]/div/section/div[1]/div/div/div[2]/form/div/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[3]/div/section/div[1]/div/div/div[2]/form/div/div/div[1]/div/input').send_keys(current_time + " 项目")
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[3]/div/section/div[1]/div/div/div[3]/button').click() #新建按鈕
        time.sleep(2)

        Item = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/table/tbody/tr/td[1]').text
        print(Item)
        self.assertEqual(Item, current_time + " 项目", "兩值不對等")  #驗證(expected預期在前，actual實際在後)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)