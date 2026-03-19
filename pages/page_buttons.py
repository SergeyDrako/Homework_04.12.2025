from playwright.sync_api import Page, expect
import enum
import os
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://www.qa-practice.com/"

class SelectState(enum.Enum):
    DISABLED = 'Disabled'
    ENABLED = 'Enabled'

class PageButtons(Page):
    def __init__(self, page):
        self.page = page
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_buttons = page.locator('a[href="/elements/button"]')
        self.choose_simple_button = page.locator('a[href="/elements/button/simple"]')
        self.choose_looks_like_button = page.locator("text = Looks like a button")
        self.choose_disabled =page.locator('a[href="/elements/button/disabled"]')
        self.choose_drop_select_state = page.locator("#id_select_state")
        self.choose_click_simple_button = page.locator('#submit-id-submit')
        self.choose_click_lookslike_button = page.locator('//a[@onclick="document.getElementById(\'button-form\').submit();"]')
        self.choose_submit = page.locator('#submit-id-submit')
        self.result_choose = page.locator('#result-text')

    def open(self):
        self.page.goto(URL)

    def click_single_ui_elements(self) -> None:
        self.choose_singleUI.click()

    def click_buttons(self) -> None:
        self.choose_buttons.click()

    def click_simple_button(self) -> None:
        self.choose_simple_button.click()

    def push_button_click_simple_button(self)-> None:
        self.choose_click_simple_button.click()

    def click_looks_like_button(self)-> None:
        self.choose_looks_like_button.click()

    def click_disabled (self)-> None:
        self.choose_disabled.click()

    def push_button_click_lookslike_button(self)-> None:
        self.choose_looks_like_button.wait_for(state="visible", timeout=5*1000)
        self.choose_click_lookslike_button.evaluate("el => el.click()")
        # self.page.evaluate("document.querySelector('a.a-button').click()")
        self.page.wait_for_load_state("networkidle")

    def drop_select_state(self,choise:str) -> None:
        self.choose_drop_select_state.select_option(choise)

    def submit(self) -> None:
        self.choose_submit.click()

    def check_status_submit_enabled(self) -> None:
        expect(self.choose_submit).to_be_enabled()

    def check_status_submit_disabled(self)-> None:
        expect(self.choose_submit).to_be_disabled()

    def check_result(self, expected)-> None:
        expect(self.result_choose).to_have_text(expected)

    def take_screenshots_buttons(self, name: str,
                                 base_folder: str = r"E:\Study IT\Final project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) /"screenshots_page_buttons"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")