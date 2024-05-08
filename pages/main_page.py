
import time
import allure

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):

    move_to_cart = "https://zrdshop.ru/cart/"


    """ Locators """

    search_field_locator = "//a[@id='nm-shop-search-btn']"
    buy_product_locator = "//*[@id='nm-shop-browse-wrap']/ul/li[2]/div/div[2]/div[1]/h3/a"
    cart_add_locator = "//button[@class='nm-simple-add-to-cart-button single_add_to_cart_button button alt']"
    close_cart_locator = "//span[@class='nm-widget-panel-close-title']"


    """ Getters """

    def get_search_field(self):
        return self.driver.find_element(By.XPATH, self.search_field_locator)
    def get_buy_product(self):
        return self.driver.find_element(By.XPATH, self.buy_product_locator)
    def get_cart_add(self):
        return self.driver.find_element(By.XPATH, self.cart_add_locator)
    def get_close_cart(self):
        return self.driver.find_element(By.XPATH, self.close_cart_locator)

    """ Actions """

    def click_search_field(self):
        search_field = self.get_search_field()
        search_field.click()
        print("Click search field")
        time.sleep(3)

    def input_search(self, keyword):
        search_input = self.driver.find_element(By.XPATH, "//input[@type='text']")
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)
        time.sleep(3)

    def click_buy_product(self):
        buy_product = self.get_buy_product()
        buy_product.click()
        print("Click buy product")

    def click_cart_add(self):
        cart_add = self.get_cart_add()
        cart_add.click()
        print("Click cart add")

    def click_close_cart(self):
        close_cart = self.get_close_cart()
        close_cart.click()
        print("Click close cart")
        time.sleep(3)


    """ Methods """

    def select_product(self):

        # Подключаю в метод Allure
        with allure.step("Select product"):

            Logger.add_start_step(method="select_product")
            self.get_current_url()
            self.click_search_field()
            self.input_search("Носки")
            self.click_buy_product()
            self.click_cart_add()
            self.driver.get(self.move_to_cart)
            self.driver.maximize_window()
            Logger.add_end_step(url=self.driver.current_url, method="select_product")