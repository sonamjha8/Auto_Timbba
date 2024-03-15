import time
from driver_timbba import Chrome_driver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


class Login(Chrome_driver):

    def login(self):
        driver = Chrome_driver()
        self.driver.get(self.url)
         # Find element by ID and input text
        user_name = self.driver.find_element(By.ID, "a3")
        user_name.send_keys("Subtlelabs")
        self.driver.implicitly_wait(2000)
        psw = self.driver.find_element(By.ID, "a4")
        psw.send_keys("sltAdmin")  
        self.driver.implicitly_wait(4000)
        login_button =self.driver.find_element(By.XPATH, '//*[@id="pwd-container"]/div/div/div/div/div/div[4]/button')
        login_button.click()

        #time.sleep()  # 120 seconds = 2 minutes



# Instantiate the Login class
object = Login()
object.login()

