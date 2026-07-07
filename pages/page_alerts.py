from playwright.sync_api import expect
import allure
import enum
import os
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
from utils_logger_test_QA_Practic.pages_base_page import BasePage

class PageAlerts(BasePage):
    def __init__(self, page,logger):
        super().__init__(page,logger)
        self.url = "https://www.qa-practice.com/"
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_alerts = page.locator('a[href="/elements/alert"]')
        self.choose_alerts_box = page.get_by_role("link", name="Alert box")
        self.choose_confirmation_box = page.get_by_role("link", name="Confirmation box")
        self.choose_prompt_box = page.get_by_role("link", name="Prompt box")
        self.click_button_locator = page.locator('.a-button')
        self.result_text = page.locator("#result")

    @allure.step('Open the website')
    def open(self):
        super().open(self.url)

    @allure.step('click in the page Single UI elements')
    def click_single_ui_elements(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_singleUI}")
        self.choose_singleUI.click()

    @allure.step('click in the page alerts')
    def click_alerts(self)-> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_alerts}")
        self.choose_alerts.click()

    @allure.step('click in the confirmation box button')
    def click_confirmation_box(self)-> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_confirmation_box}")
        self.choose_confirmation_box.click()

    @allure.step('click in the prompt box button')
    def click_prompt_box(self)-> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_prompt_box}")
        self.choose_prompt_box.click()

    @allure.step('setting up dialog handler prompt box dismiss')
    def dialog_handler_prompt_box_dismiss(self)-> None:
        def handle(dialog):
            self.logger.log_issue("INFO", f"Dialog appeared: '{dialog.message}'. Dismissing it.")
            dialog.dismiss()
        self.page.once("dialog", handle)

    @allure.step('setting up dialog handler prompt box accept')
    def dialog_handler_prompt_box_accept(self,text_to_enter)-> None:
        self.logger.log_issue("INFO", f"Setting up handler to ACCEPT the next dialog: '{text_to_enter}'")
        self.page.once("dialog", lambda dialog: dialog.accept(text_to_enter))

    @allure.step('setting up dialog handler confirmation box')
    def dialog_handler_confirmation_box(self)-> None:
        self.logger.log_issue("INFO", "Setting up handler to ACCEPT the next Confirmation dialog")
        self.page.once("dialog", lambda dialog: dialog.accept())

    @allure.step('setting up handle dialog alerts box')
    def handle_dialog_alerts_box(self, dialog)-> None:
        self.logger.log_issue("INFO", f"Dialog message: '{dialog.message}'")
        assert dialog.message == "I am an alert!"
        dialog.accept()

    @allure.step('set a trap dialog handler alerts box')
    def dialog_handler_alerts_box(self)-> None:
        self.logger.log_issue("INFO", "Setting up listener for Alert")
        self.page.once("dialog", self.handle_dialog_alerts_box)

    @allure.step('check data confirmation box')
    def check_confirmation_box(self, value: str)-> None:
        self.logger.log_issue("INFO", f"Checking confirmation box: '{value}'")
        expect(self.result_text).to_have_text(value)

    @allure.step('check data prompt box')
    def check_prompt_box(self, value: str)-> None:
        self.logger.log_issue("INFO", f"Checking prompt box: '{value}'")
        expect(self.result_text).to_contain_text(value)

    @allure.step('click on the click button')
    def click_button(self)-> None:
        self.logger.log_issue("INFO", f"Click on: {self.click_button_locator}")
        self.click_button_locator.click()

    @allure.step('take screenshots  full page text area')
    def take_screenshots_text_area(self, name: str,
                                   base_folder: str = r"E:\Study IT\Final_project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) / "screenshots_alert_box"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")








