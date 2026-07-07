from playwright.sync_api import expect
import allure
import pytest
import enum
from pages.page_inputs import PageInputs
import time

@allure.title("Positive test page Inputs. Enter text valid: 25 characters into the window Submit me")
def test_positive_page_inputs_max_25_characters(page, page_inputs)->None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_text_input()
    page_inputs.click_window_text_string()
    page_inputs.check_visible_text_string()
    page_inputs.check_field_is_required_box_text_string()
    page_inputs.input_box_text_string("Python_DrakoSerge-2101990")
    page_inputs.press_enter_box_text_string()
    page_inputs.check_result("Python_DrakoSerge-2101990")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_Positive_inputs_valid_2_characters')

@allure.title("Positive test page Inputs. Enter text valid: 2 characters into the window Submit me")
def test_positive_page_inputs_min_2_characters(page, page_inputs)->None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_text_input()
    page_inputs.click_window_text_string()
    page_inputs.check_visible_text_string()
    page_inputs.check_field_is_required_box_text_string()
    page_inputs.input_box_text_string("S1")
    page_inputs.press_enter_box_text_string()
    page_inputs.check_result("S1")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_Positive_inputs_valid_2_characters')

@allure.title("Negative test page Inputs. Enter text anymore: 25 characters into the window Submit me")
def test_negative_page_inputs_max_25_characters(page, page_inputs)->None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_text_input()
    page_inputs.click_window_text_string()
    page_inputs.input_box_text_string("gkngldfnglkfdmgjodemg22333")
    page_inputs.press_enter_box_text_string()
    page_inputs.check_max_length_restriction_text_string("Please enter no more than 25 characters")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_Negative_inputs_anymore_25_characters')

@allure.title("Negative test page Inputs. Enter text min: 2 characters into the window Submit me")
def test_negative_page_inputs_min_2_characters(page, page_inputs)->None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_text_input()
    page_inputs.click_window_text_string()
    page_inputs.input_box_text_string("B")
    page_inputs.press_enter_box_text_string()
    page_inputs.check_result_error_text('B', "Please enter 2 or more characters")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_Negative_inputs_min_2_characters')


@allure.title("Negative test page Inputs. Enter symbols: '.', '!', '?', ':', ';','@'  characters "
              "into the window Submit me")
def test_negative_page_inputs_symbols(page, page_inputs)->None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_text_input()
    page_inputs.click_window_text_string()
    page_inputs.input_box_text_string("Drako@1990!")
    page_inputs.press_enter_box_text_string()
    page_inputs.check_result_error_text('Drako@1990!',
                                        "Enter a valid string consisting of letters, "
                                        "numbers, underscores or hyphens")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_Negative_inputs_symbols')

@allure.title("Positive test button Email_field. Enter text e-mail: "
                  "text with @,number, ! into the window Submit me")
def test_positive_button_email_field_input_box(page, page_inputs) -> None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_email_field()
    page_inputs.click_window_email()
    page_inputs.check_visible_window_email()
    page_inputs.check_field_is_required_box_email()
    page_inputs.input_box_email("DRAKOSERGE1990!@GMAIL.COM")
    page_inputs.press_enter_box_email()
    page_inputs.check_result("DRAKOSERGE1990!@GMAIL.COM")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_Positive_inputs_email_field')

@allure.title("Negative test button Email_field. Enter text e-mail: "
                  "text is not  domena 'com' into the window Submit me")
def test_negative_button_email_field_input_box_is_not_valid_email(page, page_inputs) -> None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_email_field()
    page_inputs.click_window_email()
    page_inputs.check_visible_window_email()
    page_inputs.check_field_is_required_box_email()
    page_inputs.input_box_email("DRAKOSERGE1990@GMAIL.")
    page_inputs.press_enter_box_email()
    page_inputs.check_text_error_input_is_not_valid_email('Enter a valid email address.')
    page_inputs.take_screenshots_buttons('screenshots_looks_like_Negative_inputs is_not_valid_email')

@allure.title("Positive test button Password field. "
              "Enter valid text password: Has minimum 8 characters in length"
              "At least one uppercase English letter"
              "At least one lowercase English letter"
              "At least one digit"
              "At least one special character into the window Submit me")
def test_positive_button_password_field_input_box(page, page_inputs) -> None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_password_field()
    page_inputs.click_window_password()
    page_inputs.check_visible_password_field()
    page_inputs.check_field_is_required_box_password()
    page_inputs.input_box_password("Petrov@1234!")
    page_inputs.press_enter_box_password()
    page_inputs.check_result("Petrov@1234!")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_Positive_inputs_password_field')

@allure.title("Negative test button Password field. "
              "Enter valid text password: Has minimum < 8 characters in length")
def test_negative_button_password_field_input_box_password_is_not_minimum_8_characters_in_length(page, page_inputs) -> None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_password_field()
    page_inputs.click_window_password()
    page_inputs.check_visible_password_field()
    page_inputs.check_field_is_required_box_password()
    page_inputs.input_box_password("Petro1!")
    page_inputs.press_enter_box_password()
    page_inputs.check_password_error_text('Petro1!', "Low password complexity")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_has_minimum_less_8_characters_in_length')


@allure.title("Negative test button Password field. "
              "There is not password at least one uppercase English letter")
def test_negative_button_password_field_input_box_password_is_not_least_one_uppercase_english_letter(page, page_inputs) -> None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_password_field()
    page_inputs.click_window_password()
    page_inputs.check_visible_password_field()
    page_inputs.check_field_is_required_box_password()
    page_inputs.input_box_password("petrov1234!")
    page_inputs.press_enter_box_password()
    page_inputs.check_password_error_text('petrov1234!', "Low password complexity")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_is_not_least_one_uppercase_English_letter')

@allure.title("Negative test button Password field. "
              "There is not password at least one lowercase English letter")
def test_negative_button_password_field_input_box_password_is_not_least_one_lowercase_english_letter(page, page_inputs) -> None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_password_field()
    page_inputs.click_window_password()
    page_inputs.check_visible_password_field()
    page_inputs.check_field_is_required_box_password()
    page_inputs.input_box_password("PETROV1234!")
    page_inputs.press_enter_box_password()
    page_inputs.check_password_error_text('PETROV1234', "Low password complexity")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_is_not_least_one_lowercase_english_letter')

@allure.title("Negative test button Password field. There is not password at least one digit")
def test_negative_button_password_field_input_box_password_is_not_one_digit(page, page_inputs) -> None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_password_field()
    page_inputs.click_window_password()
    page_inputs.check_visible_password_field()
    page_inputs.check_field_is_required_box_password()
    page_inputs.input_box_password("Petrov@Ivan!")
    page_inputs.press_enter_box_password()
    page_inputs.check_password_error_text('Petrov@Ivan!', "Low password complexity")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_is_not_password_at_least_one_digit')

@allure.title("Negative test button Password field. "
              "There are password at least one cyrillic character into the window Submit me")
def test_negative_button_password_field_input_box_password_have_one_cyrillic_character(page, page_inputs) -> None:
    page_inputs.open()
    page_inputs.click_single_ui_elements()
    page_inputs.click_inputs()
    page_inputs.click_button_password_field()
    page_inputs.click_window_password()
    page_inputs.check_visible_password_field()
    page_inputs.check_field_is_required_box_password()
    page_inputs.input_box_password("ПетрSee@20700!")
    page_inputs.press_enter_box_password()
    page_inputs.check_password_error_text('ПетрSee@20700!', "Low password complexity")
    page_inputs.take_screenshots_buttons('screenshots_looks_like_least_one_cyrillic_character')