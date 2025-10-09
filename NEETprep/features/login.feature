Feature: NEETprep Login
  As a NEETprep user
  I want to login using my mobile number and OTP
  So that I can access the NEETprep home page

  @implemented
  Scenario: Successful login with valid mobile number and Valid OTP
    Given I am on the NEETprep login page
    When I enter my mobile number
    And I click the Send OTP button
    And I enter the OTP
    And I click the Verify OTP button
    Then I should see the NEETprep home page

  Scenario: Login with valid mobile number and invalid OTP
    Given I am on the NEETprep login page
    When I enter my mobile number
    And I click the Send OTP button
    And I enter the ivalid OTP
    And I click the Verify OTP button
    Then Proper Error Message should be displayed due to invalid OTP

  Scenario: Login with valid mobile number and without entering OTP
    Given I am on the NEETprrp Login page
    When I enter my mobile number
    And I click the Send OTP buttion
    And I didnt enter any OTP
    And I click the verify OTP button
    Then Proper Error Validation message Please enter the OTP should be displayed

  Scenario: Login with valid mobile number and Expired OTP
    Given I am on the NEETprrp Login page
    When I enter a valid mobile number
    And I click the Send OTP buttion
    And I enter any expired OTP
    And I click the verify OTP button
    Then Proper Error Validation message for expired OTP should be displayed

  Scenario: Login without entering mobile number and valid OTP
    Given I am on the NEETprrp Login page
    When I didnt enter any mobile number
    And I click the Send OTP buttion
    And I enter a valid OTP
    And I click the verify OTP button
    Then Proper Error Validation message for expired OTP should be displayed