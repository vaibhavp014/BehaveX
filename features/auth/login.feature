Feature: Login functionality
  As a user
  I want to be able to log in to the application
  So that I can access the dashboard

  Scenario: Valid login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard
