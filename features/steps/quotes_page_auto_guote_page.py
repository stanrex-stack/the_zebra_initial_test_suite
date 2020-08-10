from behave import then


@then('Verify Quotes are shown')
def verify_quotes_shown(context):
    context.app.car_quote_quote_page.verify_quotes_shown()
