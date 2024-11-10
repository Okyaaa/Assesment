import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

service = Service(executable_path="chromedriver")
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=chr_options)
driver.get("https://www.paper.id/webappv1/#/login")
driver.find_element(By.NAME, "email").send_keys("kandidat@paper.id")
driver.find_element(By.CSS_SELECTOR, ".paper-button").click()

try:
    WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.ID, "mat-mdc-dialog-0")))
    print("Pop up appears")
    password = driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/login-password-dialog/section/div[3]/form/div[1]/div[2]/input')
    password.send_keys("paper.id")
    driver.find_element(By.XPATH, '//*[@id="mat-mdc-dialog-0"]/div/div/login-password-dialog/section/div[3]/form/button').click()
except TimeoutException:
    print("Pop up not appears")

WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="navbarCustom"]/div[3]')))

candidate_name= driver.find_element(By.XPATH, '//*[@id="onboarding-accurate-4"]/div[2]/div[1]/span[1]').text
print(candidate_name)

if candidate_name == 'Kandidat':
    print("Test Pass")
else:
    print("failed")


time.sleep(2)
    
driver.close()