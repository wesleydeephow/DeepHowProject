import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class InvitesUserCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(100)  #隱式等待10秒
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

    def test_invitesuser(self):
        driver = self.driver
        current_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "tool-bar-icon")))
        driver.find_element_by_class_name("tool-bar-icon").click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "管理")))
        driver.find_element_by_link_text("管理").click()

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "filter-div")))
        driver.find_element_by_class_name("filter-div").click() #點狀態
        driver.find_element_by_partial_link_text("已邀请").click()
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/section/div/div/div[2]/div[1]/button[2]')))
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div[1]/button[2]').click() #點邀請用戶
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div[1]/div/div/div[1]/div/input').send_keys(current_time + "User") #填姓名
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[2]/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[2]/div/div[1]/div/input').send_keys("Wesley.chen+" + current_time + "@deephow.com") #填信箱
        time.sleep(2)

        InvitesButton = driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/div[2]/button')
        action = ActionChains(driver)
        action.double_click(InvitesButton).perform() #邀請按鈕點兩下
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[4]/section/div/div/section/div/div/div[2]/div/div[2]/button')))
        driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/section/div/div/div[2]/div/div[2]/button').click() #點完成按鈕
        time.sleep(2)

        firstname = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td[1]/span').text #點第一筆姓名
        print(firstname)
        self.assertEqual(current_time + "User", firstname, "兩值不對等") #驗證(expected預期在前，actual實際在後)
        firstemail = driver.find_element_by_xpath('//*[@id="app"]/div[4]/section/div/div/div[2]/div[5]/div/div/table/tbody/tr[1]/td[2]').text #點第一筆信箱
        print(firstemail)
        self.assertEqual("wesley.chen+" + current_time + "@deephow.com", firstemail, "兩值不對等") #驗證(expected預期在前，actual實際在後)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)