from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver_timbba import Chrome_driver
import time

class Login:
    def __init__(self):
        self.driver = Chrome_driver.get_instance()
        self.url = "https://admin.timbba.in/#/login"

    def login(self):
        self.driver.get(self.url)
        user_name = self.driver.find_element(By.ID, "a3")
        user_name.send_keys("Subtlelabs")
        psw = self.driver.find_element(By.ID, "a4")
        psw.send_keys("sltAdmin")
        login_button = self.driver.find_element(By.XPATH, '//*[@id="pwd-container"]/div/div/div/div/div/div[4]/button')
        login_button.click()
        time.sleep(5)


    def logout(self):

        # Click on the dropdown with class name 'avatar-container'
        dropdown_avatar = self.driver.find_element(By.CLASS_NAME, 'avatar-container')
        dropdown_avatar.click()
        time.sleep(2)

        # Locate the dropdown menu by class name 'el-dropdown-menu'
        dropdown_menu = self.driver.find_element(By.CLASS_NAME, 'el-dropdown-menu')

        # Find all list items within the dropdown menu
        list_items = dropdown_menu.find_elements(By.CLASS_NAME, 'el-dropdown-menu__item')

        # Iterate through the list items to find the one with the text "Logout"
        for item in list_items:
            if item.text.strip() == "Logout":
                print(item.text.strip() )
                item.click()
                print("clicked")
                time.sleep(5)
                break  # Exit the loop once the "Logout" item is clicked
                



        
        




# Instantiate the Login class
# object = Login()
# object.login()
