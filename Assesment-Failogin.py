import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

email = "random-candidate@yuhu.com"

service = Service(executable_path="chromedriver")
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chr_options)
driver.get("https://www.paper.id/webappv1/#/login")
driver.find_element(By.NAME, "email").send_keys(email)
driver.find_element(By.CSS_SELECTOR, ".paper-button").click()
try:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mat-snack-bar-container-live-0"]/div/app-paper-toast/div')))
    print("Toast message exist")
    validation = driver.find_element(By.XPATH, '//*[@id="mat-snack-bar-container-live-0"]/div/app-paper-toast/div/div[2]/h3').text
except:
    print("Toast message doesn't exist")

if "Email tidak terdaftar" in validation:
    print("Test pass")
else: 
    print("Test failed")

time.sleep(2)
driver.close()