
import time
import allure

from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    cart_url = "https://zrdshop.ru/cart/"

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver


    """ Locators """

    create_order_locator = "//*[@id='post-10']/div/div[2]/div[2]/div/a"


    """ Getters """

    def get_create_order(self):
        return self.driver.find_element(By.XPATH, self.create_order_locator)

    """ Actions """

    def click_create_order(self):
        create_order = self.get_create_order()
        create_order.click()
        print("Click create order")
        time.sleep(3)


    """ Methods """

    def order_product(self):

        # Подключаю в метод Allure
        with allure.step("Order product"):
            # Обращаюсь к классу Logger и вызываю до начала теста
            Logger.add_start_step(method="order_product")
            # Открытие страницы
            self.driver.get(self.cart_url)
            # Максимизация окна браузера
            self.driver.maximize_window()
            # Получение текущего URL в терминале
            self.get_current_url()
            # Нажатие на поле поиска
            self.click_create_order()
            time.sleep(3)
            # Обращаюсь к классу Logger и вызываю после завершения теста
            Logger.add_end_step(url=self.driver.current_url, method="order_product")