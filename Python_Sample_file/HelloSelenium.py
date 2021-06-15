from selenium import webdriver
import time

path ="C:\\Programs\\Python39\\chromedriver.exe"
path2 ="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
path3 ="C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedgedriver.exe"

driver = webdriver.Chrome(path)
#driver.maximize_window()
driver2 = webdriver.Firefox(firefox_binary=path2)
#driver2.maximize_window()
driver3 = webdriver.Edge(path3)
#driver3.maximize_window()

# chrome
driver.get("http://rwd.devtest.tk")
print(driver.current_url)
print(driver.title)
time.sleep(1)
driver.close()
driver.quit()

# firefox
driver2.get("http://rwd.devtest.tk")
print(driver2.current_url)
print(driver2.title)
time.sleep(2)
driver2.close()
driver2.quit()

# edge
driver3.get("http://rwd.devtest.tk")
print(driver3.current_url)
print(driver3.title)
time.sleep(3)
driver3.close()
driver3.quit()