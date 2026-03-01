import pytest
from selenium import webdriver
from page.page_forms import PagePracticeForm
from page.page_forms import RegistrationPage

# Фикстура для инициализации и закрытия браузера
@pytest.fixture
def my_driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()

@pytest.fixture
def page_forms(my_driver):
    return PagePracticeForm(my_driver)

@pytest.fixture
def registration_page(my_driver):
    return RegistrationPage(my_driver)
