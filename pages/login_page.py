
import time
import allure

from selenium.webdriver.common.by import By
from base.base_class import Base
from utilities.logger import Logger

class Login_page(Base):

    url = "https://zrdshop.ru/"

    def __init__(self, driver):

        # Инициализация класса-родителя
        super().__init__(driver)
        self.driver = driver


    """ Locators """

    enter_button = "//a[@id='nm-menu-account-btn']"
    login = "//input[@id='username']"
    password = "//input[@id='password']"
    login_button = "//button[@type='submit']"
    main_word = "//li[@class='woocommerce-MyAccount-navigation-link woocommerce-MyAccount-navigation-link--dashboard is-active']"
    shop_button = "//li[@id='menu-item-4772']"


    """ Getters """

    def get_enter_button(self):
        return self.driver.find_element(By.XPATH, self.enter_button)
    def get_login(self):
        return self.driver.find_element(By.XPATH, self.login)
    def get_password(self):
        return self.driver.find_element(By.XPATH, self.password)
    def get_login_button(self):
        return self.driver.find_element(By.XPATH, self.login_button)
    def get_main_word(self):
        return self.driver.find_element(By.XPATH, self.main_word)
    def get_shop_button(self):
        return self.driver.find_element(By.XPATH, self.shop_button)


    """ Actions """

    def click_enter_button(self):
        # Нажатие на кнопку входа
        self.get_enter_button().click()
        print("Click enter account button")
    def input_login(self, login):
        # Ввод почты пользователя
        self.get_login().send_keys(login)
        print("Input email")
    def input_password(self, password):
        # Ввод пароля
        self.get_password().send_keys(password)
        print("Input password")
    def click_login_button(self):
        # Нажатие на кнопку входа
        self.get_login_button().click()
        print("Click login button")

    def click_shop_button(self):
        # Нажатие на кнопку входа в магазин
        self.get_shop_button().click()
        print("Click shop button")


    """ Methods """

    # Метод авторизации пользователя
    def authorization(self):

        # Подключаю в метод Allure
        with allure.step("Authorization"):
            # Обращаюсь к классу Logger и вызываю до начала теста
            Logger.add_start_step(method="authorization")
            # Открытие страницы
            self.driver.get(self.url)
            # Максимизация окна браузера
            self.driver.maximize_window()
            # Получение текущей url в терминале
            self.get_current_url()
            # Нажатие кнопки входа в ЛК
            self.click_enter_button()
            time.sleep(3)
            # Ввод имени пользователя и пароля
            self.input_login("testaqa777@gmail.com")
            time.sleep(3)
            self.input_password("KursiAlexaBest")
            time.sleep(3)
            # Нажатие кнопки входа
            self.click_login_button()
            time.sleep(3)
            # Проверка того, что авторизация прошла успешно, по элементу "Личный кабинет"
            self.assert_word(self.get_main_word(), "Панель управления")
            time.sleep(3)
            # Нажатие кнопки входа в магазин
            self.click_shop_button()
            time.sleep(3)
            # Обращаюсь к классу Logger и вызываю после завершения теста
            Logger.add_end_step(url=self.driver.current_url, method="authorization")