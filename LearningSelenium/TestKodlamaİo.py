from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
import time
from selenium.webdriver.common.by import By



class kodlama_io():
    def coding(self):
        driver.get("https://www.kodlama.io/")
        driver.maximize_window()
        kurs_listesi=driver.find_elements(By.CLASS_NAME,"course-listing")
        time.sleep(3)
        print(f"kodlamaio sitesinde şu an ücretsiz {len(kurs_listesi)} adet kurs var.")
        time.sleep(5)
        driver.find_element(By.XPATH,"(//img[@role='presentation'])[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH,"//button[@class='banner__button b-75248009-button_border_radius base-button']").click()
        time.sleep(5)
kod= kodlama_io()
kod.coding()