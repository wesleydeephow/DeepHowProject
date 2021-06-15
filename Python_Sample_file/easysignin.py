import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class EasySign(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://autofms.devtest.tk/index/login?next=%2F')

    def test_singin(self):
        driver = self.driver
        print(driver.current_url)
        print(driver.title)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.NAME, 'account')))
        driver.find_element_by_name('account').send_keys('admin')
        driver.find_element_by_name('password').send_keys('111111')
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, 'btn-primary')))
        driver.find_element_by_class_name('btn-primary').click()
        admin = driver.find_element_by_link_text('系統管理者').text
        print(admin)
        self.assertEqual(admin, "系統管理者", "系統管理者沒成功登入")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)