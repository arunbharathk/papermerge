from selenium.webdriver.common.by import By

from common_utils.utilis import find_element
from pageObjects.base import BasePage


class PageManagement(BasePage):
    UPLOAD_BUTTON = (By.ID, "id_btn_upload")
    CHOOSE_FILE = (By.ID, "id_file_name")
    UPLOAD_SUCCESS_MSG = (By.ID, "newsHeading")
    DOCUMENT = (
    By.XPATH, "//li[contains(@class, 'node ui-widget-content node-w1 d-flex flex-column align-items-center')][1]")
    LEFT_PANE = (By.ID, "sw-left-panel")

    def __init__(self, browser):
        self.browser = browser

    def is_upload_button_displayed(self):
        return find_element(self.browser, *self.UPLOAD_BUTTON).is_displayed()

    def get_upload_button(self):
        return find_element(self.browser, *self.UPLOAD_BUTTON)

    def get_choose_file_button(self):
        return find_element(self.browser, *self.CHOOSE_FILE)

    def is_upload_success_displayed(self):
        return find_element(self.browser, *self.UPLOAD_SUCCESS_MSG).is_displayed()

    def is_document_available(self):
        return find_element(self.browser, *self.DOCUMENT).is_displayed()

    def open_the_document(self):
        return find_element(self.browser, *self.DOCUMENT)

    def click_left_pane(self):
        return find_element(self.browser, *self.LEFT_PANE).click()
