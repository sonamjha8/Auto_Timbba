from selenium.webdriver.common.by import By

class Consignment:
    def __init__(self, driver):
        self.driver = driver

    def cons_access(self):
        # Click on New Pinewood Log
        pinelog = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/section/div/div[2]/div/div[1]/div/a[3]')
        pinelog.click()

        # Pinewood form open
        # click on consignment select dropdown
        element = self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div[2]/section/div/div[4]/div[2]/div/section/form/div[1]/div[1]/div/div/span/select')
        element.click()

        # select dropdown list
        # element = self.driver.find_element_by_id("your_dropdown_id")
        # select = Select(element)
        # element.select_by_value('659fbfbcb9474e11b520b4e3')
