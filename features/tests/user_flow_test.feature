# Created by zelec at 8/6/2020
Feature: Tests for UI

  Scenario: User Flow: user can get a quote
    Given Open Main Page
    When Select Car Insurance
    And Input zip 78735, start
    And Answer Yes for active car insurance
    And Select option 1 for owning a home
    And Select option 1 for why shopping, continue
    And Enter address: 1845 Comanche Creek Drive
    And Enter name Quanah Parker, dob 03/25/1983, continue
    And Enter 2020, Ford, Mustang, Shelby, continue
    #TODO THE MUSTANG, SHELBY STEPS ARE FALLING
    And Select option 2 for owning a car
    And Select option 4 for car usage
    And Enter milage 12000, continue
    And Select option 1 for gender
    And Select option 2 for marital status
    And Select option 1 for credit score
    And Select option 5 for education
    And Select option 4 for current insurance duration
    And Select 1 result for current provider
    And Select option 2 for current accidents
    And Enter email testexample@gmail.com
    And Select option 2 for discounts
    And Select option 4 for discounts
    And Select option 1 for reference
    And Enter spouse Wekeah, Penateka, dob 11/21/1993
    And Select option 2 for spouse gender
    And Select option 2 for additional driver, continue
    When QUOTES Wait for a 35 seconds
    Then QUOTES Gather All The Quotes
