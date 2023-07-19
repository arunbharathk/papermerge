import time

import ipdb
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
    SELECT_EMPTY_PAGE = (
        By.XPATH, "/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div/div[2]/div/div[1]/ul/li[2]/div[4]")
    DELETE_PAGE_OPTION = (By.ID, "delete-page")
    TOTAL_PAGE_NUMBER = (By.CSS_SELECTOR, "li.page_thumbnail")
    CLICK_FILTER = (By.ID, "dropdown_order_opt")
    SELECT_DOC = (By.XPATH, "//*[@id='browse']/table/tbody/tr/td[1]/input")
    SELECT_VIEW_FILTER = (By.XPATH, "//*[@id='display-mode']/div[1]")
    SELECT_LIST_VIEW = (By.XPATH, "//*[@id='display-mode']/div[1]/div/a[2]")
    DELETE_DOC = (By.ID,"delete")

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
        find_element(self.browser, *self.DOCUMENT).click()
        return True

    def click_left_pane(self):
        return find_element(self.browser, *self.LEFT_PANE).click()

    def get_select_page(self):
        return find_element(self.browser, *self.SELECT_EMPTY_PAGE)

    def get_total_page_number(self):
        return self.browser.find_elements(*self.TOTAL_PAGE_NUMBER)

    def select_delete_option(self):
        return find_element(self.browser, *self.DELETE_PAGE_OPTION)

    def select_document(self):
        return find_element(self.browser, *self.SELECT_DOC)

    def select_view_filter(self):
        time.sleep(2)
        find_element(self.browser, *self.SELECT_VIEW_FILTER)
        time.sleep(2)
        find_element(self.browser,*self.SELECT_LIST_VIEW)
        return True

    def get_delete_document(self):
        return find_element(self.browser,*self.DELETE_DOC)