import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from Script_automation_Stepik import autorisation_in_Stepik


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

browser = webdriver.Chrome()
browser.get(link)

try:
    price = browser.find_element(By.ID, "price")
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element(By.ID, "book").click()

    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    answer.send_keys(y)
    submit_button = browser.find_element(By.ID, "solve")
    submit_button.click()

    alert = browser.switch_to.alert

    # autorisation_in_Stepik(alert_text)

finally:
    print(alert.text.split(": ")[-1])
    browser.quit()
