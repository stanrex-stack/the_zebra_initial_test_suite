from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('QUOTES Wait for a {time_var} seconds')
def waiting_function(context, time_var):
    sleep(int(time_var))


@then('QUOTES Gather All The Quotes')
def gather_all_quotes(context):
    context.app.car_quote_quote_page.gather_all_quotes()
