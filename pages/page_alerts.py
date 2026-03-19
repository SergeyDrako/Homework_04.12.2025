from playwright.sync_api import Page, expect
import enum
import os
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright

URL = "https://www.qa-practice.com/"

class PageAlerts(Page):
    def __init__(self, page):
        self.page = page
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_alerts = page.locator('a[href="/elements/alert"]')
        self.choose_alerts_box = page.get_by_role("link", name="Alert box")
        self.choose_confirmation_box = page.get_by_role("link", name="Confirmation box")
        self.choose_prompt_box = page.get_by_role("link", name="Prompt box")
        self.click_button_locator = page.locator('.a-button')
        self.result_text = page.locator("#result")

    def open(self):
        self.page.goto(URL)

    def click_single_ui_elements(self) -> None:
        self.choose_singleUI.click()

    def click_alerts(self)-> None:
        self.choose_alerts.click()

    def click_confirmation_box(self)-> None:
        self.choose_confirmation_box.click()

    def click_prompt_box(self)-> None:
        self.choose_prompt_box.click()

    def dialog_handler_prompt_box_dismiss(self)-> None:
        self.page.on("dialog", lambda dialog: dialog.dismiss())

    def dialog_handler_prompt_box_accept(self,test_name)-> None:
        self.page.on("dialog", lambda dialog: dialog.accept(test_name))

    def dialog_handler_confirmation_box(self)-> None:
        self.page.on("dialog", lambda dialog: dialog.accept())

    def dialog_handler_alerts_box(self)-> None:
        self.page.on("dialog", self.handle_dialog_alerts_box)

    def handle_dialog_alerts_box(self, dialog)-> None:
        print(f"Текст алерта: {dialog.message}")
        assert dialog.message == "I am an alert!"
        dialog.accept()

    def check_confirmation_box(self, value: str)-> None:
        expect(self.result_text).to_have_text(value)

    def check_prompt_box(self, value: str)-> None:
        expect(self.result_text).to_contain_text(value)

    def click_button(self)-> None:
        self.click_button_locator.click()

    def take_screenshots_text_area(self, name: str,
                                   base_folder: str = r"E:\Study IT\Final project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) / "screenshots_alert_box"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")








