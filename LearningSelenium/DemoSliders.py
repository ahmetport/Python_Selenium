from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep


class DemoSliders():
    def slid(self):
        driver= webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.snapdeal.com/products/mens-footwear?sort=plrty")
        driver.maximize_window()

        element1=driver.find_element(By.XPATH,"//a[@class='price-slider-scroll left-handle ui-slider-handle ui-state-default ui-corner-all hashAdded']")
        element2=driver.find_element(By.XPATH,"//a[contains(@class, 'right-handle')]")
        ActionChains(driver).drag_and_drop_by_offset(element1, 60 , 0).perform()
        sleep(5)
        #ActionChains(driver).click_and_hold(element1).pause(1).move_by_offset(50, 0).release().perform()
        #ActionChains(driver).move_to_element(element1).pause(1).click_and_hold(element1).move_by_offset(40,0).release().perform()
        ActionChains(driver).drag_and_drop_by_offset(element2, -40, 0).perform()
        sleep(5)





SS=DemoSliders()
SS.slid()