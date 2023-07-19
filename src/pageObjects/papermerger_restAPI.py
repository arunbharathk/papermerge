import os

import requests

from pageObjects.base import BasePage


class Papermerger_restAPI(BasePage):
    getDocUrl = "http://localhost:8000/api/documents"
    uploadDocUrl = "http://localhost:8000/api/document/upload/"
    apiToken = "26667911a44c56249913c063b7d22b43"

    def __init__(self, browser):
        self.browser = browser

    def get_documents(self):
        headers = {"Authorization": f"Token {self.apiToken}"}
        response = requests.get(self.getDocUrl, headers=headers)
        return response

    def upload_local_file_without_name(self):
        # Perform a file upload without specifying the remote name
        relative_path = "src/testData/no-name.pdf"
        full_path = os.path.abspath(os.path.join(os.getcwd(), relative_path))
        headers = {"Authorization": f"Token {self.apiToken}"}
        files = {"file": open(full_path, "rb")}
        response = requests.put(self.uploadDocUrl, headers=headers, files=files)
        return response

    def get_api_token(self):
        return self.apiToken
