from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

username = 'nishthac3'
password = 'Nishtha@c3'

chrome_driver_path = "/Users/administrator/Downloads/chromedriver_mac64/chromedriver"

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
chrome_options.add_argument("--start-maximized")  


chrome_options.add_argument('executable_path=' + chrome_driver_path)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://demoqa.com/login")

username_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
)
username_field.send_keys(nishthac3)

password_field = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='password']"))
)
password_field.send_keys(Nishtha@c3)

submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type=\"submit\"]"))
)
submit_button.click()

print("Logged in successfully")
