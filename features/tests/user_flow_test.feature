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

#
#
#    When VEHICLE Click On First Question Paid
#    When VEHICLE Click On Second Question Farm
#    When VEHICLE Send Milage 12000
#    When VEHICLE Click On Save And Continue
#
#    When DRIVER Click On Driver Male
#    When DRIVER Click On Marital Married
#    When DRIVER Click On Credit Excellent (720+)
#    When DRIVER Click On Education No diploma
#    When DRIVER Click On Insured Less than 6 months
#    When DRIVER Click On Current Provider Input
#    When DRIVER Click On Current Provider First Selection
#    When DRIVER Click On Violations No
#
##    When DRIVER For email type in testexample@gmail.com
#    When DRIVER Email Send testexample@gmail.com
#
#    When DRIVER Click On Discount Active military or veteran
#    When DRIVER Click On Referral Input
#    When DRIVER Click On Referral First Selection
#
#    When DRIVER Spouse First Name Send Wekeah
#    When DRIVER Spouse Last Name Send Penateka
#    When DRIVER Spouse Birthdate Send 11211993
#    When DRIVER Click On Spouse Female
#    When DRIVER Click On Add Driver No
#    When DRIVER Click On Show My Quotes
#    When QUOTES Wait for a 35 seconds
#    Then QUOTES Gather All The Quotes