
import allure

from base.base_class import Base
from utilities.logger import Logger


class Finish_page(Base):


    """ Methods """

    def finish(self):

        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")