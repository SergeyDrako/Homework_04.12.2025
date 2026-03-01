from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import  pytest
import time
from enum import Enum
from page.page_forms import PagePracticeForm
from page.page_forms import Select_City_NCR
from page.page_forms import Select_City_Uttar_Pradesh
from page.page_forms import Select_City_Haryana
from page.page_forms import Select_City_Rajasthan
from page.page_forms import Select_State
from page.page_forms import RegistrationPage


# Тесты ввода данных
def test_text_input():
    browser = webdriver.Chrome()
    browser.maximize_window()
    actions = ActionChains(browser)
    wait = WebDriverWait(browser, 10)

    browser.get('https://www.qa-practice.com/elements/input/simple')
    element_1 = browser.find_element(By.ID, 'id_text_string')
    element_2 = browser.find_element(By.CSS_SELECTOR, 'a[href="/whats_new/"]')
    actions.move_to_element(element_1).perform()
    element_1.send_keys('Hello World')
    EC.text_to_be_present_in_element_value(element_1, 'Hello World')
    assert element_1.get_attribute('value') == 'Hello World'
    actions.move_to_element(element_2).perform()
    element_2.click()
    browser.quit()


def test_input_first_name(page_forms):
    page_forms.open_practice_form()
    page_forms.input_first_name("Nec")

def test_input_last_name(page_forms):
    page_forms.open_practice_form()
    page_forms.input_last_name("Cotavich")

def test_input_email(page_forms):
    page_forms.open_practice_form()
    page_forms.input_email("cat@gmail.com")

def test_input_phone(page_forms):
    page_forms.open_practice_form()
    page_forms.input_phone("+37544-111-11-11")

def test_input_subjects(page_forms):
    page_forms.open_practice_form()
    page_forms.input_subjects("There vacation in cat")

def test_input_current_address(page_forms):
    page_forms.open_practice_form()
    page_forms.input_current_address("city Minsk, street Skoda,10")

   # Тесты методов для click Gender
def test_ender_click_male(page_forms):
    page_forms.open_practice_form()
    page_forms.gender_click_male()

def test_gender_click_female(page_forms):
    page_forms.open_practice_form()
    page_forms.gender_click_female()

def test_gender_click_other(page_forms):
    page_forms.open_practice_form()
    page_forms.gender_click_other()

def test_hobbies_click_sport(page_forms):
    page_forms.open_practice_form()
    page_forms.hobbies_click_sport()

def test_hobbies_click_reading(page_forms):
    page_forms.open_practice_form()
    page_forms.hobbies_click_reading()

def test_hobbies_click_music(page_forms):
    page_forms.open_practice_form()
    page_forms.hobbies_click_music()

@pytest.mark.parametrize('select_state', [x.value for x in list(Select_State)])
def test_drop_select_state(registration_page, select_state:str):
    registration_page.open_practice_form()
    registration_page.drop_select_state(select_state)

@pytest.mark.parametrize('select_city', [x.value for x in list(Select_City_NCR)])
def test_drop_select_city(registration_page, select_city:str):
    registration_page.open_practice_form()
    registration_page.drop_select_state('NCR')
    registration_page.drop_select_city(select_city)

@pytest.mark.parametrize('select_city', [x.value for x in list(Select_City_Uttar_Pradesh)])
def test_drop_select_city(registration_page, select_city:str):
    registration_page.open_practice_form()
    registration_page.drop_select_state('Uttar Pradesh')
    registration_page.drop_select_city_1(select_city)

@pytest.mark.parametrize('select_city', [x.value for x in list(Select_City_Haryana)])
def test_drop_select_city(registration_page, select_city:str):
    registration_page.open_practice_form()
    registration_page.drop_select_state('Haryana')
    registration_page.drop_select_city(select_city)

@pytest.mark.parametrize('select_city', [x.value for x in list(Select_City_Rajasthan)])
def test_drop_select_city(registration_page, select_city:str):
    registration_page.open_practice_form()
    registration_page.drop_select_state('Rajasthan')
    registration_page.drop_select_city_1(select_city)








