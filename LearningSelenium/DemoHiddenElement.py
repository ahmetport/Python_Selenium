from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class DemoHiddenElement():
    def demo_is_display(self):
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        driver.maximize_window()
        elem=driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(elem)
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        elem1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(elem1)

    def demo_is_display_yatra(self):
        driver.get("https://www.yatra.com/hotels")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//label[normalize-space()='Traveller and Hotel']").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[2]").click()
        time.sleep(3)
        elem1=driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        print(elem1)
        driver.find_element(By.XPATH,"//div[@class='hotel_passengerBox dflex relative']//div[3]//div[1]//div[1]//span[1]").click()
        elem2 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        time.sleep(10)
        print(elem2)

demoDisplay=DemoHiddenElement()
#demoDisplay.demo_is_display()
demoDisplay.demo_is_display_yatra()

