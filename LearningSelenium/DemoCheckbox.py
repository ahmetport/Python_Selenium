from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(ChromeDriverManager().install())


class DemoCheckbox():
    def Checkbox(self):
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(3)
        driver.find_element(By.XPATH,"//a[normalize-space()='Non Stop Flights']").click()
        time.sleep(3)
        che=driver.find_element(By.XPATH,"(//i[@class='ico ico-checkbox'])[2]").is_selected()
        print(che)
        driver.find_element(By.XPATH,"//a[normalize-space()='Student Fare']")
        time.sleep(3)
        student_fare=driver.find_element(By.XPATH,"//a[normalize-space()='Student Fare']").is_selected()
        print(student_fare)
        

check=DemoCheckbox()
check.Checkbox()
