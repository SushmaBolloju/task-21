import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
paths = r"C:\Users\chand\Downloads\chromedriver-win32\chromedriver-win32\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options=Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(3)
driver.get("https://www.saucedemo.com/")
print("Cookies before login:")
print(driver.get_cookies())
time.sleep(3)
username_field = driver.find_element(By.NAME, 'user-name')
password_field = driver.find_element(By.NAME, 'password')
username_field.send_keys('standard_user')
password_field.send_keys('secret_sauce')
password_field.send_keys(Keys.RETURN)
driver.maximize_window()
driver.add_cookie({'name': 'sri', 'value': '101'})
cookies = driver.get_cookies()
print("Cookies after login:", cookies)
# MENU
menu = driver.find_element(By.XPATH, '//*[@id="react-burger-menu-btn"]') # Adjust XPath according to your logout button
menu.click()
time.sleep(3)
#logout
log_out = driver.find_element(By.XPATH, '//*[@id="logout_sidebar_link"]') # Adjust XPath according to your logout button
log_out.click()
time.sleep(3)
# # Close the browser
driver.quit()
