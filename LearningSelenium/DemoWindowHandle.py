from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoMultiWindow():
    def windowHandle(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        parent_handle=driver.current_window_handle
        print(parent_handle)
        time.sleep(5)

        driver.find_element(By.XPATH,"//a[normalize-space()='View All']").click()
        all_handles=driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "(//img[@class='respnsiv-img'])[1]").click()
                time.sleep(6)
                driver.close()
                time.sleep(5)
                break
        driver.switch_to.window(parent_handle)
        driver.find_element(By.XPATH, "//a[normalize-space()='View All']").click()

handlewindow=DemoMultiWindow()
handlewindow.windowHandle()


