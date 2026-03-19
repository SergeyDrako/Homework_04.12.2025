import email

from playwright.sync_api import Page, expect
import enum
import os
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
from Page_Tests.utils_logger import log_test_issue

URL = "https://www.qa-practice.com/"

class SelectState(enum.Enum):
    NCR = 'NCR'
    UTTAR_PRADESH = 'Uttar Pradesh'
    HARYANA = 'Haryana'
    RAJASTHAN = 'Rajasthan'

class SelectCityStateNCR(enum.Enum):
    DELHI = 'Delhi'
    GURGAON = 'Gurgaon'
    NOIDA = 'Noida'

class SelectCityUttarStatePradesh(enum.Enum):
    AGRA = 'Agra'
    LUCKNOW = 'Lucknow'
    MERRUT = 'Merrut'

class SelectCityStateHaryana(enum.Enum):
    KARNAL = 'Karnal'
    PANIPAT = 'Panipat'

class SelectCityStateRajasthan(enum.Enum):
    JAIPUR = 'Jaipur'
    JAISELMER = 'Jaiselmer'

class PagePracticeForm:
    def __init__(self, page):
        self.page = page
        self.choose_forms = page.locator("text = Forms")
        self.choose_practice_form = page.locator('a[href="/forms/practice-form"]')

        # настройка лакаторов ввода данных
        self.input_first_name = page.locator('//input[@name="first_name"]')
        self.input_last_name = page.locator('//input[@name="last_name"]')
        self.input_email = page.locator('//input[@name="email"]')
        self.input_mobile = page.locator('//input[@name="mobile"]')
        self.input_subjects = page.locator('#subjectsAutocomplete')
        self.input_current_address = page.locator('//textarea[@name="current_address"]')
        self.date_input = page.locator("#date_of_birth")
        self.month_select = page.locator(".ui-datepicker-month")
        self.year_select = page.locator(".ui-datepicker-year")
        self.day_locator = self.page.locator(".ui-state-default")

        #настройка лакаторов для click
        self.click_gender_male = page.locator('#gender_0')
        self.click_gender_female = page.locator('#gender_1')
        self.click_gender_other = page.locator('#gender_2')
        self.click_hobbies_sport = page.locator('#hobbies_0')
        self.click_hobbies_reading = page.locator('#hobbies_1')
        self.click_hobbies_music = page.locator('#hobbies_2')
        self.click_subjects = page.locator('.suggestion-item')

        # настройка лакаторов для birthday
        self.click_date_input = page.locator("#dateOfBirthInput")
        self.click_month = page.locator("//*[@role='navigator']/div[@role='period' and text() = 'March 2026']")
        self.click_years = page.locator("//*[@role='navigator']/div[@role='period' and text()='2026']")
        self.click_year_2019 = page.locator("table").get_by_role("cell", name="2019")
        self.click_month_oct = page.locator("table").get_by_role("cell", name="Oct")
        self.click_day_20 = page.locator("table").get_by_role("cell", name="20")

        #настройка лакаторов для downloads
        self.choose_downloads_picture = page.locator('#uploadPicture')

        # настройка лакатора drop_down.
        self.state_container =  page.locator('//div[@class="custom-dropdown-control"]')
        self.city_container = page.locator('//span[@class="selected-value placeholder"]')
        self.click_state_NCR = page.locator('#div_id_state .custom-dropdown-option').get_by_text("NCR", exact=True)
        self.click_city_Delhi = page.locator('#div_id_city .custom-dropdown-option').get_by_text("Delhi", exact=True)

        #настройка лакатора кнопка birthday
        self.submit = page.locator('#submit-id-submit')
        self.result = page.locator('#resultsModal')

        # настройка лакатора табло результатов
        self.row_title = self.page.locator('.modal-title')
        self.row_title.student_name = self.page.locator('#resultsTable').locator("tr", has_text="Student Name")
        self.row_student_email = self.page.locator('#resultsTable').locator("tr", has_text="Student Email")
        self.row_gender = self.page.locator('#resultsTable').locator("tr", has_text="Gender")
        self.row_mobile = self.page.locator('#resultsTable').locator("tr", has_text="Mobile")
        self.row_date_birth = self.page.locator('#resultsTable').locator("tr", has_text="Date of Birth")
        self.row_subjects = self.page.locator('#resultsTable').locator("tr", has_text="Subjects")
        self.row_hobbies = self.page.locator('#resultsTable').locator("tr", has_text="Hobbies")
        self.row_address = self.page.locator('#resultsTable').locator("tr", has_text="Address")
        self.row_state_and_city = self.page.locator("#resultsTable").locator("tr", has_text="State")

    def open(self)-> None:
        self.page.goto(URL)

    def click_forms(self)-> None:
        self.choose_forms.click()

    def click_practice_form(self)-> None:
        self.choose_practice_form.click()

    def fill_practice_form(self, user: dict)-> None:
        self.input_first_name.fill(user['first_name'])
        self.input_last_name.fill(user['last_name'])
        self.input_email.fill(user['email'])
        self.click_gender_male.click()
        self.input_mobile.fill(user['mobile'])
        self.click_date_input.click()
        self.click_month.click()
        self.click_years.click()
        self.click_year_2019.click()
        self.click_month_oct.click()
        self.click_day_20.click()
        self.input_subjects.fill(user['subjects'])
        self.page.keyboard.press("Enter")
        self.click_hobbies_sport.click()
        self.click_hobbies_reading.click()
        self.click_hobbies_music.click()
        self.input_current_address.fill(user['address'])
        self.state_container.click()
        self.click_state_NCR.click()
        self.city_container.click()
        self.click_city_Delhi.click()

    def click_submit(self) -> None:
        self.submit.click()

    def check_result(self, value)-> None:
        expect(self.result).to_contain_text(value)

    def check_result_input_data_forma(self, user)-> None:
        expect(self.row_title).to_have_text("Thanks for submitting the form")
        expect(self.row_title.student_name).to_contain_text(f"{user['first_name']} {user['last_name']}")
        expect(self.row_student_email).to_contain_text(f"{user['email']}")
        expect(self.row_mobile).to_contain_text(f"{user['mobile']}")
        expect(self.row_date_birth).to_contain_text(f"{user['birthday']['year']}-{user['birthday']['month']}-{user['birthday']['day']}")
        expect(self.row_subjects).to_contain_text(f"{user['subjects']}")
        expect(self.row_address).to_contain_text(f"{user['address']}")

    def check_result_row_state_and_city(self, expected: str) -> None:
        try:
            expect(self.row_state_and_city).to_contain_text(expected)
            print("Проверка текста пройдена успешно.")

        except AssertionError:
            actual_text = self.row_state_and_city.inner_text()
            log_test_issue(
                level="ERROR",
                message=f"Текст в поле #result-text не соответствует ожидаемому.\n ОЖИДАЛИ: '{expected}' \n ПОЛУЧИЛИ: '{actual_text}'",
                page=self.page
            )

    def check_result_click_gender_forma(self,value):
        expect(self.click_gender_male).to_be_visible()
        expect(self.click_gender_male).to_have_attribute("required", "")
        expect(self.row_gender).to_contain_text(value)

    def check_result_click_hobbies_forma(self, value):
        expect(self.click_hobbies_sport).to_be_visible()
        expect(self.click_hobbies_reading).to_be_visible()
        expect(self.click_hobbies_music).to_be_visible()
        expect(self.row_hobbies).to_contain_text(value)

    def take_screenshots_practice_form(self, name: str,
                                       base_folder:str = r"E:\Study IT\Final project_Test_QA_Practic\screenshots_all_page") -> None:
        folder = Path(base_folder) / "screenshots_practice_form"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.result.wait_for(state="visible")
        self.result.screenshot(path=file_path)
        print(f"Скриншот сохранен: {filename}")




