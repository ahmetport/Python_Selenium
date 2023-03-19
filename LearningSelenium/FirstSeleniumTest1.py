from selenium import webdriver

driver = webdriver.Chrome()


driver.get("https:\\www.rcvacademy.com")
driver.maximize_window()
print(driver.title)