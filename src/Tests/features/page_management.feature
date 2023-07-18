
Feature: Page Management
  As a user of Papermerge
  I want to be able to upload files into the application
  So that I can work and organize my documents effectively

    Background: Open PaperMerge document page
    Given I have navigated to the paperMerge "Form Authentication" page
    Given I have navigated to the paperMerge LoggedIn page

  Scenario: Uploading a file
    Given I am on the Papermerge application
    And A upload button should be displayed
    When I upload a file
    Then the file should be successfully uploaded
    And the uploaded file should be visible in the document list

  @test
  Scenario: Open and Delete the empty page in the file
    Given the file should be available in the document list
    And I open the document
    And I select the page using right click
    And I can delete the page
    Then Document should rearrage properly
