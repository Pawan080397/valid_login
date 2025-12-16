from selenium.webdriver.common.by import By 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)
        # 👉 Yaha apne locators daal
        self.username_input = (By.XPATH, "//input[@type='text']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.login_button = (By.XPATH, "//span[@class='MuiButton-label']")
        # self.error_message = (By.ID, "error")

    def enter_username(self, username):
        self.wait.until(EC.visibility_of_element_located(self.username_input)).send_keys(username)

    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located(self.password_input)).send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()