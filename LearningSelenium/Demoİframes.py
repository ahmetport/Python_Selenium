from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoFrames():
    def windowiframes(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))#iframe iniçine girmek için
        time.sleep(4)
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH,"//a[@id='signupbtn_topnav']").click()# frame içine girdik tıklıyoruz
        time.sleep(10)

frame=DemoFrames()
frame.windowiframes()



