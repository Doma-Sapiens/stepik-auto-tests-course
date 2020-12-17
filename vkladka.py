from selenium import webdriver
import time 
import math


link = "http://suninjuly.github.io/redirect_accept.html" # переходим по ссылке
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_tag_name("button")  # жмем кнопку 
button.click()

new_window = browser.window_handles[1]   # находим вкладку
browser.switch_to.window(new_window)     # переходим на нее

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) # математика


x_element = browser.find_element_by_id("input_value") 
x = x_element.text
y = calc(x)

input1 = browser.find_element_by_id("answer") # находим поле
input1.send_keys(y)                           # вставляем значение у

button = browser.find_element_by_tag_name("button") # кликаем кнопку
button.click()