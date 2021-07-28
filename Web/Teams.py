import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TeamsCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(600)  #隱式等待60秒
        self.driver.get("https://dev.deephow.net/")
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input'))) #顯示等待
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input').send_keys("wesley.chen+root@deephow.com")
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        self.driver.find_element_by_class_name("v-btn__content").click()
        time.sleep(2)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input'))) #顯示等待
        self.driver.find_element_by_xpath('//*[@id="app"]/div[2]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input').send_keys("Pa$$w0rd")
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        self.driver.find_element_by_class_name("v-btn__content").click()

    def test_teams(self):
        driver = self.driver
        current_time = time.strftime("%Y/%m/%d/ %H:%M:%S", time.localtime(time.time()))
        #time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "tool-bar-icon")))
        driver.find_element_by_class_name("tool-bar-icon").click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "管理")))
        driver.find_element_by_link_text("管理").click()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/section/div/div/div[1]/div/div/button[3]/span')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/div[1]/div/div/button[3]/span').click() #點團隊

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[6]/section/div/div/div[2]/div/div[1]/button/div')))
        driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/div[2]/div/div[1]/button/div').click() #新建團隊
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[7]/section/div/div/div[2]/div/section/div[1]/div/div/div[2]/form/div[1]/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[7]/section/div/div/div[2]/div/section/div[1]/div/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys(current_time + " 团队")

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[7]/section/div/div/div[2]/div/section/div[1]/div/div/div[2]/form/div[2]/div/div')))
        driver.find_element_by_xpath('//*[@id="app"]/div[7]/section/div/div/div[2]/div/section/div[1]/div/div/div[2]/form/div[2]/div/div').click()
        driver.find_element_by_link_text("02021工作空間").click() #選工作空間
        driver.find_element_by_xpath('//*[@id="app"]/div[7]/section/div/div/div[2]/div/section/div[1]/div/div/div[3]/button').click() #新建按鈕
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/div[2]/div/div[2]/div[2]/div/div[1]/table/thead/tr[1]/th[1]/i').click() #點排序
        time.sleep(2)

        driver.find_element_by_class_name("team-name-hover").click() #點第一個團隊
        TeamsTitle = driver.find_element_by_class_name("text-truncate").text
        print(TeamsTitle)

        self.assertEqual(TeamsTitle, current_time + " 团队", "兩值不對等")  # 驗證(expected預期在前，actual實際在後)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)