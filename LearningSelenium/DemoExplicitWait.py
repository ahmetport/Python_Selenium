from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By




class DemoAutoSuggest():
    def AutoSuggest(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        depart_from=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys("New Delhi")
        depart_from.send_keys(Keys.ENTER)

        going_to=driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_city']")
        going_to.send_keys("New")
        search_results=driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]/li")
        print(len(search_results))

        for result in search_results :
            if "New York (JFK)" in result.text:
                print(result.text)
                result.click()
                break
        # birinci yol ama dinamik degil
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()

        #origin=driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']")
        #origin.click()

        # ikinci yol ama dinamik butun tarihlri al ve istbedigini seç
        all_dates=driver.find_elements(By.XPATH,"//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        print(len(all_dates))
        for date in all_dates:
            if date.get_attribute("data-date") == "30/06/2023":
                date.click()
                break

depart=DemoAutoSuggest()
depart.AutoSuggest()