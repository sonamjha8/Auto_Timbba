import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class Chrome_driver:
    driver = None

    #can call the get_instance method for 1st time initile the driver chrome browser
    @classmethod
    def get_instance(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        return cls.driver

    #can call the quit_driver method when you want to close the browser window
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None
