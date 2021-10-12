import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class WorkspacesCase(unittest.TestCase):
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

    def test_workspaces(self):
        driver = self.driver
        current_time = time.strftime("%Y/%m/%d/ %H:%M:%S", time.localtime(time.time()))
        current_time2 = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "tool-bar-icon")))
        driver.find_element_by_class_name("tool-bar-icon").click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "管理")))
        driver.find_element_by_link_text("管理").click()

        # WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/section/div/div/div[1]/div/div/button[2]')))
        # driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[1]/div/div/button[2]').click() #點工作空間
        driver.get("https://dev.deephow.net/admin/workspaces")

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[1]/button')))
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[1]/button').click() #新建工作空間
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[1]/div/div[1]/div/input').send_keys(current_time + " 工作空间") #填寫工作空間名稱

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[2]/div/div[1]/div[1]/div[2]/div/i')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[2]/div/div[1]/div[1]/div[2]/div/i').click()
        driver.find_element_by_link_text("02021業務").click() #選業務
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[3]/div/div[1]/div[1]/div[2]/div/i')))
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/form/div[3]/div/div[1]/div[1]/div[2]/div/i').click() #點語言
        driver.find_element_by_link_text("中文").click()
        driver.find_element_by_xpath('//*[@id="app"]/div[5]/section/div/div/section/div/div/div[2]/button').click() #點新建按鈕
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/div[2]/table/thead/tr/th[1]/div/div/button/i').click() #點排序
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/span')))
        WorkspacesTitle = driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/span').text #點第一筆工作空間
        print(WorkspacesTitle)
        self.assertEqual(WorkspacesTitle, current_time + " 工作空间", "兩值不對等")  # 驗證(expected預期在前，actual實際在後)
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="app"]/div[3]/section/div/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[1]/span').click() #進入第一筆工作空間
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "filter-div")))
        driver.find_element_by_class_name("filter-div").click()  # 點狀態
        driver.find_element_by_partial_link_text("已邀请").click()
        time.sleep(2)

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[6]/section/div/div/div[2]/section/div[1]/button[3]')))
        driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/div[2]/section/div[1]/button[3]').click() #添加用戶

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[7]/section/div/div/div[2]/section/section/div/div/form/div[1]/div[1]/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[7]/section/div/div/div[2]/section/section/div/div/form/div[1]/div[1]/div/div[1]/div/input').send_keys("Wesley.Chen+" + current_time2) #填姓名
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[7]/section/div/div/div[2]/section/section/div/div/form/div[2]/div/div[1]/div/input')))
        driver.find_element_by_xpath('//*[@id="app"]/div[7]/section/div/div/div[2]/section/section/div/div/form/div[2]/div/div[1]/div/input').send_keys("wesley.chen+" + current_time2 + "@deephow.com") #填信箱

        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[7]/section/div/div/div[2]/section/section/div/div/form/div[3]/div/div[1]/div[1]/div[2]/div/i')))
        driver.find_element_by_xpath('//*[@id="app"]/div[7]/section/div/div/div[2]/section/section/div/div/form/div[3]/div/div[1]/div[1]/div[2]/div/i').click() #填角色
        driver.find_element_by_link_text("工作空间管理员").click()

        InvitesButton = driver.find_element_by_xpath('//*[@id="app"]/div[7]/section/div/div/div[2]/section/section/div/div/div[3]/button') #點邀請按鈕
        action = ActionChains(driver)
        action.double_click(InvitesButton).perform()  # 邀請按鈕點兩下
        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/div[2]/section/section/div/div/div[2]/div/div[2]/button').click() #點完成按鈕
        time.sleep(2)

        firstname = driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/div[2]/section/div[5]/div/div/table/tbody/tr/td[1]/span').text #點第一筆姓名
        print(firstname)
        self.assertEqual("Wesley.Chen+" + current_time2, firstname, "兩值不對等")  # 驗證(expected預期在前，actual實際在後)
        firstemail = driver.find_element_by_xpath('//*[@id="app"]/div[6]/section/div/div/div[2]/section/div[5]/div/div/table/tbody/tr/td[2]/span').text  #點第一筆信箱
        print(firstemail)
        self.assertEqual("wesley.chen+" + current_time2 + "@deephow.com", firstemail,"兩值不對等")  # 驗證(expected預期在前，actual實際在後)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
     unittest.main(verbosity=2)