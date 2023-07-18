import json
import os
import time
import traceback

import ipdb
import pytest
import selenium
from pytest_bdd import given, then, parsers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pageObjects.base import BasePage
from pageObjects.form_authentication_page import FormAuthenticationPage

explicit_wait = 0
username= ""
password= ""


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture(scope='session')
def config(request):
    global explicit_wait
    global username, password

    BROWSERS = ['Chrome', 'Firefox']

    # Read config file
    with open('src/config.json') as config_file:
        config = json.load(config_file)
    browser = config['browser']
    username = config['username']
    password = config['password']
    # browser = request.config.option.browser
    # if browser is not None:
    #    config['browser'] = browser

    # set explicit wait time to global varible
    explicit_wait = config['explicit_wait']

    # Assert values are acceptable
    assert config['browser'] in BROWSERS
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make call wait up to 10 seconds for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the teardown
    driver.quit()


@pytest.fixture
def datatable():
    return DataTable()


class DataTable(object):

    def __init__(self):
        pass

    def __str__(self):
        dt_str = ''
        for field, value in self.__dict__.items():
            dt_str = f'{dt_str}\n{field} = {value}'
        return dt_str

    def __repr__(self) -> str:
        return self.__str__()


@given(parsers.parse('I have navigated to the paperMerge "{page_name}" page'), target_fixture='navigate_to')
def navigate_to(browser, page_name):
    url = BasePage.PAGE_URLS.get(page_name.lower())
    browser.get(url)


@given(parsers.parse('I have navigated to the paperMerge LoggedIn page'), target_fixture='navigate_to_login_page')
def navigate_to_login_page(browser):
    FormAuthenticationPage(browser).enter_username(username)
    FormAuthenticationPage(browser).enter_password(password)
    FormAuthenticationPage(browser).click_login_button()
    time.sleep(2)
    assert "Successfully signed in as admin." == FormAuthenticationPage(browser).get_success_login_text().replace("×\n",
                                                                                                                  "")


@then(parsers.parse('a "{text}" banner is displayed in the top-right corner of the page'))
def verify_banner_text(browser, text):
    url = 'https://github.com/tourdedave/the-internet'
    assert text == BasePage(browser).get_github_fork_banner_text()
    assert url == BasePage(browser).get_github_fork_banner_link()
    styleAttrs = BasePage(browser).get_github_fork_banner_position().split(";")
    for attr in styleAttrs:
        if attr.startswith("position"):
            assert "absolute" == attr.split(": ")[1]
        if attr.startswith("top"):
            assert "0px" == attr.split(": ")[1]
        if attr.startswith("right"):
            assert "0px" == attr.split(": ")[1]
        if attr.startswith("border"):
            assert "0px" == attr.split(": ")[1]


@then(parsers.parse('the page has a footer containing "{text}"'))
def verify_footer_text(browser, text):
    assert text == BasePage(browser).get_page_footer_text()


@then(parsers.parse('the link in the page footer goes to "{url}"'))
def verify_footer_link_url(browser, url):
    assert url == BasePage(browser).get_page_footer_link_url()


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """Called when step function failed to execute"""

    # Get the current scenario name
    scenario_name = scenario.name
    scenario_name = scenario_name.replace('"', '').replace(' ', '-')

    # Get the current step name
    step_name = step.name
    step_name = step_name.replace('"', '').replace(' ', '-')

    # Check if the scenario has a corresponding Jira ticket

    print("-------Test Failed-------")
    """Called when step function fails to execute"""
    screenshot_dir = "reports/failures/"
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_filename = f'{scenario_name}_{step_name}.png'
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
    # browser.save_screenshot(screenshot_path)

    # Get the exception message and stack trace
    exception_type = type(exception).__name__
    exception_message = str(exception)
    exception_traceback = traceback.format_tb(exception.__traceback__)

    # Print the failure details to the console
    print('\033[91m' + '\n' + '=' * 80)
    print('\033[91m' + f'FAILURE: {scenario_name} -> {step_name}')
    print('\033[91m' + f'Type: {exception_type}')
    print('\033[91m' + f'Message: {exception_message}')
    print('\033[91m' + f'Traceback: {exception_traceback}')
    print('\033[91m' + f'Screenshot: {screenshot_path}')
    print('\033[91m' + '=' * 80 + '\n')
    screen_shot = scenario_name + step_name + ".png"
    # xml = browser.driver.page_source
    # xmlwriter(scenario_name, xml)
