import os
import time

import ipdb
from pytest_bdd import scenarios, when, given, then
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.form_authentication_page import FormAuthenticationPage
from pageObjects.page_management import PageManagement

scenarios('../features/page_management.feature')

previousDocuCount = 0


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
    element.send_keys('/Users/savitha/PycharmProjects/paperMergeTest/src/testData/recp1.pdf')


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


@when('I open the document')
def open_the_document(browser):

    assert True == PageManagement(browser).open_the_document().click()



@when('I select the page using right click')
def select_empty_page(browser):
    assert True == PageManagement(browser).click_left_pane()



#    ipdb.set_trace()


#    element = browser.find_element(By.XPATH, "//li[contains(@class, 'last')]/div[@class='page_number']")
##    page_number = element.text
#    print(page_number)

#    element = browser.find_element(By.XPATH, "//li[contains(@class, 'last')]/div[@class='page_number']").click()

    # Create an instance of ActionChains
#    actions = ActionChains(browser)

    # Perform the right-click action on the element
#    actions.context_click(element).perform()

    # Find the "Delete" option in the context menu and click on it
#    delete_option = browser.find_element(By.ID, "delete-page")
#    actions.click(delete_option).perform()

    # Switch the focus to the alert popup
#    alert = browser.switch_to.alert

    # Accept the alert (click OK)
#    alert.accept()

 #   Afterelement = browser.find_element(By.XPATH, "//*[@id='page-thumbnails']/ul/li/div[4]")
 #   page_number = Afterelement.text
 #   print(page_number)
