import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class InactiveUserCase(unittest.TestCase):
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

    def test_inactiveuser(self):
        driver = self.driver
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "tool-bar-icon")))
        driver.find_element_by_class_name("tool-bar-icon").click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "管理")))
        driver.find_element_by_link_text("管理").click()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/section/div/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[5]/div/div/button')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[5]/div/div/button').click() #點編輯用戶
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input').send_keys(Keys.CONTROL + "a") #鍵盤全選
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input').send_keys(Keys.BACKSPACE) #鍵盤退回
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input').send_keys("wesley.chen+02021outp")

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div').click() #點狀態改未激活
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/div[2]/button').click() #按保存按鈕
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "filter-div")))
        driver.find_element_by_class_name("filter-div").click() #點狀態
        time.sleep(2)
        driver.find_element_by_partial_link_text("未激活").click()
        time.sleep(2)

        outp = driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[1]/span').text
        print(outp)
        self.assertEqual("Wesley.Chen+02021outp", outp,"兩值不對等")  #驗證(expected預期在前，actual實際在後)
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[5]/section/div/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[5]/div/div/button')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/div[2]/div[4]/div/div/table/tbody/tr[1]/td[5]/div/div/button').click() #點編輯用戶
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input').send_keys(Keys.CONTROL + "a") #鍵盤全選
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input').send_keys(Keys.BACKSPACE) #鍵盤退回
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input').send_keys("wesley.chen+02021inp")

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[2]/div/div/div/div/div[1]/div').click() #點狀態改激活
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/div[2]/button').click() #按保存按鈕
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME,"filter-div")))
        driver.find_element_by_class_name("filter-div").click() #點狀態
        time.sleep(2)
        driver.find_element_by_partial_link_text("激活").click()
        time.sleep(2)

        inp = driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/div[2]/div[3]/div/div/table/tbody/tr[1]/td[1]/span').text
        print(inp)
        self.assertEqual("Wesley.Chen+02021inp", inp, "兩值不對等") #驗證(expected預期在前，actual實際在後)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)