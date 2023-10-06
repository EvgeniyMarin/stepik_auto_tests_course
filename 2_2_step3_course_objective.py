from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
browser.find_element(By.CSS_SELECTOR, "button.trollface").click()     
print("Имена вкладок ниже в виде списка")
print(browser.window_handles)
new_window = browser.window_handles[1]                               
browser.switch_to.window(new_window)                                  
x_element = browser.find_element(By.ID, "input_value").text



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser.find_element(By.ID, "answer").send_keys(calc(x_element))
browser.find_element(By.CSS_SELECTOR, "button.btn").click()
time.sleep(10)
