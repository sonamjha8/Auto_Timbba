from consignment import consignment
from login_scenario import Login
from driver_timbba import Chrome_driver


def main_fun(): 
    print("MAIN FUNCTION CALLED")


if __name__ == '__main__':
    main_fun()

    object_1 = Chrome_driver()

    object_2 = Login()
    object_2.login()

    



