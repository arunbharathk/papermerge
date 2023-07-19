import time

from pytest_bdd import scenarios, when, then, parsers

from pageObjects.base import BasePage
from pageObjects.form_authentication_page import FormAuthenticationPage

scenarios('../features/form_authentication_page.feature')


@when(parsers.parse('I enter a username of "{username}"'))
def enter_username(browser, username):
    FormAuthenticationPage(browser).enter_username(username)


@when(parsers.parse('I enter a password of "{password}"'))
def enter_password(browser, password):
    FormAuthenticationPage(browser).enter_password(password)


@when('I click the Login button')
def click_login_button(browser):
    FormAuthenticationPage(browser).click_login_button()


@then(parsers.parse('I should see success login text "{title}"'))
def verify_login_message(browser, title):
    time.sleep(2)
    assert title == FormAuthenticationPage(browser).get_success_login_text().replace("×\n", "")


@then(parsers.parse('a {colour} "{message}" message banner is displayed'))
def verify_message_text_and_colour(browser, config, colour, message):
    assert colour in ['red', 'green']
    if config['browser'] == 'Firefox':
        expected_colour = 'rgb(198, 15, 19)' if colour == 'red' else 'rgb(93, 164, 35)'
    else:
        expected_colour = 'rgba(220, 53, 69, 1)' if colour == 'red' else 'rgba(93, 164, 35, 1)'
    assert True == FormAuthenticationPage(
        browser).is_message_banner_displayed()
    print(FormAuthenticationPage(
        browser).get_message_banner_colour())
    assert expected_colour == FormAuthenticationPage(
        browser).get_message_banner_colour()
    assert message == FormAuthenticationPage(browser).get_message_banner_text()


@then('a Logout button is displayed')
def verify_logout_button_displayed(browser):
    assert True == FormAuthenticationPage(browser).is_logout_button_displayed()


@then(parsers.parse('the "{page}" page opens'))
def verify_page_opens(browser, page):
    assert BasePage.PAGE_URLS.get(page.lower()) == FormAuthenticationPage(browser).get_current_url()


@then('I click Logout button')
def verify_logout_button_func(browser):
    assert True == FormAuthenticationPage(browser).click_logout_button()


@then('I should see confirm logout button')
def verify_confirm_logout_displayed(browser):
    assert True == FormAuthenticationPage(browser).is_confirm_logout_button_displayed()


@then('I click confirm logout button')
def verify_confirm_logout_func(browser):
    assert True == FormAuthenticationPage(browser).click_confirm_logout()


@then(parsers.parse('I should see "{text}"'))
def verify_logout_text_msg(browser, text):
    time.sleep(2)
    assert text.lower() == FormAuthenticationPage(browser).logout_message_text().lower().replace('×\n', '')


@then(parsers.parse('a {colour} "{message}" message banner is displayed'))
def verify_message_text_and_colour(browser, config, colour, message):
    assert colour in ['red', 'green']
    if config['browser'] == 'Firefox':
        expected_colour = 'rgb(198, 15, 19)' if colour == 'red' else 'rgb(93, 164, 35)'
    else:
        expected_colour = 'rgba(220, 53, 69, 1)' if colour == 'red' else 'rgba(93, 164, 35, 1)'
    assert True == FormAuthenticationPage(
        browser).is_message_banner_displayed()
    assert expected_colour == FormAuthenticationPage(
        browser).get_message_banner_colour()
    assert message == FormAuthenticationPage(browser).get_message_banner_text().strip().replace('×\n', '')
