from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoJVscript():
    def javascript(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
       # driver.get("https://www.rcvacademy.com/")
        driver.execute_script("window.open('https://www.rcvacademy.com/', '_self');")
        driver.maximize_window()
        time.sleep(10)

       # demojjs=driver.execute_script("(//img[@class='attachment-large size-large entered litespeed-loaded'])[1];")
       # driver.execute_script("arguments[0].click();",demojjs)
        time.sleep(10)



jjvs=DemoJVscript()
jjvs.javascript()