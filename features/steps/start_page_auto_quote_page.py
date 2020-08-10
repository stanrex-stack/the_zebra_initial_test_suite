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
def enter_address(context, first, last, mm, dd, yyyy):
    context.app.car_quote_start_page.enter_first_name(first)
    context.app.car_quote_start_page.enter_last_name(last)
    context.app.car_quote_start_page.enter_dob(f'{mm}{dd}{yyyy}')
    context.app.car_quote_start_page.click_continue()
    sleep(5)
@when('Enter {year}, {car}, {model}, {trim}, continue')
def enter_vehicle(context, year, car, model, trim):
    context.app.car_quote_vehicles_page.enter_car_year(year)
    context.app.car_quote_vehicles_page.enter_car_make(car)
    context.app.car_quote_vehicles_page.enter_car_model(model)
    context.app.car_quote_vehicles_page.enter_car_trim(trim)
    context.app.car_quote_vehicles_page.click_continue()

@when('Select option {option} for owning a car')
def select_if_own_car(context, option):
    context.app.car_quote_vehicles_page.select_if_own_car(option)

@when('Select option {option} for car usage')
def select_if_own_car(context, option):
    context.app.car_quote_vehicles_page.select_car_usage(option)

@when('Enter milage {milage}, continue')
def enter_milage(context, milage):
    context.app.car_quote_vehicles_page.enter_car_milage(milage)
    context.app.car_quote_vehicles_page.click_continue()
    sleep(5)