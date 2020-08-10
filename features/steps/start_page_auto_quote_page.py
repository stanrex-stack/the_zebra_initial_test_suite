from behave import when
from time import sleep


@when('Answer {option} for active car insurance')
def select_if_have_insurance(context, option):
    context.app.car_quote_start_page.select_if_have_insurance(option)


@when('Select option {option} for owning a home')
def select_if_own_home(context, option):
    context.app.car_quote_start_page.select_if_own_home(option)


@when('Select option {option} for why shopping, continue')
def select_why_shopping(context, option):
    context.app.car_quote_start_page.select_why_shopping(option)
    context.app.car_quote_start_page.click_continue()


@when('Enter address: {address}')
def enter_address(context, address):
    context.app.car_quote_start_page.enter_address(address)


@when('Enter name {first} {last}, dob {mm}/{dd}/{yyyy}, continue')
def enter_applicant(context, first, last, mm, dd, yyyy):
    context.app.car_quote_start_page.enter_first_name(first)
    context.app.car_quote_start_page.enter_last_name(last)
    context.app.car_quote_start_page.enter_dob(f'{mm}{dd}{yyyy}')
    context.app.car_quote_start_page.click_continue()


@when('Enter {year}, {car}, {model}, {trim}, continue')
def enter_vehicle(context, year, car, model, trim):
    context.app.car_quote_vehicles_page.enter_car_year(year)
    context.app.car_quote_vehicles_page.enter_car_make(car)
    context.app.car_quote_vehicles_page.enter_car_model(model)
    context.app.car_quote_vehicles_page.enter_car_trim(trim)
    context.app.car_quote_vehicles_page.click_continue()


@when('Enter email {email}')
def enter_email(context, email):
    context.app.car_quote_driver_page.enter_email(email)


@when('Click to get quotes')
def click_show_quotes(context):
    context.app.car_quote_driver_page.click_show_quotes()


@when('Select {result} result for current provider')
def select_provider_dropdown(context, result):
    context.app.car_quote_driver_page.enter_provider(result)


@when('Select option {option} for owning a car')
def select_if_own_car(context, option):
    context.app.car_quote_vehicles_page.select_if_own_car(option)


@when('Select option {option} for car usage')
def select_if_own_car(context, option):
    context.app.car_quote_vehicles_page.select_car_usage(option)


@when('Enter mileage {mileage}, continue')
def enter_mileage(context, mileage):
    context.app.car_quote_vehicles_page.enter_car_mileage(mileage)
    context.app.car_quote_vehicles_page.click_continue()


@when('Select option {option} for gender')
def select_driver_gender(context, option):
    context.app.car_quote_driver_page.select_gender(option)


@when('Select option {option} for marital status')
def select_driver_marital_status(context, option):
    context.app.car_quote_driver_page.select_marital_status(option)


@when('Select option {option} for credit score')
def select_credit_score(context, option):
    context.app.car_quote_driver_page.select_credit(option)


@when('Select option {option} for education')
def select_education(context, option):
    context.app.car_quote_driver_page.select_education(option)


@when('Select option {option} for current insurance duration')
def select_insurance_duration(context, option):
    context.app.car_quote_driver_page.select_duration(option)


@when('Select option {option} for current accidents')
def select_accidents(context, option):
    context.app.car_quote_driver_page.select_accidents(option)


@when('Select option {option} for discounts')
def select_discount(context, option):
    context.app.car_quote_driver_page.select_discounts(option)

