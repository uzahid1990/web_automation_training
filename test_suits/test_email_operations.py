from pages.launch_browsers import GetBrowser
from helpers.config_reader import JsonParser
from pages.mail_inbox_operation import MailInboxOperation
from pages.login_into_yahoo_mail import LoginToMail
import time
import pytest
import random

email_operation_class_object = MailInboxOperation()
login_class_object = LoginToMail()


def get_params():

    get_browser_list = JsonParser().read_json("browsers")
    print("List of scenarios to be executed: ", get_browser_list[0])
    return get_browser_list[0]


@pytest.fixture(params=get_params())
def params(request):
    """
    Fixture is applied to execute test cases dynamically for multiple attributes
    :param request:
    :return: This will return the params from side_by_side_execution_config file and keep itself to execute test cases one by one
    """
    return request.param

@pytest.mark.smoke
@pytest.mark.filter
def test_apply_filter_to_email(params):
    print("----------------------Running Success Scenario----------------------")
    random_num = str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)) + \
                 str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9))
    label = 'QA test label ' + random_num
    print(label)
    login_parameters = JsonParser().read_json('login')
    web_url = login_parameters[0]
    user_name = login_parameters[1]
    password = login_parameters[2]
    if params == 'chrome':
        driver = GetBrowser().launch_firefox_browser()
    else:
        driver = GetBrowser().launch_chrome_browser()
    driver.get(web_url)
    login_class_object.load_login_page(driver, web_url)
    login_class_object.add_user_name(driver, user_name)
    login_class_object.click_next_button(driver)
    login_class_object.add_password(driver, password)
    login_class_object.click_sign_in_button(driver)
    result = email_operation_class_object.create_and_mark_label(driver, label)
    assert result == label + " folder created" or result == 'Filter added. Manage filters'


@pytest.mark.smoke
@pytest.mark.compose_email
def test_compose_and_send_email(params):
    print("----------------------Compose and Send Email----------------------")
    login_parameters = JsonParser().read_json('login')
    web_url = login_parameters[0]
    user_name = login_parameters[1]
    password = login_parameters[2]
    if params == 'chrome':
        driver = GetBrowser().launch_firefox_browser()
    else:
        driver = GetBrowser().launch_chrome_browser()
    driver.get(web_url)
    login_class_object.load_login_page(driver, web_url)
    login_class_object.add_user_name(driver, user_name)
    login_class_object.click_next_button(driver)
    login_class_object.add_password(driver, password)
    login_class_object.click_sign_in_button(driver)
    result = email_operation_class_object.compose_and_send_email(driver)
    assert result is True

