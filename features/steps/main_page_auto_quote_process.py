from behave import given, when, then


@given('Open Main Page')
def open_main_page(context):
    context.app.main_page.main_open()


@when('Select Car Insurance')
def select_car_insurance(context):
    context.app.main_page.click_car_insurance()


@when('Input zip {zip}, start')
def select_car_insurance(context, zip):
    context.app.main_page.input_zip(zip)
    context.app.main_page.click_start()


@then('Verify Zip Error shown')
def verify_zip_error_present(context):
    context.app.main_page.verify_zip_error_present()


@then('Verify Zip Error text is {text}')
def verify_zip_error_text(context, text):
    context.app.main_page.verify_zip_error_text(text)


@when('Click On Instagram')
def click_instagram_link(context):
    context.app.main_page.click_instagram_link()
