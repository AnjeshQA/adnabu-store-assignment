Feature: Adnabu Store Cart Management

  Scenario: After Login user Search a product & Successfully adding a product to the cart
    Given User successfully logged in to the Adnabu store
    And I am on the store homepage
    When I search for the configured product
    And I add the product to my cart
    Then I should see the product in the checkout summary