from pages.locators import *
from pages.waiter import Waiter
import time


class LoginToMail:
    @staticmethod
    def load_login_page(driver, web_url):

        try:
            driver.get(web_url)
            return True
        except:
            print("Page Not Found")
            return False

    @staticmethod
    def add_user_name(driver, user_name):

        Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_user_name)
        try:
            username_find_element = driver.find_element_by_xpath(xpath_for_user_name)
            username_find_element.send_keys(user_name)
        except:
            print("User Name Locator Not Found")

    @staticmethod
    def click_next_button(driver):
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_next_button)
            driver.find_element_by_xpath(xpath_for_next_button).click()
        except Exception as e:
            print("Locator not found \n", e)

    @staticmethod
    def add_password(driver, password):
        Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_password)
        password_find_element = driver.find_element_by_xpath(xpath_for_password)
        password_find_element.send_keys(password)

    @staticmethod
    def click_sign_in_button(driver):
        Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_signin_button)
        driver.find_element_by_xpath(
            xpath_for_signin_button).click()

    @staticmethod
    def landing_inbox_screen(driver):
        try:
            driver.find_element_by_xpath(xpath_for_done_button_on_theme_popup)
            print("User successfully logged IN")
        except:

            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_compose_email_button)
            driver.find_element_by_xpath(xpath_for_compose_email_button)
            print("User successfully logged IN")

    @staticmethod
    def check_error_message_for_invalid_user_name(driver):
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_invalid_username_message)
            message = driver.find_element_by_xpath(xpath_for_invalid_username_message).text
            driver.close()
            return message
        except Exception as e:
            print("Locator not found \n", e)
            return False

    @staticmethod
    def check_error_message_for_invalid_password(driver):
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_invalid_password_message)
            message = driver.find_element_by_xpath(xpath_for_invalid_password_message).text
            driver.close()
            return message
        except Exception as e:
            print("Locator not found \n", e)

    @staticmethod
    def logout_user(driver):
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_user_setting_button)
            open_user_option = driver.find_element_by_xpath(xpath_for_user_setting_button).click
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_logout_button)
            click_on_signout = driver.find_element_by_xpath(xpath_for_logout_button).click
            driver.close()
            return True
        except Exception as e:
            print("Locator not found \n", e)
            return False
