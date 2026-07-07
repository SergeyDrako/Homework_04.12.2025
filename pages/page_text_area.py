import os
import allure
from playwright.sync_api import expect
from datetime import datetime
from pathlib import Path
from utils_logger_test_QA_Practic.pages_base_page import BasePage


class PageTextArea(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.url = "https://www.qa-practice.com/"
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_text_area = page.locator('a[href="/elements/textarea"]')
        self.choose_button_textarea = page.locator('a[href="/elements/textarea/single"]')
        self.choose_button_multiple_textareas = page.locator('a[href="/elements/textarea/textareas"]')
        self.choose_window_text_area_box_text = page.locator('#id_text_area')
        self.choose_window_multiple_textareas_first_chapter = page.locator('#id_first_chapter')
        self.choose_window_multiple_textareas_second_chapter = page.locator('#id_second_chapter')
        self.choose_window_multiple_textareas_third_chapter = page.locator('#id_third_chapter')
        self.choose_submit = page.locator('#submit-id-submit')
        self.result_choose = page.locator('#result-text')

    @allure.step('Open the website')
    def open(self)-> None:
        super().open(self.url)

    @allure.step('click in the page Single UI elements')
    def click_single_ui_elements(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_singleUI}")
        self.choose_singleUI.click()

    @allure.step('click in the page text area')
    def click_text_area(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_text_area}")
        self.choose_text_area.click()

    @allure.step('click in the button textarea')
    def click_button_textarea(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_button_textarea}")
        self.choose_button_textarea.click()

    @allure.step('click in the button multiple textareas')
    def click_button_multiple_textareas(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_button_multiple_textareas}")
        self.choose_button_multiple_textareas.click()

    @allure.step('click in the window textarea box text')
    def click_window_text_area_box_text(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_window_text_area_box_text}")
        self.choose_window_text_area_box_text.click()

    @allure.step('click in the window box text multiple text areas first chapter')
    def click_window_box_text_multiple_textareas_first_chapter(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_window_multiple_textareas_first_chapter}")
        self.choose_window_multiple_textareas_first_chapter.click()

    @allure.step('click in the window box text multiple text areas second chapter')
    def click_window_box_text_multiple_textareas_second_chapter(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_window_multiple_textareas_second_chapter}")
        self.choose_window_multiple_textareas_second_chapter.click()

    @allure.step('click in the window box text multiple text areas third  chapter')
    def click_window_box_text_multiple_textareas_third_chapter(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_window_multiple_textareas_third_chapter}")
        self.choose_window_multiple_textareas_third_chapter.click()

    @allure.step('check visible window text area box text')
    def check_visible_text_area_box_text(self)-> None:
        self.logger.log_issue("INFO", "Checking the visibility of a text field TextArea")
        expect(self.choose_window_text_area_box_text).to_be_visible()

    @allure.step('check visible window multiple textareas first chapter')
    def check_visible_multiple_textareas_first_chapter(self)-> None:
        self.logger.log_issue("INFO", "Checking the visibility of a text field first box for read text area")
        expect(self.choose_window_multiple_textareas_first_chapter).to_be_visible()

    @allure.step('check visible window multiple textareas second chapter')
    def check_visible_multiple_textareas_second_chapter(self)-> None:
        self.logger.log_issue("INFO", "Checking the visibility of a text field second box for read text area")
        expect(self.choose_window_multiple_textareas_second_chapter).to_be_visible()

    @allure.step('check visible window multiple textareas third chapter')
    def check_visible_multiple_textareas_third_chapter(self)-> None:
        self.logger.log_issue("INFO", "Checking the mandatory nature of filling third box for read text area")
        expect(self.choose_window_multiple_textareas_third_chapter).to_be_visible()

    @allure.step('check field is required text area box text')
    def check_field_is_required_text_area_box_text(self)-> None:
        self.logger.log_issue("INFO", "Checking the mandatory nature of filling text_area_box_text")
        expect(self.choose_window_text_area_box_text).to_have_attribute("required", "")

    @allure.step('check field is required multiple textareas first chapter box text')
    def check_field_is_required_multiple_textareas_first_chapter_box_text(self)-> None:
        self.logger.log_issue("INFO", "Checking the mandatory nature of filling first chapter box for read text area")
        expect(self.choose_window_multiple_textareas_first_chapter).to_have_attribute("required", "")

    @allure.step('input box text area box text')
    def input_box_text_area_box_text(self, data) -> None:
        self.logger.log_issue("INFO", f"input text in box text: {data}")
        self.choose_window_text_area_box_text.fill(data)

    @allure.step('input box multiple text areas first chapter box text')
    def input_box_multiple_text_areas_first_chapter_box_text(self, data) -> None:
        self.logger.log_issue("INFO", f"input text in first chapter box text: {data}")
        self.choose_window_multiple_textareas_first_chapter.fill(data)

    @allure.step('input box multiple text areas second chapter box text')
    def input_box_multiple_text_areas_second_chapter_box_text(self, data) -> None:
        self.logger.log_issue("INFO", f"input text in second chapter box text: {data}")
        self.choose_window_multiple_textareas_second_chapter.fill(data)

    @allure.step('input box multiple text areas third chapter box text')
    def input_box_multiple_text_areas_third_chapter_box_text(self, data) -> None:
        self.logger.log_issue("INFO", f"input text in third chapter box text: {data}")
        self.choose_window_multiple_textareas_third_chapter.fill(data)

    @allure.step('Click on the submit button')
    def submit(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_submit}")
        self.choose_submit.click()

    @allure.step('Check the result of the submit button')
    def check_result(self, expected:str)-> None:
        self.logger.log_issue("INFO", f"Checking whether the entered text matches the actual result: {expected}")
        expect(self.result_choose).to_have_text(expected)

    @allure.step('Check the result of the submit button {expected} and catching expected errors')
    def check_result_multiple_text_areas(self, expected) -> None:
        self.logger.log_issue("INFO", f"Проверка текста: {expected}")
        expect(self.result_choose).to_contain_text(expected, timeout=5000)
        self.logger.log_issue("INFO", f"Начинаем проверку текста. Ожидаем: {expected}")

        try:
            expect(self.result_choose).to_have_text(expected, timeout=5000)
            self.logger.log_issue("INFO", "Текст совпал успешно.")

        except AssertionError as e:
            actual_text = self.result_choose.inner_text()
            error_report = (
                f"\n[ОШИБКА СРАВНЕНИЯ ТЕКСТА]\n"
                f"ОЖИДАЛИ: {expected}\n"
                f"ПОЛУЧИЛИ: {actual_text}"
            )
            self.logger.log_issue("ERROR", error_report)

            # # Прикрепляем отчет об ошибке в Allure вручную
            # allure.attach(error_report, name="Comparison Error Details", attachment_type=allure.attachment_type.TEXT)


    @allure.step('take screenshots pages text area')
    def take_screenshots_text_area(self, name: str,
                                   base_folder:str = r"E:\Study IT\Final_project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) / "screenshots_text_area"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")