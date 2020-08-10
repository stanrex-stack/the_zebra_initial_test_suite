from behave import then

from selenium.webdriver.support import expected_conditions as EC


@then('Close {element_choice} window')
def windows_handeling(context, element_choice):
    if element_choice == "Newly Opened":
        window_index = 1
    elif element_choice == "Old":
        window_index = 0
    else:
        raise Exception("No such field name found")
    context.driver.wait.until(EC.number_of_windows_to_be(2))
    new_window = context.driver.window_handles[window_index]
    context.driver.switch_to_window(new_window)
    context.driver.close()
