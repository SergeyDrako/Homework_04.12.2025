from playwright.sync_api import expect
import enum
import allure
import os
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
from utils_logger_test_QA_Practic.pages_base_page import BasePage

class Choose_language(enum.Enum):
    PYTHON = 'Python'
    RUBY = 'Ruby'
    JAVASCRIPT = 'JavaScript'
    SHARP = 'C#'

class Local(enum.Enum):
    SEA = 'Sea'
    MOUNTAINS = 'Mountains'
    OLD_TOWN = 'Old town'
    OCEAN = 'Ocean'
    RESTAURANT = 'Restaurant'

class Transport(enum.Enum):
    CAR = 'Car'
    BUS = 'Bus'
    TRAIN = 'Train'
    AIR = 'Air'

class Period(enum.Enum):
    TODAY = 'Today'
    TOMORROW = 'Tomorrow'
    NEXT_WEEK = 'Next week'

class PageSelect(BasePage):
    def __init__(self, page,logger):
        super().__init__(page, logger)
        self.url = "https://www.qa-practice.com/"
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_select = page.locator('a[href="/elements/select"]')
        self.choose_language = page.locator('#id_choose_language')
        self.choose_multipleSelects= page.locator('a[href="/elements/select/mult_select"]')

        self.choose_contents_place = page.locator('label[for="id_choose_the_place_you_want_to_go"]')
        self.choose_contents_transport = page.locator('label[for="id_choose_how_you_want_to_get_there"]')
        self.choose_contents_period = page.locator('label[for="id_choose_when_you_want_to_go"]')

        self.choose_drop_transport = page.locator('#id_choose_how_you_want_to_get_there')
        self.choose_drop_place = page.locator('#id_choose_the_place_you_want_to_go')
        self.choose_drop_period = page.locator('#id_choose_when_you_want_to_go')

        self.choose_requirements = page.locator('#req_header')

        self.choose_submit =  page.locator('#submit-id-submit')
        self.result = page.locator('#result-text')

    @allure.step('Open the website')
    def open(self):
        super().open(self.url)

    @allure.step('click in the page Single UI elements')
    def click_single_ui_elements(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_singleUI}")
        self.choose_singleUI.click()

    @allure.step('Click in the page  Select')
    def click_select(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_select}")
        self.choose_select.click()

    @allure.step('Click in the button Select')
    def click_multiple_selects(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_multipleSelects}")
        self.choose_multipleSelects.click()

    @allure.step('Click in the button drop_down_languages')
    def click_drop_down_languages(self,languages: str)-> None:
        self.logger.log_issue("INFO", f"Click on: {languages}")
        self.choose_language.select_option(languages)

    @allure.step('Click in the button drop_down_transport')
    def click_drop_down_transport(self,transports: str)-> None:
        self.logger.log_issue("INFO", f"Click on: {transports}")
        self.choose_drop_transport.select_option(transports)

    @allure.step('Click in the button drop_down_place')
    def click_drop_down_place(self,places: str)-> None:
        self.logger.log_issue("INFO", f"Click on: {places}")
        self.choose_drop_place.select_option(places)

    @allure.step('Click in the button drop_down_period')
    def click_drop_down_period(self,periods: str)-> None:
        self.logger.log_issue("INFO", f"Click on: {periods}")
        self.choose_drop_period.select_option(periods)

    @allure.step('Click in the button Submit')
    def submit(self) -> None:
        self.logger.log_issue("INFO", f"Submit: {self.result}")
        self.choose_submit.click()

    @allure.step('Check text contents place')
    def check_text_contents_place(self,phrase)-> None:
        self.logger.log_issue("INFO", f"Check: {phrase}")
        expect(self.choose_contents_place).to_have_text(phrase)

    @allure.step('Check text contents transport')
    def check_text_contents_transport(self,phrase)-> None:
        self.logger.log_issue("INFO", f"Check: {phrase}")
        expect(self.choose_contents_transport).to_have_text(phrase)

    @allure.step('Check text contents period')
    def check_text_contents_period(self,phrase)-> None:
        self.logger.log_issue("INFO", f"Check: {phrase}")
        expect(self.choose_contents_period).to_have_text(phrase)

    @allure.step('Check result')
    def check_result(self, expected_result)-> None:
        self.logger.log_issue("INFO", f"Check: {expected_result}")
        expect(self.result).to_have_text(expected_result)

    @allure.step('take screenshots full page Select')
    def take_screenshots_select_every_element(self, name: str,
                                              base_folder: str = r"E:\Study IT\Final_project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) / "screenshots_page_select"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")

