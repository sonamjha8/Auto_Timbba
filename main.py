from login_scenario import Login
from driver_timbba import Chrome_driver
from consignment import Consignment
import time


def main_fun(): 
    print("MAIN FUNCTION CALLED")

    chrome_driver = Chrome_driver.get_instance()

    login = Login()
    login.login()

    # # Instantiate the Consignment class
    # consignment = Consignment(chrome_driver)
    # # Call cons_access method
    # consignment.cons_access()
    # time.sleep(5)


    #for Logout
    login.logout()
    time.sleep(5)






    # Close the browser window
    # Chrome_driver.quit_driver()

if __name__ == '__main__':
    main_fun()



