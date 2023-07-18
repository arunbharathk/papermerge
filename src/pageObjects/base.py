from abc import abstractmethod


class BasePage():
    BASE_URL = "http://localhost:8000"

    PAGE_URLS = {
        "home": BASE_URL + "/",
        "checkboxes": BASE_URL + "/checkboxes",
        "dropdown": BASE_URL + "/dropdown",
        "dynamic controls": BASE_URL + "/dynamic_controls",
        "form authentication": BASE_URL + "/accounts/login/",
        "inputs": BASE_URL + "/inputs",
        "secure area": BASE_URL + "/secure"
    }

    @property
    @abstractmethod
    def PAGE_TITLE(self):
        pass

    @abstractmethod
    def get_page_title_text(self):
        pass
