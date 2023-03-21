from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class DemoAlertPopup():
    def jsalert(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")#iframe iniçine girmek için
        time.sleep(4)
        #ACCEPT ALERT
       # driver.find_element("//button[normalize-space()='Try it']").click()
       # time.sleep(5)
       # driver.switch_to.alert.accept()
       # time.sleep(3)

        #DİSMİSS ALERT
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        time.sleep(5)
        driver.switch_to.alert.dismiss()
        time.sleep(3)

        #send to text alert
        #driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        #time.sleep(5)
        #print(driver.switch_to.alert.text)# çıkan popupda ne yazdıgını bize getir
        #driver.switch_to.alert.send_keys("hello PORTAKAL")
        #driver.switch_to.alert.accept() # yeni yazılan metni kabul et
        #time.sleep(3)

alert=DemoAlertPopup()
alert.jsalert()