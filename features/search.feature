Feature: Google Search Functionality

  Scenario: Search for 'Selenium Python' on Google
    Given I open the browser and go to "https://www.google.com"
    When I search for "Selenium Python"
    Then I should see results related to "Selenium Python"