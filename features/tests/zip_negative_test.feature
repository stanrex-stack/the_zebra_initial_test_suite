# Created by stanrex at 8/8/2020
Feature: Main Page Hero Alerts Verification

  @negative
  Scenario: Error message shown upon entering invalid zip
    Given Open Main Page
    When Input zip 111, start
    Then Verify Zip Error shown
    And Verify Zip Error text is  This ZIP code is invalid.
