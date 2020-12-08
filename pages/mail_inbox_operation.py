from selenium.webdriver.common.keys import Keys
from pages.locators import *
from pages.waiter import Waiter
import os
import time
import pyautogui


class MailInboxOperation:
    @staticmethod
    def create_and_mark_label(driver, label):
        # selecting email
        try:
            time.sleep(3)
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_mail_checkbox)
            driver.find_element_by_xpath(xpath_for_mail_checkbox).click()

        except Exception as e:
            print("Locator not found \n", e)

        # opening more options
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_mail_menu)
            driver.find_element_by_xpath(xpath_for_mail_menu).click()

        except Exception as e:
            print("Locator not found \n", e)

        # selecting filter option
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_filter_option)
            driver.find_element_by_xpath(xpath_for_filter_option).click()

        except Exception as e:
            print("Locator not found \n", e)

        # clicking on drop down to add new filter
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_filter_dropdown)
            driver.find_element_by_xpath(xpath_for_filter_dropdown).click()

        except Exception as e:
            print("Locator not found \n", e)

        # click on add new filter
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_filter_add_new_filter)
            driver.find_element_by_xpath(xpath_for_filter_add_new_filter).click()

        except Exception as e:
            print("Locator not found \n", e)

        # add text for the new label
        try:
            label = label
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_add_text_in_filter)
            driver.find_element_by_xpath(xpath_for_add_text_in_filter).send_keys(label, Keys.ENTER)

        except Exception as e:
            print("Locator not found \n", e)

        # apply filter
        try:

            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_save_filter)
            driver.find_element_by_xpath(xpath_for_save_filter).click()

        except Exception as e:
            print("Locator not found \n", e)

        try:

            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_for_label_success_message)
            message = driver.find_element_by_xpath(xpath_for_label_success_message).text
            driver.save_screenshot("filter.png")
            driver.close()
            print(message)
            return message
        except Exception as e:
            print("Locator not found \n", e)
            driver.close()
            return False

    @staticmethod
    def compose_and_send_email(driver):

        # click on Compose email button
        try:
            time.sleep(3)
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_to_click_compose_email_button)
            compose_email_button_click = driver.find_element_by_xpath(xpath_to_click_compose_email_button).click()

        except Exception as e:
            print("Locator(Compose email button) not found \n", e)
            return False
        # enter email address
        try:

            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_to_enter_email_address)
            driver.find_element_by_xpath(xpath_to_enter_email_address).send_keys("usman.zahid@northbaysolutions.net")

        except Exception as e:
            print("Locator(email address) not found \n", e)
            return False

        # enter email subject
        try:
            time.sleep(3)
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_to_enter_email_subject)
            driver.find_element_by_xpath(xpath_to_enter_email_subject).send_keys("Email is sent via Selenium Script")

        except Exception as e:
            print("Locator(email subject) not found \n", e)
            return False

        # enter email body
        try:
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_to_enter_email_body)
            driver.find_element_by_xpath(xpath_to_enter_email_body).click()
            driver.find_element_by_xpath(xpath_to_enter_email_body).send_keys("Hi,\n This email is being sent via selenium test script. ")

        except Exception as e:
            print("Locator(email body) not found \n", e)
            return False

        # attach a document
        try:
            time.sleep(5)
            # click on attachment button
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_to_click_on_attachment_button)
            driver.find_element_by_xpath(xpath_to_click_on_attachment_button).click()
            # click on upload file on computer
            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_to_click_upload_file_from_computer)
            driver.find_element_by_xpath(xpath_to_click_upload_file_from_computer).click()
            time.sleep(4)  # waiting for window popup to open
            pyautogui.write(r"C:\Users\usman.zahid\Desktop\Certification\AWS Technical Professional Certificate.jpg")  # path of File
            time.sleep(4)
            pyautogui.press('enter')
            time.sleep(15)

        except Exception as e:
            print("Locator(attachment) not found and attachment not be done\n", e)
            return False

        # click on send email button
        try:

            Waiter().wait_until_to_find_element(driver, 'XPATH', xpath_to_send_email)
            driver.find_element_by_xpath(xpath_to_send_email).click()
            driver.close()
            return True

        except Exception as e:
            print("Locator(send email button) not found \n", e)
            driver.close()
            return False