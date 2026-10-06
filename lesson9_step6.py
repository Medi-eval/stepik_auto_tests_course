import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def Stepik(code):
    link = "https://stepik.org/lesson/184253/step/6?unit=158843"
    browser.get(link)
    time.sleep(15)

    button_1 = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
    button_1.click()

    login = browser.find_element(By.ID, "id_login_email")
    login.send_keys("alexandrdu1997@mail.ru")
    password = browser.find_element(By.ID, "id_login_password")
    password.send_keys("qazsw_192001")
    autorisation = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
    autorisation.click()
    time.sleep(5)

    continue_button = browser.find_element(By.CSS_SELECTOR, "button.button")
    continue_button.click()
    time.sleep(3)

    answer = browser.find_element(By.TAG_NAME, "textarea")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(code)
    button_2 = browser.find_element(By.CSS_SELECTOR, "button.attempt-wrapper-button")
    browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_2)
    time.sleep(1)
    button_2.click()


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(2)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(y)

    button_2 = browser.find_element(By.TAG_NAME, "button")
    button_2.click()
    time.sleep(3)

    alert = browser.switch_to.alert
    alert_text = alert.text.split(": ")[-1]
    alert.accept()
    Stepik(alert_text)

finally:
    time.sleep(10)
    browser.quit()
