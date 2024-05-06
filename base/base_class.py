import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver


    """ Получение и возврат текущей url """

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url is: " + get_url)

    """ Проверка по элементу после авторизации """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Value word is ok")

    """ Метод, который будет парсить url """

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Final url is: " + get_url)


    """ Метод, который будет делать скрин конечной страницы """

    def get_screenshot(self):

        # Создание скриншота
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = "screenshot " + now_date + ".png"
        # ./screen - точка указывает на текущий каталог, то есть система найдёт в этом проекте папку screen
        self.driver.save_screenshot(f"./screen/{name_screenshot}")
        print("Screenshot done")
