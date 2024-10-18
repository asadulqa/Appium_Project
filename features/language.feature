# Created by Asadul at 10/4/2024
Feature: User change the language

  Scenario: User change the Language
    Given User Open app
    Then User click on the Workspace
    And User click on the setting button
    And User click on the Language button
    Then User select the Language
    Then User click_back_button
    And User verify the language changed successfully
