Feature: Full test for User Flow

  Scenario: User Flow: user can get a quote
    Given Open Main Page
    When Select Car Insurance
    And Input zip 78735, start
    And Answer Yes for active car insurance
    And Select option 1 for owning a home
    And Select option 1 for why shopping, continue
    And Enter address: 1845 Comanche Creek Drive
    And Enter name Quanah Parker, dob 03/25/1983, continue
    And Enter 2020, Ford, Mustang, Shelby GT500, continue
    And Select option paid in full for owning a car
    And Select option business/rideshare for car usage
    And Enter mileage 12000, continue
    And Select option male for gender
    And Select option single for marital status
    And Select option good for credit score
    And Select option doctoral for education
    And Select option 1 for current insurance duration
    And Select AARP result for current provider
    And Select option no for current accidents
    And Enter email testexample@gmail.com
    And Click to get quotes
    Then Verify Quotes are shown
