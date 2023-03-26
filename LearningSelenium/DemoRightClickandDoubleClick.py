from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


class DemoMouseOver():
    def mouse_hover(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.get("")
        driver.maximize_window()
        sleep(3)