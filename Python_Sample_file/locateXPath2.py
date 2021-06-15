from selenium import webdriver
import time

path = "C:\\Programs\\Python37\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/")

driver.find_element_by_xpath('//a[@id="signup"]').click()
print(driver.title)
time.sleep(2)
driver.back()

driver.find_element_by_xpath('//a[@name="signin"]').click()
print(driver.title)
time.sleep(2)

driver.close()
driver.quit()