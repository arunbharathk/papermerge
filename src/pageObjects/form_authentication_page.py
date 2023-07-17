from selenium.webdriver.common.by import By

from common_utils.utilis import find_element
from pageObjects.base import BasePage


class FormAuthenticationPage(BasePage):
    # @property
    # def PAGE_TITLE(self):
    #    return By.XPATH, '//title'

    USERNAME = (By.ID, "id_login")
    PASSWORD = (By.ID, "id_password")
    LOGIN_BUTTON = (By.XPATH, "//button[text() = 'Sign In']")
    DROP_DOWN_LINK = (By.XPATH, "/html/body/div[1]/nav/ul[2]/li/a/div")
    LOGOUT_BUTTON = (By.XPATH, "//li[@class='dropdown-item']/a[contains(text(), 'Log out')]")
    CONFIRM_LOGOUT_BUTTON = (
        By.XPATH, "//button[contains(@class, 'btn btn-success m-3') and contains(text(), 'Yes, sign out')]")
    SIGNOUT_MESSAGE = (By.XPATH,
                       "//div[contains(@class, 'alert alert-success alert-dismissible') and contains(text(), 'You have signed out')]")
    MESSAGE_BANNER = (By.XPATH, '/html/body/div[2]/div/div/form/div[1]')
    PAGE_TITLE = (By.XPATH, "/html/head/title")

    def __init__(self, browser):
        self.browser = browser

    def get_page_title_text(self):
        return find_element(self.browser, *self.PAGE_TITLE).text

    def click_login_button(self):
        return find_element(self.browser, *self.LOGIN_BUTTON).click()

    def is_message_banner_displayed(self):
        return self.browser.find_element(*self.MESSAGE_BANNER).is_displayed()

    def enter_username(self, username):
        print("*******************", *self.USERNAME)
        find_element(self.browser, *self.USERNAME).send_keys(username)

    def enter_password(self, password):
        find_element(self.browser, *self.PASSWORD).send_keys(password)

    def is_logout_button_displayed(self):
        # Click on the dropdown menu to expand it
        find_element(self.browser, *self.DROP_DOWN_LINK).click()
        return find_element(self.browser, *self.LOGOUT_BUTTON).is_displayed()

    def click_logout_button(self):
        return find_element(self.browser, *self.LOGOUT_BUTTON).click()

    def click_confirm_logout(self):
        return find_element(self.browser, *self.CONFIRM_LOGOUT_BUTTON).click()

    def get_current_url(self):
        return self.browser.current_url

    def is_confirm_logout_button_displayed(self):
        return find_element(self.browser, *self.CONFIRM_LOGOUT_BUTTON).is_displayed()

    def logout_message_text(self):
        return find_element(self.browser, *self.SIGNOUT_MESSAGE).text

    def get_message_banner_text(self):
        # Full text includes 'x' to close the message so need to strip this off
        return find_element(self.browser,*self.MESSAGE_BANNER).text

    def get_message_banner_colour(self):
        return find_element(self.browser,*self.MESSAGE_BANNER).value_of_css_property('background-color')
