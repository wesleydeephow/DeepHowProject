from selenium import webdriver
import time

path = "C:\\Programs\\Python37\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com/")

#first name
driver.find_element_by_xpath('//*[@id="u_0_j"]').send_keys('Chen')
#surname
driver.find_element_by_xpath('//*[@id="u_0_l"]').send_keys('WeiMing')
#button
driver.find_element_by_xpath('//*[@id="u_0_11"]').click()
time.sleep(3)

driver.close()
driver.quit()

