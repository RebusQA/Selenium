
import time
import allure

from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger


class Payment_page(Base):

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver


    """ Locators """

    confirm_pay_locator = "//button[@id='place_order']"


    """ Getters """

    def get_confirm_pay(self):
        return self.driver.find_element(By.XPATH, self.confirm_pay_locator)


    """ Actions """

    def click_confirm_pay(self):
        self.get_confirm_pay().click()
        print("Click confirm pay button")


    """ Methods """

    def payment_confirm(self):

        with allure.step("Payment confirm"):
            Logger.add_start_step(method="payment_confirm")
            self.get_current_url()
            self.click_confirm_pay()
            time.sleep(3)
            Logger.add_end_step(url=self.driver.current_url, method="payment_confirm")