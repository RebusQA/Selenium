
import time
import allure

from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger

class Client_info_page(Base):

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver


    """ Locators """

    first_name_locator = "//input[@id='billing_first_name']"
    last_name_locator = "//input[@id='billing_last_name']"
    address_locator = "//input[@id='billing_address_1']"
    locality_locator = "//input[@id='billing_city']"
    region_locator = "//input[@id='billing_state']"
    index_locator = "//input[@id='billing_postcode']"
    telephone_locator = "//input[@id='billing_phone']"
    delivery_choice_locator = "//input[@id='shipping_method_0_official_cdek_137']"


    """ Getters """

    def get_first_name(self):
        return self.driver.find_element(By.XPATH, self.first_name_locator)
    def get_last_name(self):
        return self.driver.find_element(By.XPATH, self.last_name_locator)
    def get_address(self):
        return self.driver.find_element(By.XPATH, self.address_locator)
    def get_locality(self):
        return self.driver.find_element(By.XPATH, self.locality_locator)
    def get_region(self):
        return self.driver.find_element(By.XPATH, self.region_locator)
    def get_index(self):
        return self.driver.find_element(By.XPATH, self.index_locator)
    def get_telephone(self):
        return self.driver.find_element(By.XPATH, self.telephone_locator)
    def get_delivery_choice(self):
        return self.driver.find_element(By.XPATH, self.delivery_choice_locator)


    """ Actions """


    def input_first_name(self, first_name):
        self.get_first_name().clear()
        self.get_first_name().send_keys(first_name)
        print("Input first name")
    def input_last_name(self, last_name):
        self.get_last_name().clear()
        self.get_last_name().send_keys(last_name)
        print("Input last name")
    def input_address(self, address):
        self.get_address().clear()
        self.get_address().send_keys(address)
        print("Input address")
    def input_locality(self, locality):
        self.get_locality().clear()
        self.get_locality().send_keys(locality)
        print("Input locality")
    def input_region(self, region):
        self.get_region().clear()
        self.get_region().send_keys(region)
        print("Input region")
    def input_index(self, index):
        self.get_index().clear()
        self.get_index().send_keys(index)
        print("Input index")
    def input_telephone(self, telephone):
        self.get_telephone().clear()
        self.get_telephone().send_keys(telephone)
        print("Input telephone")
        time.sleep(10)
    def click_delivery_choice(self):
        self.get_delivery_choice().click()
        print("Click delivery choice button")
        time.sleep(5)


    """ Methods """

    def payment_details(self):

        with allure.step("Payment details"):
            Logger.add_start_step(method="payment_details")
            self.get_current_url()
            self.input_first_name("Иван")
            time.sleep(3)
            self.input_last_name("Иванов")
            time.sleep(3)
            self.input_address("ул. Любимая, 1")
            time.sleep(3)
            self.input_locality("Михайловск")
            time.sleep(3)
            self.input_region("Ставропольский край")
            time.sleep(3)
            self.input_index("333777")
            time.sleep(3)
            self.input_telephone("83337777777")
            time.sleep(3)
            self.click_delivery_choice()
            time.sleep(3)
            Logger.add_end_step(url=self.driver.current_url, method="payment_details")