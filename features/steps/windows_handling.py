from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Close {element_choice} Window')
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

