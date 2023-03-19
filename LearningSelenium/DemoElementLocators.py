from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class DemoFindElementById():
    def locate_by_id_demo(self):
        driver.get("https:\\www.amazon.com")
        driver.maximize_window()
        driver.find_element(By.ID,"twotabsearchtextbox").send_keys("nutella\n")
        time.sleep(5)
        liste=driver.find_elements(By.TAG_NAME,"img")
        print(len(liste))
        

findById=DemoFindElementById()
findById.locate_by_id_demo()
