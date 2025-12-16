import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import time
from utilities.webdriver_setup import get_driver
from utilities.read_config import read_config
from pages.login_page import LoginPage


def test_valid_login():
    driver = get_driver()
    config = read_config()

    driver.get(config["base_url"])
    login = LoginPage(driver)

    login.enter_username(config["username"])
    login.enter_password(config["password"])
    login.click_login()

    time.sleep(2)

    print("login success")
    driver.quit()

