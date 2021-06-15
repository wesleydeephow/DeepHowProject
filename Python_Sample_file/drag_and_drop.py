from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import *
import time

path="C:\\Programs\\Python39\\chromedriver.exe"

driver = webdriver.Chrome(path)

driver.implicitly_wait(3)  #隱式等待3秒

driver.get('http://kennethhutw.github.io/demo/Selenium/fancytree.html')

driver.find_element_by_xpath('//*[@id="tree"]/tbody/tr[3]/td[3]/span/span[1]').click()

deleteditem = driver.find_element_by_xpath('//*[@id="tree"]/tbody/tr[5]/td[3]/span/span[3]')
deleteditemText = deleteditem.text
ActionChains(driver).context_click(deleteditem).perform()
time.sleep(1)
driver.find_element_by_id('ui-id-3').click() #右鍵刪除
time.sleep(1)
currentItem = driver.find_element_by_xpath('//*[@id="tree"]/tbody/tr[5]/td[3]/span/span[3]') #被刪除了要在寫一次

print('deleted item : ' + deleteditemText)
print('current Item : ' + currentItem.text)

assert deleteditemText !=  currentItem.text

target = driver.find_element_by_xpath('//*[@id="tree"]/tbody/tr[9]/td[3]/span')
ActionChains(driver).drag_and_drop(currentItem,target).perform()
time.sleep(3)


try:
    driver.find_element_by_xpath('//*[@id="tree"]/tbody/tr[11]/td[3]/span/span[3]')
    print("Element exists")
except NoSuchElementException:
    print('Element does not exist')


driver.close()
driver.quit()

