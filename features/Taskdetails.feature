# Created by Asadul at 10/4/2024
Feature: User verify Board Section


  Scenario: User delete the project details
    Given User open the home page
    Then User click on the Board section
    Then User click on the Pen icon
    And User Delete the project details
    Then User click on the yes delete button
    And User verify the project details delete successful

    