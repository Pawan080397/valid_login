from xml.dom.xmlbuilder import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--start-maximized")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)




# ---------------------------
# SIMPLE LOGIN TEST SCRIPT
# ---------------------------
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()



# 👉 Your Login Page URL
driver.get("http://192.168.1.127:8000/")

# 👉 Enter Username
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("admin")

# 👉 Enter Password
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("admin123")

# 👉 Click Login Button
driver.find_element(By.XPATH, "//span[@class='MuiButton-label']").click()

time.sleep(3)

# 👉 Validation (Check login success)
if "dashboard" in driver.current_url.lower():
    print("Login Successful!")
else:
    print("Login Failed!")

driver.quit()


