import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from enum import Enum

URL = "https://www.qa-practice.com/forms/practice-form"

class Select_State(Enum):
    NCR = 'NCR'
    UTTAR_PRADESH = 'Uttar Pradesh'
    HARYANA = 'Haryana'
    RAJASTHAN = 'Rajasthan'

class Select_City_NCR(Enum):
    DELHI = 'Delhi'
    GURGAON = 'Gurgaon'
    NOIDA = 'Noida'

class Select_City_Uttar_Pradesh(Enum):
    AGRA = 'Agra'
    LUCKNOW = 'Lucknow'
    MERRUT = 'Merrut'

class Select_City_Haryana(Enum):
    KARNAL = 'Karnal'
    PANIPAT = 'Panipat'

class Select_City_Rajasthan(Enum):
    JAIPUR = 'Jaipur'
    JAISELMER = 'Jaiselmer'

class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

    def expect_text_to_be(self, locator, expected_text):
        """Аналог expect(locator).to_have_text(text)"""
        return self.wait.until(
            EC.text_to_be_present_in_element(locator, expected_text),
            message=f"Текст в элементе {locator} не стал равен '{expected_text}'"
        )

    def expect_value_to_be(self, locator, expected_value):
        """Аналог expect(locator).to_have_value(value)"""
        return self.wait.until(
            EC.text_to_be_present_in_element_value(locator, expected_value),
            message=f"Value элемента {locator} не стало равно '{expected_value}'"
        )

class  PagePracticeForm:
    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(self.browser, 10)
        self.actions = ActionChains(self.browser)

        # настройка лакаторов ввода данных
        self.first_name = (By.XPATH, '//input[@name="first_name"]')
        self.last_name = (By.ID, 'lastName')
        self.email = (By.ID, 'userEmail')
        self.phone = (By.ID, 'userNumber')
        self.subjects = (By.ID, 'subjectsAutocomplete')
        self.current_address = (By.ID, 'currentAddress')

        # #настройка лакаторов для click Gender
        self.click_male = (By.ID, 'gender_0')
        self.click_female = (By.ID, 'gender_1')
        self.click_other = (By.ID, 'gender_2')
        self.click_hobbies_sport = (By.ID, 'hobbies_0')
        self.click_hobbies_reading = (By.ID, 'hobbies_1')
        self.click_hobbies_music = (By.ID, 'hobbies_2')
        #
        # #настройка лакатора drop_down.
        self.click_drop_state = (By.CSS_SELECTOR, '#div_id_state .custom-dropdown-control')
        self.click_drop_city = (By.CSS_SELECTOR, '#div_id_city .custom-dropdown-control')

        # #кнопка
        self.submit = (By.ID, 'submit-id-submit')
        self.result = (By.ID, 'resultsTable')
        #
        #загрузка файла
        self.file_loading = (By.ID,'uploadPicture')

    def open_practice_form(self) -> None:
        self.browser.get(URL)

        # настройка методов ввода данных
    def input_first_name(self, first_name_value:str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.first_name))
        element_first_name = self.browser.find_element(*self.first_name )
        self.actions.move_to_element(element_first_name).perform()
        element_first_name.clear()
        element_first_name.send_keys(first_name_value)
        assert element_first_name.get_attribute('value') == first_name_value

    def input_last_name(self, first_name_value:str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.last_name))
        element_last_name = self.browser.find_element(*self.last_name)
        self.actions.move_to_element(element_last_name).perform()
        element_last_name.clear()
        element_last_name.send_keys(first_name_value)
        assert element_last_name.get_attribute('value') == first_name_value

    def input_email(self, email_value:str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.email))
        element_email = self.browser.find_element(*self.email)
        self.actions.move_to_element(element_email).perform()
        element_email.clear()
        element_email.send_keys(email_value)
        assert element_email.get_attribute('value') == email_value

    def input_phone(self, phone_value:str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.phone))
        element_phone = self.browser.find_element(*self.email)
        self.actions.move_to_element(element_phone).perform()
        element_phone.clear()
        element_phone.send_keys(phone_value)
        assert element_phone.get_attribute('value') == phone_value

    def input_subjects(self, subjects_value:str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.subjects))
        element_subjects = self.browser.find_element(*self.subjects)
        self.actions.move_to_element(element_subjects).perform()
        element_subjects.clear()
        element_subjects.send_keys(subjects_value)
        assert element_subjects.get_attribute('value') == subjects_value

    def input_current_address(self, current_address_value:str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.current_address))
        element_address = self.browser.find_element(*self.current_address)
        self.actions.move_to_element(element_address).perform()
        element_address.clear()
        element_address.send_keys(current_address_value)
        assert element_address.get_attribute('value') == current_address_value

    # настройка методов для click Gender
    def gender_click_male(self)-> None:
        self.wait.until(EC.element_to_be_clickable(self.click_male))
        element_click_male = self.browser.find_element(*self.click_male)
        self.actions.move_to_element(element_click_male).perform()
        element_click_male.click()
        assert element_click_male.is_selected() #Гендер 'Male'  был выбран!"

    def gender_click_female(self)-> None:
        self.wait.until(EC.element_to_be_clickable(self.click_female))
        element_click_female = self.browser.find_element(*self.click_female)
        self.actions.move_to_element(element_click_female).perform()
        element_click_female.click()
        assert element_click_female.is_selected()

    def gender_click_other(self)-> None:
        self.wait.until(EC.element_to_be_clickable(self.click_other))
        element_click_other = self.browser.find_element(*self.click_other)
        self.actions.move_to_element(element_click_other).perform()
        element_click_other.click()
        assert element_click_other.is_selected()

    # настройка методов для click hobbies
    def hobbies_click_sport(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.click_hobbies_sport))
        element_click_sport = self.browser.find_element(*self.click_hobbies_sport)
        self.actions.move_to_element(element_click_sport).perform()
        element_click_sport.click()
        assert element_click_sport.is_selected()

    def hobbies_click_reading(self) -> None:
        self.wait.until(EC.element_to_be_clickable(self.click_hobbies_reading))
        element_click_reading = self.browser.find_element(*self.click_hobbies_reading)
        self.actions.move_to_element(element_click_reading).perform()
        element_click_reading.click()
        assert element_click_reading.is_selected()

    def hobbies_click_music(self)-> None:
        self.wait.until(EC.element_to_be_clickable(self.click_hobbies_music))
        element_click_music = self.browser.find_element(*self.click_hobbies_music)
        self.actions.move_to_element(element_click_music ).perform()
        element_click_music.click()
        assert element_click_music.is_selected()

    def click_submit(self) -> None:
        element_click_submit = self.wait.until(EC.element_to_be_clickable(self.submit))
        element_click_submit.click()
        assert "success" in self.result


    # Метод drop_select_state с универсальным метод в BasePage

class RegistrationPage(BasePage):
    # #настройка лакатора drop_down

    click_drop_state = (By.CSS_SELECTOR, '#div_id_state .custom-dropdown-control')
    click_drop_city = (By.CSS_SELECTOR, '#div_id_city .custom-dropdown-control')

    def open_practice_form(self) -> None:
        self.browser.get(URL)

    def drop_select_state(self, state: str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.click_drop_state))
        dropdown = self.browser.find_element(*self.click_drop_state)
        self.browser.execute_script("arguments[0].click();", dropdown)
        option = self.browser.find_element(By.CSS_SELECTOR, f'[data-value="{state}"]')
        self.browser.execute_script("arguments[0].click();", option)
        self.expect_text_to_be(self.click_drop_state, state)


    def drop_select_city(self, city: str) -> None:
        dropdown = self.wait.until(EC.element_to_be_clickable(self.click_drop_city))
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", dropdown)
        self.browser.execute_script("arguments[0].click();", dropdown)
        option_xpath = (By.XPATH, f"//div[contains(@class, '-menu')]//div[text()='{city}']")
        option_element = self.wait.until(EC.element_to_be_clickable(option_xpath))
        self.browser.execute_script("arguments[0].click();", option_element)
        self.expect_text_to_be(self.click_drop_city, city)

    def drop_select_city_1(self, city: str) -> None:
        self.wait.until(EC.visibility_of_element_located(self.click_drop_city))
        dropdown = self.browser.find_element(*self.click_drop_city)
        self.browser.execute_script("arguments[0].click();", dropdown)
        option_xpath = (By.XPATH, f"//*[contains(@class, '-menu')]//*[text()='{city}']")
        option_element = self.wait.until(EC.presence_of_element_located(option_xpath))
        self.browser.execute_script("arguments[0].click();", option_element)
        self.expect_text_to_be(self.click_drop_city, city)




































