from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class DemoAttributeValue():
    def Value(self):
        driver.get("https:\\www.yatra.com")
        driver.maximize_window()
        Attribute=driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(Attribute)
        time.sleep(3)


find = DemoAttributeValue()
find.Value()