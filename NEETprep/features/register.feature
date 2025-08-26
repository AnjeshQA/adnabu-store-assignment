Feature: New/Existing User Registration Functionality

  Scenario: Mobile number Registration with new user
    Given As New User I am on the NEETprep New login page
    When As New User I enter my mobile number
    And As New User I click the Send OTP button
    And As New User I enter the OTP
    And As New User I click the OTP button to verify OTP
    And As New User I See regsitration page & click I am new here button
    And As New User I enter Full Name in new user field
    And As New User I enter valid emailID
    And As New User I click Next button & will see account successfully created message
    And As New User I fill board exam year
    And As New User I click Continue button
    And As New User I click Get Started button & Exit buy course page
    Then As New User I will sucessfully land on NEETprep dashbaord


