from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

path = "C:\\Programs\\Python37\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.maximize_window()
#driver.implicitly_wait(30)
driver.get("http://kennethhutw.github.io/demo/Selenium/bload.html")
#WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.ID,'bload')))
WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID,'bload')))
#time.sleep(3)

Aboutlink = driver.find_element_by_id('bload')
Aboutlink.click()
time.sleep(2)

print(driver.current_url)
driver.close()
driver.quit()
