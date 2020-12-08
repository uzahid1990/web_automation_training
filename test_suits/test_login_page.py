from pages.launch_browsers import GetBrowser
from helpers.config_reader import JsonParser
from pages.login_into_yahoo_mail import LoginToMail
import pytest


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
@pytest.mark.dependency()
def test_login_page_with_success_scenario(params):
    print("----------------------Running Success Scenario----------------------")
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
    login_class_object.landing_inbox_screen(driver)
    test_login = login_class_object.logout_user(driver)
    assert test_login is True

@pytest.mark.smoke
@pytest.mark.dependency(depends=['test_login_page_with_success_scenario'])
def test_login_page_with_invalid_username(params):
    print("----------------------Running Invalid Scenario----------------------")
    login_parameters = JsonParser().read_json('login')
    web_url = login_parameters[0]
    user_name = login_parameters[3]
    if params == 'chrome':
        driver = GetBrowser().launch_firefox_browser()
    else:
        driver = GetBrowser().launch_chrome_browser()
    driver.get(web_url)
    login_class_object.load_login_page(driver, web_url)
    login_class_object.add_user_name(driver, user_name)
    login_class_object.click_next_button(driver)
    message = login_class_object.check_error_message_for_invalid_user_name(driver)
    assert message == "Sorry, we don't recognize this email."

@pytest.mark.invalid_login
@pytest.mark.dependency(depends=['test_login_page_with_success_scenario'])
def test_login_page_with_invalid_password(params):
    print("----------------------Running Invalid Scenario----------------------")
    login_parameters = JsonParser().read_json('login')
    web_url = login_parameters[0]
    user_name = login_parameters[1]
    password = login_parameters[4]
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
    message = login_class_object.check_error_message_for_invalid_password(driver)
    assert message == 'Invalid password. Please try again'
