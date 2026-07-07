from playwright.sync_api import expect
import allure
import enum
import os
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
from utils_logger_test_QA_Practic.pages_base_page import BasePage

class SelectState(enum.Enum):
    DISABLED = 'Disabled'
    ENABLED = 'Enabled'

class PageButtons(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.url = "https://www.qa-practice.com/"
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

    @allure.step('Open the website')
    def open(self):
        super().open(self.url)

    @allure.step('Click in the page Single UI elements')
    def click_single_ui_elements(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_singleUI}")
        self.choose_singleUI.click()

    @allure.step('Click in the page Buttons')
    def click_buttons(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_buttons}")
        self.choose_buttons.click()

    @allure.step('Click in the simple_button')
    def click_simple_button(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_simple_button}")
        self.choose_simple_button.click()

    @allure.step('Click in the push button click simple button')
    def push_button_click_simple_button(self)-> None:
        self.logger.log_issue("INFO", f"Push on: {self.choose_simple_button}")
        self.choose_click_simple_button.click()

    @allure.step('Click in the looks like button')
    def click_looks_like_button(self)-> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_looks_like_button}")
        self.choose_looks_like_button.click()

    @allure.step('Click in the click Submit disabled')
    def click_disabled (self)-> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_disabled}")
        self.choose_disabled.click()

    @allure.step('Click in push button click looks like button')
    def push_button_click_lookslike_button(self)-> None:
        self.choose_looks_like_button.wait_for(state="visible", timeout=5*1000)
        self.logger.log_issue("INFO", f"Push on: {self.choose_looks_like_button}")
        self.choose_click_lookslike_button.evaluate("el => el.click()")
        # self.page.evaluate("document.querySelector('a.a-button').click()")
        self.page.wait_for_load_state("networkidle")

    @allure.step('Dropping select_state disabled or enabled')
    def drop_select_state(self,choise:str) -> None:
        self.logger.log_issue("INFO", f"Dropping select_state: {choise}")
        self.choose_drop_select_state.select_option(choise)

    @allure.step('Click in the submit button')
    def submit(self) -> None:
        self.logger.log_issue("INFO", f"Submit: {self.choose_submit}")
        self.choose_submit.click()

    @allure.step('check status submit enabled')
    def check_status_submit_enabled(self) -> None:
        self.logger.log_issue("INFO", f"Check_status_submit_enabled")
        expect(self.choose_submit).to_be_enabled()

    @allure.step('check status submit disabled')
    def check_status_submit_disabled(self)-> None:
        self.logger.log_issue("INFO", f"Check_status_submit_disabled")
        expect(self.choose_submit).to_be_disabled()

    @allure.step('check result')
    def check_result(self, expected)-> None:
        self.logger.log_issue("INFO", f"Check_result: {expected}")
        expect(self.result_choose).to_have_text(expected)

    @allure.step('take screenshots full page Buttons')
    def take_screenshots_buttons(self, name: str,
                                 base_folder: str = r"E:\Study IT\Final_project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) /"screenshots_page_buttons"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")