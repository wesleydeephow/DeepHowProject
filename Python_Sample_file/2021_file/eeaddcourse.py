import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class eeaddcourseCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()    #視窗最大化
        self.driver.implicitly_wait(600)  #隱式等待600秒
        self.driver.get("http://eeauto.devtest.tk/")

    def test_eeaddcourse(self):
        driver = self.driver
        current_time = time.strftime("%Y/%m/%d/ %H:%M:%S", time.localtime(time.time()))
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.LINK_TEXT, "admin"))) #顯示等待 30秒內每隔0.5毫秒掃描1次頁面變化
        driver.find_element_by_link_text("admin").click()
        driver.find_element_by_class_name("dropdown-toggle").click()
        driver.find_element_by_link_text("課程管理").click()
        print(driver.current_url)
        print(driver.title)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "新增")))
        driver.find_element_by_partial_link_text("新增").click()
        driver.switch_to.frame(0) #切到子級用frame的index來定位，第一個是0
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, "code")))
        driver.find_element_by_name("code").send_keys(current_time)
        driver.find_element_by_name("name").send_keys(current_time + " 課程")
        driver.find_element_by_name("credit").send_keys("1")
        driver.find_element_by_class_name("select2-search__field").send_keys("admin")
        time.sleep(1) #抓取 select2 需停留1秒
        driver.find_element_by_class_name("select2-search__field").send_keys(Keys.ENTER) #鍵盤Enter
        selectGrade = Select(driver.find_element_by_name("gradeId"))
        selectGrade.select_by_value("10") #select抓value方法
        for op in selectGrade.options:
            print(op.text) #取得下拉選單元件裡所有選項的文字
        selectClass = Select(driver.find_element_by_name("classId"))
        selectClass.select_by_index(2) #select抓index方法
        driver.find_element_by_xpath('//*[@id="edit_form"]/div[5]/div/button[1]').click()
        driver.switch_to.parent_frame() #切到父级frame
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "2021/")))
        driver.find_element_by_partial_link_text("2021/").click() #點剛建立的課程
        CourseTitle = driver.find_element_by_class_name("fs-text-divider").text
        print(CourseTitle)
        self.assertEqual(CourseTitle,current_time + " 課程","兩值不對等")
        time.sleep(2)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
   unittest.main(verbosity=2)