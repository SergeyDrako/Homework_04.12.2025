from playwright.sync_api import expect
import allure
import enum
import os
import re
import pytest
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
from utils_logger_test_QA_Practic.pages_base_page import BasePage

class PageInputs(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.url = "https://www.qa-practice.com/"
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_inputs = page.locator('a[href="/elements/input"]')
        self.choose_text_input = page.locator('a[href="/elements/input/simple"]')
        self.choose_email_field = page.locator('a[href="/elements/input/email"]')
        self.choose_password_field = page.locator('a[href="/elements/input/passwd"]')
        self.choose_text_string_box = page.locator('#id_text_string')
        self.choose_email_box = page.locator('#id_email')
        self.choose_password_box = page.locator('#id_password')
        self.choose_result = page.locator('#result')
        self.choose_error_text_string = page.locator('#error_1_id_text_string')
        self.choose_error_text_email = page.locator('#error_1_id_email')
        self.choose_error_text_password = page.locator('#error_1_id_password')


    @allure.step('Open the website')
    def open(self):
        super().open(self.url)

    @allure.step('click in the page Single UI elements')
    def click_single_ui_elements(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_singleUI}")
        self.choose_singleUI.click()

    @allure.step('click in the page Text Inputs')
    def click_inputs(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_inputs}")
        self.choose_inputs.click()

    @allure.step('click in the button in Text Inputs')
    def click_button_text_input(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_text_input}")
        self.choose_text_input.click()

    @allure.step('click in the button in Email field')
    def click_button_email_field(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_email_field}")
        self.choose_email_field.click()

    @allure.step('click in the button in Password field')
    def click_button_password_field(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_password_field}")
        self.choose_password_field.click()

    @allure.step('click in the window Text string')
    def click_window_text_string(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_text_string_box}")
        self.choose_text_string_box.click()

    @allure.step('click in the window Email string')
    def click_window_email(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_email_box}")
        self.choose_email_box.click()

    @allure.step('click in the window Password string')
    def click_window_password(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_password_box}")
        self.choose_password_box.click()

    @allure.step('presses enter on the keyboard into button Text input')
    def press_enter_box_text_string(self):
        self.logger.log_issue("INFO", f"Press button Enter on the keyboard")
        self.choose_text_string_box.press('Enter')

    @allure.step('presses enter on the keyboard into button Email field')
    def press_enter_box_email(self):
        self.logger.log_issue("INFO", f"Press button Enter on the keyboard")
        self.choose_email_box.press('Enter')

    @allure.step('presses enter on the keyboard into button Password field')
    def press_enter_box_password(self):
        self.logger.log_issue("INFO", f"Press button Enter on the keyboard")
        self.choose_password_box.press('Enter')

    @allure.step('check visible window Text string')
    def check_visible_text_string(self) -> None:
        self.logger.log_issue("INFO", "Checking the visibility window text string")
        expect(self.choose_text_string_box).to_be_visible()

    @allure.step('check visible window email field')
    def check_visible_window_email(self) -> None:
        self.logger.log_issue("INFO", "Checking the visibility window email field")
        expect(self.choose_email_box).to_be_visible()

    @allure.step('check visible window password field')
    def check_visible_password_field(self) -> None:
        self.logger.log_issue("INFO", "Checking the visibility window password field")
        expect(self.choose_password_box).to_be_visible()

    @allure.step('check field is required text Text string')
    def check_field_is_required_box_text_string(self)-> None:
        self.logger.log_issue("INFO", "Checking   the mandatory nature of filling Text string")
        expect( self.choose_text_string_box).to_have_attribute("required", "")

    @allure.step('check field is required text email field')
    def check_field_is_required_box_email(self)-> None:
        self.logger.log_issue("INFO", "Checking the mandatory nature of filling email field")
        expect(self.choose_email_box).to_have_attribute("required", "")

    @allure.step('check field is required text password field')
    def check_field_is_required_box_password(self)-> None:
        self.logger.log_issue("INFO", "Checking the mandatory nature of filling password field")
        expect(self.choose_password_box).to_have_attribute("required", "")

    @allure.step('Enter text into the window Submit me')
    def input_box_text_string(self, data) -> None:
        self.logger.log_issue("INFO", f"Enter text into the window Submit me: {data}")
        self.choose_text_string_box.fill(data)

    @allure.step('Enter text into the window email')
    def input_box_email(self, data) -> None:
        self.logger.log_issue("INFO", f"Enter text into the window email: {data}")
        self.choose_email_box.fill(data)

    @allure.step('Enter text into the window password')
    def input_box_password(self, data) -> None:
        self.logger.log_issue("INFO", f"Enter text into the window password: {data}")
        self.choose_password_box.fill(data)

    @allure.step('Positive test page. Check result after enter data')
    def check_result(self, expected: str) -> None:
        self.logger.log_issue("INFO", f"Check result after enter data: {expected}")
        expect(self.choose_result).to_contain_text(expected)

    @allure.step('Negative test page. Check result after enter invalid text: "{data}"')
    def check_result_error_text(self, data: str, expected: str) -> None:
        self.logger.log_issue("INFO", f"Check result after enter data. Expected on UI: '{expected}'")

        if any(char in data for char in ['.', '!', '?', ':', ';', '@']):
            reason = "Обнаружены запрещенные спецсимволы"
        elif len(data) < 2:
            reason = "Текст слишком короткий (< 2 символа)"
        elif not data.strip():
            reason = "Передана пустая строка или только пробелы"
        else:
            reason = f"Текст '{data}' не соответствует регулярному выражению валидации"

        self.logger.log_issue("INFO", f"Тест требований. Причина: {reason}. Ожидаем на UI: '{expected}'")
        expect(self.choose_error_text_string).to_be_visible(timeout=5000)
        expect(self.choose_error_text_string).to_contain_text(expected)

    @allure.step('Negative test page. Check result after enter Enter text Max: 25 characters into the window Submit me')
    def check_max_length_restriction_text_string(self, expected)-> None:
        self.logger.log_issue("INFO", f"Check result after enter data: {expected}")
        expect(self.choose_error_text_string).to_contain_text(expected)

    @allure.step("Negative test page. Check result after enter Enter text e-mail without domen (com) into the window Submit me")
    def check_text_error_input_is_not_valid_email(self, expected)-> None:
        self.logger.log_issue("INFO", f"Check result after enter data: {expected}")
        expect(self.choose_error_text_email).to_contain_text(expected)

    @allure.step('Negative password test. Check result after enter invalid password: "{data}"')
    def check_password_error_text(self, data: str, expected: str) -> None:
        self.logger.log_issue("INFO", f"Check password error after enter data. Expected on UI: '{expected}'")

        reasons = []

        if len(data) < 8:
            reasons.append("Длина < 8 символов")

        if re.search(r'[а-яА-ЯёЁ]', data):
            reasons.append("Обнаружена недопустимая кириллица")

        if not re.search(r'[A-Z]', data):
            reasons.append("Нет заглавной английской буквы")

        if not re.search(r'[a-z]', data):
            reasons.append("Нет строчной английской буквы")

        if not re.search(r'\d', data):
            reasons.append("Нет ни одной цифры")

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', data):
            reasons.append("Нет специальных символов")

        #Итоговая строка для логов:
        if reasons:
            final_reason = " | ".join(reasons)
        else:
            final_reason = "Пароль формально валиден, но отклонен системой"

        self.logger.log_issue("INFO",f"Тест требований пароля. Нарушения: [{final_reason}]. "
                                     f"Ожидаем на UI: '{expected}'")

        try:
            expect(self.choose_error_text_password).to_be_visible(timeout=5000)
            expect(self.choose_error_text_password).to_contain_text(expected)
            self.logger.log_issue("INFO", "Текст ожидаемых ошибок отображается корректно.")

        except AssertionError:
            # Если элемент вообще отсутствует в DOM, inner_text()
            # может выбросить ошибку, поэтому страхуемся через try/except
            try:
                actual_text = self.choose_error_text_password.inner_text()
            except Exception:
                actual_text = "Элемент ошибки не появился на экране (text: Low password complexity)"

            error_report = (
                f"\n[ОШИБКА СРАВНЕНИЯ ТЕКСТА ОШИБКИ]\n"
                f"ВВЕДЕННЫЙ ПАРОЛЬ: '{data}'\n"
                f"ВЫЯВЛЕННЫЕ НАРУШЕНИЯ: {final_reason}\n"
                f"ОЖИДАЛИ НА UI: '{expected}'\n"
                f"ПОЛУЧИЛИ НА UI: '{actual_text}'\n"
                f"ПРИЧИНА ПАДЕНИЯ: Сайт не отобразил ожидаемый текст ошибки для данного набора нарушений."
            )
            self.logger.log_issue("ERROR", error_report, page=self.page)
            pytest.fail(error_report)

    @allure.step('take screenshots full page Inputs')
    def take_screenshots_buttons(self, name: str,
                                 base_folder: str = r"E:\Study IT\Final_project_Test_QA_Practic\screenshots_all_page"):
        folder = Path(base_folder) / "screenshots_page_inputs"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")