Feature: Login functionality
  As a user
  I want to be able to log in to the application
  So that I can access the dashboard

  Scenario: Valid login
    Given the user is on the login page
    When the user enters valid credentials
    Then the user should be redirected to the dashboard


    Scenario: Unsuccessful Login with Incorrect Password
    Given the user is on the login page
    When the user enters a valid username and an incorrect password
      | Username | Password   |
      | admin    | wrongpass  |
    And the user clicks the login button
    Then the user should see an error message "Invalid credentials"

  Scenario: Unsuccessful Login with Empty Username
    Given the user is on the login page
    When the user enters an empty username and a valid password
      | Username | Password   |
      |          | admin123   |
    And the user clicks the login button
    Then the user should see an error message "Username is required"
#
#  Scenario: Unsuccessful Login with Empty Password
#    Given the user is on the login page
#    When the user enters a valid username and leaves the password field empty
#      | Username | Password |
#      | admin    |          |
#    And the user clicks the login button
#    Then the user should see an error message "Password is required"
#
#  Scenario: Unsuccessful Login with Both Fields Empty
#    Given the user is on the login page
#    When the user leaves both the username and password fields empty
#    And the user clicks the login button
#    Then the user should see error messages indicating both fields are required
