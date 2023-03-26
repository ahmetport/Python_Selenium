from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep


class DemoImplicitWait():
    def wait(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://login.salesforce.com/")
        driver.maximize_window()
        driver.implicitly_wait(10) #elementi bulana kadar bekliyor bulursa hemen donuyor beklemiyor max bekleme

        driver.find_element(By.ID,"username").send_keys("portakal akademi")
        sleep(5)
        driver.find_element(By.ID,"password").send_keys("autodidactic")

ww=DemoImplicitWait()
ww.wait()