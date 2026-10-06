from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

img_chest = browser.find_element(By.TAG_NAME, "img")
x_element = img_chest.get_attribute("valuex")
x = int(x_element)
y = calc(x)

try:
    input4 = browser.find_element(By.ID, "answer")
    input4.send_keys(y)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radiobuttons = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    radiobuttons.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
