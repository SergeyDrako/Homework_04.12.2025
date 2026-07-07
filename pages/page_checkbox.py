from playwright.sync_api import expect
import enum
import os
import allure
from pathlib import Path
from datetime import datetime
from playwright.sync_api import sync_playwright
from utils_logger_test_QA_Practic.pages_base_page import BasePage

class PageCheckbox(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.url = "https://www.qa-practice.com/"
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_submit = page.locator('#submit-id-submit')
        self.result_choose = page.locator('#result-text')
        self.choose_checkbox = page.locator('a[href="/elements/checkbox"]')
        self.choose_checkboxes = page.locator('a[href="/elements/checkbox/mult_checkbox"]')
        self.choose_select_me_or_not = page.locator('#id_checkbox_0')
        self.choose_one = page.locator('#id_checkboxes_0')
        self.choose_two = page.locator('#id_checkboxes_1')
        self.choose_three = page.locator('#id_checkboxes_2')

    @allure.step('Open the website')
    def open(self):
        super().open(self.url)

    @allure.step('click in the page Single UI elements')
    def click_single_ui_elements(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_singleUI}")
        self.choose_singleUI.click()

    @allure.step('click in the page Checkbox')
    def click_checkbox(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_checkbox}")
        self.choose_checkbox.click()

    @allure.step('click in the button Single checkbox')
    def click_single_checkbox(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_checkbox}")
        self.choose_singleUI.click()

    @allure.step('click in button Select me or not')
    def click_select_me_or_not(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_select_me_or_not}")
        self.choose_select_me_or_not.click()

    @allure.step('click in the button Checkboxes')
    def click_checkboxes(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_checkboxes}")
        self.choose_checkboxes.click()

    @allure.step('click in the button One')
    def click_choise_one(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_one}")
        self.choose_one.click()

    @allure.step('click in the button Two')
    def click_choise_two(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_two}")
        self.choose_two.click()

    @allure.step('click in the button Three')
    def click_choise_three(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_three}")
        self.choose_three.click()

    @allure.step('click in the button Submit')
    def click_submit(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.result_choose}")
        self.choose_submit.click()

    allure.step('status_submit_enabled')
    def check_status_submit_enabled(self) -> None:
        self.logger.log_issue("INFO", f"Check status: {self.choose_submit}")
        expect(self.choose_submit).to_be_enabled()

    @allure.step('check result')
    def check_result(self, expected)-> None:
        self.logger.log_issue("INFO", f"Check result: {expected}")
        expect(self.result_choose).to_have_text(expected)

    @allure.step("Check the status of the page checkboxs result_is_empty")
    def check_checkboxs_result_is_empty(self) -> None:
        self.logger.log_issue("INFO", f"Check result: {self.result_choose}")
        expect(self.result_choose).to_be_hidden(timeout=5*1000)

    @allure.step('take screenshots full page Checkbox')
    def take_screenshots_checkbox(self, name: str,
                                  base_folder:str = r"E:\Study IT\Final_project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) / "screenshots_page_checkbox"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")