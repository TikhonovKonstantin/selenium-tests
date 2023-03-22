from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service('C:/Users/Tikhon/chromedriver_win32/chromedriver.exe')
browser = webdriver.Chrome(service=s)
url = 'https://www.saucedemo.com/'
browser.maximize_window()
browser.get(url)
input_username = browser.find_element(By.ID, 'user-name')
if input_username is None:
    print("Элемент не найден")
else:
    print("Элемент найден")