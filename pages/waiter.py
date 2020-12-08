from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Waiter:
    @staticmethod
    def wait_until_to_find_element(driver, locator_type, locator):

        if locator_type == 'XPATH':
            wait = WebDriverWait(driver, 60).until(EC.presence_of_element_located(
                (By.XPATH, locator)))
            return wait
        else:
            print("add more locator Types")
