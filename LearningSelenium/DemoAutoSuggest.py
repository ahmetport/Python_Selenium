from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoAutoSuggest():
    def AutoSuggest(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(5)
        depart_from=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        time.sleep(4)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.ENTER)
        time.sleep(2)

        going_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        time.sleep(3)
        search_results=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_results))

        for result in search_results :
            if "New York (JFK)" in result.text:
                print(result.text)
                result.click()
                time.sleep(5)
                break

depart=DemoAutoSuggest()
depart.AutoSuggest()
