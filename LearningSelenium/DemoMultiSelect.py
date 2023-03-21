from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class DemoDropDown():
    def dropdownmultiselect(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("http://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        driver.maximize_window()
        time.sleep(5)
        dd=driver.find_element(By.ID,"multi-select")
        multi=Select(dd)
        multi.select_by_value("California")
        multi.select_by_index(0)
        multi.select_by_visible_text("Florida")
        multi.select_by_value("New Jersey")
        multi.select_by_index(1)
        multi.select_by_visible_text("New York")
        time.sleep(10)
        multi.deselect_by_index(0)
        multi.deselect_by_value("Florida")
        time.sleep(5)
        multi.deselect_all()
        time.sleep(10)



multiselect=DemoDropDown()
multiselect.dropdownmultiselect()