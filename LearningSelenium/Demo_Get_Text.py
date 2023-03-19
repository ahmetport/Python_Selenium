from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class DemoGetText():
    def GetText(self):
        driver.get("https:\\www.amazon.com")
        driver.maximize_window()
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("nutella\n")
        text=driver.find_element(By.XPATH,"(//span[@class='a-size-base-plus a-color-base a-text-normal'][contains(text(),'Nutella Hazelnut Spread with Cocoa for Breakfast, ')])[1]").text
        text1=driver.find_element(By.ID,"nav-link-accountList-nav-line-1").text
        print(text1)
        time.sleep(3)


find = DemoGetText()
find.GetText()