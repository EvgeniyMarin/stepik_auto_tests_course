from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.CSS_SELECTOR, 'button[type="submit"].btn').click()
confirm = browser.switch_to.alert
confirm.accept()
x_element = browser.find_element(By.ID, "input_value").text


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.find_element(By.CSS_SELECTOR, "input.form-control").send_keys(calc(x_element))
browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(10)