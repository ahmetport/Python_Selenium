from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class DemoFindElementById():
    def locate_by_id_demobrowserMethods(self):
        driver.get("https:\\www.amazon.com")
        driver.maximize_window()
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys("nutella\n")
        print(driver.current_url)
        print(driver.title)
        driver.refresh()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(5)



findById = DemoFindElementById()
findById.locate_by_id_demobrowserMethods()