import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class HellowloginCase(unittest.TestCase):
        driver = webdriver.Chrome()
        driver.maximize_window()    #視窗最大化
        driver.implicitly_wait(600)  #隱式等待60秒
        driver.get("https://dev.deephow.net/")
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input'))) #顯示等待
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/div[1]/form/div/div/div[1]/div/input').send_keys("wesley.chen+root@deephow.com")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        driver.find_element_by_class_name("v-btn__content").click()
        time.sleep(2)
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input'))) #顯示等待
        driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div[1]/div[2]/div/form/div/div/div[1]/div[1]/input').send_keys("Pa$$w0rd")
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "v-btn__content")))
        driver.find_element_by_class_name("v-btn__content").click()