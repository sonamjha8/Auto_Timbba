import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class Chrome_driver :
  def __init__(self):

    # Initialize Chrome webdriver using ChromeDriverManager
    self.url = "https://admin.timbba.in/#/login"

    # Create Chrome webdriver with ChromeDriverManager
    driver_service = ChromeService(ChromeDriverManager().install())
    self.driver = webdriver.Chrome(service=driver_service)
    #self.driver.get(self.url)

#object = Chrome_driver()

    #------ To run this file uncomment the Chrome_driver() function