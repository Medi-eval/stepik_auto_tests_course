from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    # successful_link = 'http://suninjuly.github.io/registration1.html'

    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
    input1.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "third")
    input3.send_keys("abcd")
    input3 = browser.find_element(By.CSS_SELECTOR, ".second_block .first")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block .second")
    input4.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
