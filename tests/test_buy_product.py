
import time
import allure

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.cart_page import Cart_page
from pages.client_info_page import Client_info_page
from pages.finish_page import Finish_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

@allure.description("Test buy product")
def test_buy_product(set_up):

        # Очистка терминала от лишних сообщений
        options = Options()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

        # Вызов методов с шагами теста
        login = Login_page(driver)
        login.authorization()

        mp = Main_page(driver)
        mp.select_product()

        cp = Cart_page(driver)
        cp.order_product()

        cip = Client_info_page(driver)
        cip.payment_details()

        pp = Payment_page(driver)
        pp.payment_confirm()
        time.sleep(7)

        fp = Finish_page(driver)
        fp.finish()

        driver.quit()