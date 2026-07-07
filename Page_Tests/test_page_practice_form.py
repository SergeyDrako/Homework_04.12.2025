from playwright.sync_api import expect
import allure
import pytest
import enum
from pages.page_practice_form import PagePracticeForm
from pages.page_practice_form import SelectState
from pages.page_practice_form import SelectCityStateNCR
from pages.page_practice_form import SelectCityUttarStatePradesh
from pages.page_practice_form import SelectCityStateHaryana
from pages.page_practice_form import SelectCityStateRajasthan
import time

@allure.title('Test Page Practice Form')
def test_page_practice_form(page_practice_form)->None:
    user = {
        'first_name': "Nec",
        'last_name': "BlackCat",
        'email' : 'drakoserge1990@gmail.com',
        'mobile': '8029375455',
        'birthday':{
            'year': '2019',
            'month': '10',
            'day': '20',
        },
        'subjects':'Maths',
        "address" : "city Minsk, street Zhudro",
        'state':'NCR',
        'city':'Delhi'
    }
    page_practice_form.open()
    page_practice_form.click_forms()
    page_practice_form.click_practice_form()
    page_practice_form.fill_practice_form(user)
    page_practice_form.click_submit()
    page_practice_form.check_result_input_data_forma(user)
    page_practice_form.check_result_click_gender_forma('Male')
    page_practice_form.check_result_click_hobbies_forma('Sports, Reading, Music')
    page_practice_form.check_result_row_state_and_city('NCR Delhi')
    page_practice_form.take_screenshots_practice_form('creenshots_practice_form')
