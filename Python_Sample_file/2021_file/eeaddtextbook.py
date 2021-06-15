import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class eeaddtextbookCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(600)  #隱式等待600秒
        self.driver.get("http://eeauto.devtest.tk/")

    def test_eeaddtextbook(self):
        driver = self.driver
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "admin")))  # 顯示等待 30秒內每隔0.5毫秒掃描1次頁面變化
        driver.find_element_by_link_text("admin").click()
        driver.get("http://eeauto.devtest.tk/course/94")
        driver.find_element_by_partial_link_text("新增主題").click()
        driver.switch_to.frame(0) #切到子級用frame的index來定位，第一個是0
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "title")))
        driver.find_element_by_name("title").send_keys("test 主題")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "cke_wysiwyg_frame")))
        frame = driver.find_element(By.CLASS_NAME, "cke_wysiwyg_frame")
        driver.switch_to.frame(frame)
        body = driver.find_element(By.TAG_NAME, "body")
        body.send_keys("test 主題說明")
        driver.switch_to.default_content() #切到frame中之後，我們便不能繼續操作主文檔的元素，這時如果想操作主文檔內容，則需切回主文檔。
        driver.switch_to.frame(0) #切到子級用frame的index來定位，第一個是0
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="editChapterForm"]/div[5]/div/button[1]')))
        driver.find_element_by_xpath('//*[@id="editChapterForm"]/div[5]/div/button[1]').click()
        driver.switch_to.parent_frame() #切到父级frame
        time.sleep(1)
        plus_icon = driver.find_element_by_css_selector('span.font-icon.fa.fa-plus-circle')
        plus_icon.click()
        time.sleep(3)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
   unittest.main(verbosity=2)