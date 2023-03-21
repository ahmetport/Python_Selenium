from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class DemoDropDown():
    def dropdown(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.salesforce.com/eu/form/signup/freetrial-sales-pe/?d=70130000000EqoP")
        driver.maximize_window()
        time.sleep(5)
        DropDownn=driver.find_element(By.NAME,"CompanyEmployees")
        dd=Select(DropDownn)

        dd.select_by_index(1)
        time.sleep(5)
        dd.select_by_value("50")
        time.sleep(5)
        dd.select_by_visible_text("500 - 999 employees")
        time.sleep(10)

dddrop=DemoDropDown()
dddrop.dropdown()







