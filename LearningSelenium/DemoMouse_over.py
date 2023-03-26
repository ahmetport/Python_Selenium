from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


class DemoMouseOver():
    def mouse_hover(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        sleep(3)

        morebutton=driver.find_element(By.XPATH,"//span[@class='more-arr']")
        sleep(3)
        actions=ActionChains(driver)
        actions.move_to_element(morebutton).perform()
        sleep(5)
        driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
        sleep(10)


mous=DemoMouseOver()
mous.mouse_hover()
