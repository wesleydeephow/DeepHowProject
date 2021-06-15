from selenium import webdriver
import time

path ="C:\\Programs\\Python37\\chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/")
print(driver.current_url)
print(driver.title)
time.sleep(2)

signup = driver.find_element_by_class_name("btn-primary")
signup.click()
print(driver.current_url)
print(driver.title)
time.sleep(2)

driver.back()

signin = driver.find_element_by_class_name("btn-default")
signin.click()
print(driver.current_url)
print(driver.title)
time.sleep(2)

driver.close()
driver.quit()
