from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://stepik.org/lesson/181384/step/8?unit=156009"

browser = webdriver.Chrome()
browser.implicitly_wait(15)
browser.get(link)

def autorisation_in_Stepik(x):
    try:
        button_1 = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
        button_1.click()

        login = browser.find_element(By.ID, "id_login_email")
        login.send_keys("alexandrdu1997@mail.ru")
        password = browser.find_element(By.ID, "id_login_password")
        password.send_keys("qazsw_192001")
        autorisation = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn")
        autorisation.click()

        continue_button = browser.find_element(By.CSS_SELECTOR, "button.button")
        continue_button.click()

        answer = browser.find_element(By.TAG_NAME, "textarea")
        browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
        answer.send_keys(x)
        button_2 = browser.find_element(By.CSS_SELECTOR, "button.attempt-wrapper-button")
        browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_2)
        button_2.click()

    finally:
        browser.quit()    