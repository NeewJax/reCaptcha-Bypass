from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = r'chromedriver.exe' # replace with the path to the chromedriver.exe file

chrome_options = Options()
chrome_options.add_extension("buster.crx")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
pageurl = "https://www.google.com/recaptcha/api2/demo"

# navigate to the page
driver.get(pageurl)
time.sleep(2)

# Find the recaptcha iframe and switch to it
iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//iframe[@title="reCAPTCHA"]'))
)
driver.switch_to.frame(iframe)

# Click on the reCAPTCHA checkbox
driver.find_element(By.CLASS_NAME, 'recaptcha-checkbox-border').click()
driver.implicitly_wait(5)

# Switch back to the default content
driver.switch_to.default_content()

# Find the recaptcha challenge iframe and switch to it
iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//iframe[@title="recaptcha challenge expires in two minutes"]'))
)
driver.switch_to.frame(iframe)

# Click on the buster extension button icon on iframe recaptcha challenge
driver.find_element(By.XPATH, '//*[@id="rc-imageselect"]/div[3]/div[2]/div[1]/div[1]/div[4]').click()
time.sleep(4)

# Switch back to the default content
driver.switch_to.default_content()
time.sleep(8)

# Submit the form
submit_button = driver.find_element(By.ID, 'recaptcha-demo-submit')
submit_button.click()
time.sleep(5)

print('Bypassing the reCaptcha')
time.sleep(4)
