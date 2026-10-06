import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Enter first name']"
    )
    input1.send_keys("Ivan")
    input2 = browser.find_element(
        By.CSS_SELECTOR, "input[placeholder='Enter last name']"
    )
    input2.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Enter email']")
    input2.send_keys("Ivan")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "Abc.txt")

    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
