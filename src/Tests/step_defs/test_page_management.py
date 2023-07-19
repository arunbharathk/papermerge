import os
import time

import ipdb
from pytest_bdd import scenarios, when, given, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.base import BasePage
from pageObjects.form_authentication_page import FormAuthenticationPage
from pageObjects.page_management import PageManagement

scenarios('../features/page_management.feature')

previousDocuCount = 0
totalPageNumber = 0


@given("I am on the Papermerge application")
def verify_user_loggedIn(browser):
    global previousDocuCount
    elements = browser.find_elements(By.CSS_SELECTOR,
                                     "li.node.ui-widget-content.node-w1.d-flex.flex-column.align-items-center")
    previousDocuCount = len(elements)
    assert "Successfully signed in as admin." == FormAuthenticationPage(browser).get_success_login_text().replace("×\n",
                                                                                                                  "")


@given("A upload button should be displayed")
def verify_upload_option_visible(browser):
    assert True == PageManagement(browser).is_upload_button_displayed()


@when("I upload a file")
def upload_file(browser):
    # Find the file input element on the web page
    browser.execute_script("document.getElementById('id_file_name').removeAttribute('hidden');")
    time.sleep(2)
    element = PageManagement(browser).get_choose_file_button()
    relative_path = "src/testData/pageMergeDocu.pdf"
    full_path = os.path.abspath(os.path.join(os.getcwd(), relative_path))
    element.send_keys(full_path)


@then("the file should be successfully uploaded")
def verify_file_uploaded(browser):
    assert True == PageManagement(browser).is_upload_success_displayed()


@then("the uploaded file should be visible in the document list")
def step_then_uploaded_file_visible(browser):
    time.sleep(3)
    elements = browser.find_elements(By.CSS_SELECTOR,
                                     "li.node.ui-widget-content.node-w1.d-flex.flex-column.align-items-center")
    latestDocuCount = len(elements)
    assert previousDocuCount + 1 == latestDocuCount


@given('the file should be available in the document list')
def verify_file_availbility(browser):
    assert True == PageManagement(browser).is_document_available()


@given('I open the document')
def open_the_document(browser):
    response = PageManagement(browser).open_the_document()
    assert response, "The click action was not successful."


@when('I right click and delete the last page')
def select_empty_page(browser):
    global totalPageNumber
    PageManagement(browser).click_left_pane()
    time.sleep(2)
    totalPageNumber = len(PageManagement(browser).get_total_page_number())
    element = PageManagement(browser).get_select_page()
    element.click()
    # Create an instance of ActionChains
    actions = ActionChains(browser)

    # Perform the right-click action on the element
    actions.context_click(element).perform()

    # Find the "Delete" option in the context menu and click on it
    delete_option = PageManagement(browser).select_delete_option()
    actions.click(delete_option).perform()
    # Switch the focus to the alert popup
    alert = browser.switch_to.alert

    # Accept the alert (click OK)
    alert.accept()


@then('Document should rearrage properly')
def verify_document_rearrange(browser):
    # get the latest page number after deletion
    Lelement = len(PageManagement(browser).get_total_page_number())
    assert int(Lelement) + 1 == int(totalPageNumber)


@given('Delete the uploaded document')
def delete_document(browser):
    PageManagement(browser).select_view_filter()
    element = PageManagement(browser).select_document()
    element.click()
    # Create an instance of ActionChains
    actions = ActionChains(browser)

    # Perform the right-click action on the element
    actions.context_click(element).perform()

    # Find the "Delete" option in the context menu and click on it
    delete_option = PageManagement(browser).get_delete_document()
    actions.click(delete_option).perform()
    # Switch the focus to the alert popup
    alert = browser.switch_to.alert

    # Accept the alert (click OK)
    alert.accept()
