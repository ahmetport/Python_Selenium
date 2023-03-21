from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoScreenshot():
    def screenshot(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.maximize_window()
        time.sleep(5)
        demoscenshot=driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        demoscenshot.screenshot(".\\test.png")
        demoscenshot.click()
        time.sleep(2)

        driver.get_screenshot_as_file("C:\\python-selenium\\error.png")
        driver.save_screenshot(".\\test1.png")

demosss=DemoScreenshot()
demosss.screenshot()


