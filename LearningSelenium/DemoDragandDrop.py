from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


class DemoDragDrop():
    def draganddrop(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        sleep(3)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        element1=driver.find_element(By.ID,"draggable")
        element2=driver.find_element(By.ID,"droppable")
        #ActionChains(driver).drag_and_drop(element1,element2).perform()
        ActionChains(driver).drag_and_drop_by_offset(element1,419,238).perform()
        sleep(10)

dd=DemoDragDrop()
dd.draganddrop()