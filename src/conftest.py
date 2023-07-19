import json
import os
import time
import traceback

import ipdb
import pytest
import pytest_html
from pytest_bdd import given, parsers
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pageObjects.base import BasePage
from pageObjects.form_authentication_page import FormAuthenticationPage

implicit_wait = 0
username = ""
password = ""
token = ""


def pytest_addoption(parser):
    parser.addoption("--browser", action="store")


@pytest.fixture(scope='session')
def config(request):
    global implicit_wait
    global token
    global username, password

    BROWSERS = ['Chrome', 'Firefox']

    # Read config file
    with open('src/config.json') as config_file:
        config = json.load(config_file)
    browser = config['browser']
    token = config['token']
    username = config['username']
    password = config['password']
    implicit_wait = config['implicit_wait']

    # Assert values are acceptable
    assert config['browser'] in BROWSERS
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config


@pytest.fixture()
def browser(config):
    # Initialize the WebDriver instance
    if config['browser'] == 'Chrome':
        opts = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    elif config['browser'] == 'Firefox':
        opts = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(
            GeckoDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Make call wait up to 10 seconds for elements to appear
    driver.implicitly_wait(config['implicit_wait'])

    # Return the WebDriver instance for the setup
    yield driver

    # Quit the WebDriver instance for the teardown
    driver.quit()


@given(parsers.parse('I have navigated to the paperMerge "{page_name}" page'), target_fixture='navigate_to')
def navigate_to(browser, page_name):
    url = BasePage.PAGE_URLS.get(page_name.lower())
    browser.get(url)


@given(parsers.parse('I have navigated to the paperMerge LoggedIn page'), target_fixture='navigate_to_login_page')
def navigate_to_login_page(browser):
    url = BasePage.PAGE_URLS.get("Form Authentication".lower())
    browser.get(url)
    FormAuthenticationPage(browser).enter_username(username)
    FormAuthenticationPage(browser).enter_password(password)
    FormAuthenticationPage(browser).click_login_button()
    time.sleep(2)
    assert "Successfully signed in as admin." == FormAuthenticationPage(browser).get_success_login_text().replace("×\n",
                                                                                                                  "")


def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    """Called when step function failed to execute"""

    # Get the current scenario name
    scenario_name = scenario.name
    scenario_name = scenario_name.replace('"', '').replace(' ', '-')

    # Get the current step name
    step_name = step.name
    step_name = step_name.replace('"', '').replace(' ', '-')

    # Use the request fixture to access the browser fixture
    browser = request.getfixturevalue('browser')

    print("-------Test Failed-------")
    """Called when step function fails to execute"""
    screenshot_dir = "reports/failures/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_filename = f'{scenario_name}_{step_name}.png'
    screenshot_path = os.path.join(screenshot_dir, screenshot_filename)
    browser.save_screenshot(screenshot_path)

    # Get the exception message and stack trace
    exception_type = type(exception).__name__
    exception_message = str(exception)
    exception_traceback = traceback.format_tb(exception.__traceback__)

    # Print the failure details to the console
    print('\033[91m' + '\n' + '=' * 80)
    print('\033[91m' + f'FAILURE: {scenario_name} -> {step_name}'+'\n')
    print('\033[91m' + f'Type: {exception_type}'+'\n')
    print('\033[91m' + f'Message: {exception_message}'+'\n')
    print('\033[91m' + f'Traceback: {exception_traceback}'+'\n')
    print('\033[91m' + f'Screenshot: {screenshot_path}'+'\n')
    print('\033[91m' + '=' * 80 + '\n')
