import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_exist_add_to_cart_button(browser):
	# переход на нужную страницу
    browser.get(link)
    #time.sleep(30)
	# поиск кнопки добавления товара в корзину
    time.sleep(30)
    WebDriverWait(browser, 3).until(
		EC.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "No add to cart button on page")
