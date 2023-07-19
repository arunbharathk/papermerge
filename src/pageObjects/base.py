from abc import abstractmethod


class BasePage():
    BASE_URL = "http://localhost:8000"

    PAGE_URLS = {
        "home": BASE_URL + "/",
        "form authentication": BASE_URL + "/accounts/login/",
        "secure area": BASE_URL + "/secure"
    }

    @property
    @abstractmethod
    def PAGE_TITLE(self):
        pass

    @abstractmethod
    def get_page_title_text(self):
        pass
