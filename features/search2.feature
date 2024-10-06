Feature: Google Search Functionality

  Scenario: Search for 'Selenium Java' on Google
    Given I open the browser and go to "https://www.google.com"
    When I search for "Selenium Java"
    Then I should see results related to "Selenium Java"