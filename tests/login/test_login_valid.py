import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

import time
from utilities.webdriver_setup import get_driver
from utilities.read_config import read_config
from pages.login_page import LoginPage
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    yield driver
    driver.quit()

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

