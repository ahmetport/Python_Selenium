from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class DemoState():
    def WebElement_State(self):
        driver.get("https://training.openspan.com/login")
        driver.maximize_window()
        demo_state=driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(demo_state) #False
        time.sleep(3)
        username=driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("testing")
        time.sleep(3)
        password=driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("testing343")
        time.sleep(3)
        demo_state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(demo_state1) #True




state=DemoState()
state.WebElement_State()
