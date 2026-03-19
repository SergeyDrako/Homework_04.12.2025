from playwright.sync_api import Page, expect
import os
from datetime import datetime
from pathlib import Path
from Page_Tests.utils_logger import log_test_issue

URL = "https://www.qa-practice.com/"

class PageTextArea(Page):
    def __init__(self, page):
        self.page = page
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

    def open(self):
        self.page.goto(URL)

    def click_single_ui_elements(self) -> None:
        self.choose_singleUI.click()

    def click_text_area(self) -> None:
        self.choose_text_area.click()

    def click_button_textarea(self) -> None:
        self.choose_button_textarea .click()

    def click_button_multiple_textareas(self) -> None:
        self.choose_button_multiple_textareas.click()

    def click_window_text_area_box_text(self) -> None:
        self.choose_window_text_area_box_text.click()

    def click_window_box_text_multiple_textareas_first_chapter(self) -> None:
        self.choose_window_multiple_textareas_first_chapter.click()

    def click_window_box_text_multiple_textareas_second_chapter(self) -> None:
        self.choose_window_multiple_textareas_second_chapter.click()

    def click_window_box_text_multiple_textareas_third_chapter(self) -> None:
        self.choose_window_multiple_textareas_third_chapter.click()

    def check_visible_text_area_box_text(self)-> None:
        expect(self.choose_window_text_area_box_text).to_be_visible()

    def check_visible_multiple_textareas_first_chapter(self)-> None:
        expect(self.choose_window_multiple_textareas_first_chapter).to_be_visible()

    def check_visible_multiple_textareas_second_chapter(self)-> None:
        expect(self.choose_window_multiple_textareas_second_chapter).to_be_visible()

    def check_visible_multiple_textareas_third_chapter(self)-> None:
        expect(self.choose_window_multiple_textareas_third_chapter).to_be_visible()

    def check_field_is_required_text_area_box_text(self)-> None:
        expect(self.choose_window_text_area_box_text).to_have_attribute("required", "")

    def check_field_is_required_multiple_textareas_first_chapter_box_text(self)-> None:
        expect(self.choose_window_multiple_textareas_first_chapter).to_have_attribute("required", "")

    def input_box_text_area_box_text(self, data) -> None:
        self.choose_window_text_area_box_text.fill(data)

    def input_box_multiple_textareas_first_chapter_box_text(self, data) -> None:
        self.choose_window_multiple_textareas_first_chapter.fill(data)

    def input_box_multiple_textareas_second_chapter_box_text(self, data) -> None:
        self.choose_window_multiple_textareas_second_chapter.fill(data)

    def input_box_multiple_textareas_third_chapter_box_text(self, data) -> None:
         self.choose_window_multiple_textareas_third_chapter.fill(data)

    def submit(self) -> None:
        self.choose_submit.click()

    def check_result(self, expected)-> None:
        expect(self.result_choose).to_have_text(expected)

    def check_result_multiple_textareas(self, expected: str) -> None:
        try:
            expect(self.result_choose).to_have_text(expected, timeout=5000)
            print("Проверка текста пройдена успешно.")

        except AssertionError:
            actual_text = self.result_choose.inner_text()
            log_test_issue(
                level="ERROR",
                message=f"Текст в поле #result-text не соответствует ожидаемому.\n ОЖИДАЛИ: '{expected}' \n ПОЛУЧИЛИ: '{actual_text}'",
                page=self.page
            )

    def take_screenshots_text_area(self, name: str,
                                   base_folder:str = r"E:\Study IT\Final project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) / "screenshots_text_area"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")