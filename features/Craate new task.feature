# Created by Asadul at 10/4/2024
Feature: User Create New Tasks

  Scenario: User Create Repeating task
    Given Open the app
    And User click on the "+" icon
    Then User click on the create repeating task
    And User enter the task title
    And  User enter the descriptions
    Then User click on the Select project
    And user enter the project name and save
    And User click on the Set priority button
    Then User click on the Urgent
    Then User click on the Add reminder button
    And User select the scheduled
    And User click on the Checklist button
    Then User click on the Add item button
    And User enter the checklist item name and back button
    Then User click on the export button
    And User verify the Repeating task on the dashboard




  Scenario: User create Note
    Given Open the app
    And User click on the "+" icon
    Then User click on the create Note
    Then User enter the Note title
    Then User enter the descriptions
    Then User click on the Select project
    And user enter the project name and save
    And User click on the Set priority button
    Then User click on the Urgent
    Then User click on the Add reminder button
    And User select the scheduled
    And User click on the Checklist button
    Then User click on the Add item button
    And User enter the checklist item name and back button
    Then User click on the export button
    And User verify the Note task on the dashboard


  Scenario: User Create task
    Given Open the app
    Then User click on the "+" icon
    And user click on the Note button
    And User enter the task title
    And  User enter the descriptions
    Then User click on the Select project
    And user enter the project name and save
    And User click on the Set priority button
    Then User click on the Urgent
    And User click on the Checklist button
    Then User click on the Add item button
    And User enter the checklist item name and back button
    Then User click on the export button
    And User verify the task on the dashboard



