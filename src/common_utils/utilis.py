from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from conftest import explicit_wait


def get_element_text(browser, locator):
    """Get the text of an element using the locator received via argument"""
    try:
        element = get_element_if_visible(browser, locator)
        assert element is not None, "Assert Failed: Element Not found"
        return element.text
    except TimeoutException as e:
        print('\033[31;2m' + "Timeout occurred while waiting for element:", str(e) + '\033[0m')
        raise e
    except NoSuchElementException as e:
        print('\033[31;2m' + "Element not found:", str(e) + '\033[0m')
        raise e
    except ElementNotInteractableException as e:
        print('\033[31;2m' + "Element is not interactable:", str(e) + '\033[0m')
        raise e
    except Exception as e:
        print('\033[31;2m' + "An error occurred:", str(e) + '\033[0m')
        raise e


def get_element_if_visible(browser, locator, locator_value):
    try:
        given_element = WebDriverWait(browser.driver, explicit_wait).until(
            ec.visibility_of_element_located((locator, locator_value)))
        if given_element.is_displayed() and given_element.is_enabled():
            return given_element
        else:
            print('\033[31;2m' + "Element is not visible or enabled." + '\033[0m')
    except TimeoutException as e:
        raise e
    except NoSuchElementException as e:
        raise e
    except Exception as e:
        raise e


def find_element(browser, locator_id, locator_value):
    try:
        if locator_id.upper() == "XPATH":
            return WebDriverWait(browser, 60).until(
                ec.presence_of_element_located((By.XPATH, locator_value)))
        elif locator_id.upper() == "ID":
            return WebDriverWait(browser, 60).until(
                ec.presence_of_element_located((By.ID, locator_value)))
    except TimeoutException:
        raise AssertionError(f"Element not found: {locator_value}")
    except Exception as e:
        #printOnException(e)
        raise e