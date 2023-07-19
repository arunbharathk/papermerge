@form-authentication  @sanity
Feature: Form Authentication Page


    Background: Open Form Authentication page
    Given I have navigated to the paperMerge "Form Authentication" page


  Scenario: Login with valid credentials
    When I enter a Username of "admin"
    And I enter a Password of "admin"
    And I click the Login button
    Then the "home" page opens
    And I should see success login text "Successfully signed in as admin."
    And a Logout button is displayed
    And I click Logout button
    And I should see confirm logout button
    And I click confirm logout button
    Then I should see "You have signed out."


   Scenario: Login with invalid username but invalid password
    When I enter a Username of "arun"
    And I enter a Password of "arun"
    And I click the Login button
    Then a red "The username and/or password you specified are not correct." message banner is displayed