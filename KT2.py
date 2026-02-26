from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.reddit.com/login/")
print("Открыли Reddit")

time.sleep(3)

# Поле логина
username = browser.find_element(By.ID, "loginUsername")
username.send_keys("root")

# Поле пароля
password = browser.find_element(By.ID, "loginPassword")
password.send_keys("123")

time.sleep(2)

# Кнопка входа
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(30)
