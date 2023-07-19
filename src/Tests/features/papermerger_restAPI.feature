@restapi  @sanity
Feature: Testing REST API functionality of PaperMerger

  Background:
    Given I have a REST API token

  Scenario: Retrieve all documents
    When I make a GET request to retrieve all documents
    Then I should receive a 2XX response


  #This Test Case will fail, I'm getting 404 when try to upload, due to limit of resource documentation, I couldn't debug more
  Scenario: Upload a local file without specifying the remote name
    When I upload a local file without specifying the remote name
    Then the uploaded file should have the same name as the local file