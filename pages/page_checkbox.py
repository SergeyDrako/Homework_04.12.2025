from playwright.sync_api import Page, expect
import enum
import os
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright

URL = "https://www.qa-practice.com/"

class ClickCheckbox(Page):
    def __init__(self, page):
        self.page = page
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_submit = page.locator('#submit-id-submit')
        self.result_choose = page.locator('#result-text')
        self.choose_checkbox = page.locator('a[href="/elements/checkbox"]')
        self.choose_checkboxes = page.locator('a[href="/elements/checkbox/mult_checkbox"]')
        self.choose_select_me_or_not = page.locator('#id_checkbox_0')
        self.choose_one = page.locator('#id_checkboxes_0')
        self.choose_two = page.locator('#id_checkboxes_1')
        self.choose_three = page.locator('#id_checkboxes_2')

    def open(self):
        self.page.goto(URL)

    def click_single_ui_elements(self) -> None:
        self.choose_singleUI.click()

    def click_single_checkbox(self) -> None:
        self.choose_singleUI.click()

    def click_checkbox(self) -> None:
        self.choose_checkbox.click()

    def click_select_me_or_not(self) -> None:
        self.choose_select_me_or_not.click()

    def click_checkboxes(self) -> None:
        self.choose_checkboxes.click()

    def click_choise_one(self) -> None:
        self.choose_one.click()

    def click_choise_two(self) -> None:
        self.choose_two.click()

    def click_choise_three(self) -> None:
        self.choose_three.click()

    def click_submit(self) -> None:
        self.choose_submit.click()

    def check_status_submit_enabled(self) -> None:
        expect(self.choose_submit).to_be_enabled()

    def check_result(self, expected)-> None:
        expect(self.result_choose).to_have_text(expected)

    def check_checkboxs_result_is_empty(self) -> None:
        expect(self.result_choose).to_be_hidden(timeout=5*1000)

    def take_screenshots_checkbox(self, name: str,
                                  base_folder:str = r"E:\Study IT\Final project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) / "screenshots_page_checkbox"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")