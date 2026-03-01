from playwright.sync_api import Page, expect
import enum

URL = "https://www.qa-practice.com/"

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

class PageMultiple_Selects(Page): # Multiselect
    def __init__(self, page):
        self.page = page
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_select = page.locator('a[href="/elements/select"]')
        self.choose_multipleSelects= page.locator('a[href="/elements/select/mult_select"]')

        self.choose_contents_place = page.locator('label[for="id_choose_the_place_you_want_to_go"]')
        self.choose_contents_transport = page.locator('label[for="id_choose_how_you_want_to_get_there"]')
        self.choose_contents_period = page.locator('label[for="id_choose_when_you_want_to_go"]')

        self.choose_drop_transport = page.locator('#id_choose_how_you_want_to_get_there')
        self.choose_drop_place = page.locator('#id_choose_the_place_you_want_to_go')
        self.choose_drop_period = page.locator('#id_choose_when_you_want_to_go')

        self.choose_requirements = page.locator('#req_header')

        self.choose_submit =  page.locator('#submit-id-submit')
        self.result_choice = page.locator('#result-text')

    def single(self) -> None:
        self.choose_singleUI.click()

    def select(self) -> None:
        self.choose_select.click()

    def multiple_selects(self) -> None:
        self.choose_multipleSelects.click()

    def check_text_contents_place(self,phrase)-> None:
        expect(self.choose_contents_place).to_have_text(phrase)

    def check_text_contents_transport(self,phrase)-> None:
        expect(self.choose_contents_transport).to_have_text(phrase)

    def check_text_contents_period(self,phrase)-> None:
        expect(self.choose_contents_period).to_have_text(phrase)

    def click_requirements(self)-> None:
        self.choose_requirements.click()

    def click_drop_transport(self,transports: str)-> None:
        self.choose_drop_transport.select_option(transports)

    def click_drop_place(self,places: str)-> None:
        self.choose_drop_place.select_option(places)

    def click_drop_period(self,periods: str)-> None:
        self.choose_drop_period.select_option(periods)

    def submit(self) -> None:
        self.choose_submit.click()

    def check_result(self, expected_result)-> None:
        expect(self.result_choice).to_have_text(expected_result)

    def open(self):
        self.page.goto(URL)
