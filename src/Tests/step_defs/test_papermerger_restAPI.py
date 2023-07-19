import ipdb
from pytest_bdd import when, then, scenarios, given

from pageObjects.papermerger_restAPI import Papermerger_restAPI

scenarios('../features/papermerger_restAPI.feature')

context = {}
response: any


@when("I make a GET request to retrieve all documents")
def get_all_documents(browser):
    # Perform a GET request to retrieve all documents
    context['response'] = Papermerger_restAPI(browser).get_documents()
    response = context['response']
    data = response.json()
    numberOfDocu = len(data)
    if numberOfDocu > 0:
        title = data[0]['title']
        assert title is not None
    else:
        pass


@then("I should receive a 2XX response")
def receive_2xx_response():
    assert context['response'].status_code // 100 == 2


@when("I upload a local file without specifying the remote name")
def upload_local_file_without_name(browser):
    global response
    response = Papermerger_restAPI(browser).upload_local_file_without_name()
    assert response.status_code == 200


@then("the uploaded file should be placed in the Inbox")
def uploaded_file_in_inbox():
    pass


@given('I have a REST API token')
def get_api_token(browser):
    assert Papermerger_restAPI(browser).apiToken is not None

