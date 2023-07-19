@page_management  @sanity
Feature: Page Management
  As a user of Papermerge
  I want to be able to upload files into the application
  So that I can work and organize my documents effectively

    Background: Open PaperMerge document page
    Given I have navigated to the paperMerge LoggedIn page

  Scenario: Uploading a file
    Given I am on the Papermerge application
    And A upload button should be displayed
    When I upload a file
    Then the file should be successfully uploaded
    And the uploaded file should be visible in the document list


  Scenario: Open and Delete the empty page in the file
    Given the file should be available in the document list
    And I open the document
    When I right click and delete the last page
    Then Document should rearrage properly

  #We can have Test Tear down after this feature will clear the uploaded documents
  #Which will benefit the automation performance as well data clarity.
  #Easy way to clear using API but I couldn't found that in documents.