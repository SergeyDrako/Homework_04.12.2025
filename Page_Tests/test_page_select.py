from playwright.sync_api import Page, expect
import pytest
import enum
from pages.page_select import Choose_language
from pages.page_select import PageSelect
from pages.page_select import Local
from pages.page_select import Transport
from pages.page_select import Period
import time

@pytest.mark.parametrize('languages', [x.value for x in Choose_language])
def test_page_select_languages(page_select,languages: str)-> None:
    page_select.open()
    page_select.click_single_ui_elements()
    page_select.click_select()
    page_select.click_drop_down_languages(languages)
    page_select.submit()
    page_select.check_result(languages)
    page_select.take_screenshots_select_every_element(languages)

def test_text_multiple_selects(page_select)-> None:
    page_select.open()
    page_select.click_single_ui_elements()
    page_select.click_select()
    page_select.click_multiple_selects()
    page_select.check_text_contents_place("Choose the place you want to go*")
    page_select.check_text_contents_transport('Choose how you want to get there*')
    page_select.check_text_contents_period('Choose when you want to go*')

@pytest.mark.parametrize('place', [x.value for x in Local])
def test_select_multiple_place(page_select, place: str) -> None:
    page_select.open()
    page_select.click_single_ui_elements()
    page_select.click_select()
    page_select.click_multiple_selects()
    page_select.click_drop_down_transport('Air')
    page_select.click_drop_down_place(place)
    page_select.click_drop_down_period('Next week')
    page_select.submit()
    page_select.check_result(f'to go by air to the {place.lower()} next week')
    page_select.take_screenshots_select_every_element(place)

@pytest.mark.parametrize('transport', [x.value for x in Transport])
def test_select_transport(page_select, transport:str) -> None:
    page_select.open()
    page_select.click_single_ui_elements()
    page_select.click_select()
    page_select.click_multiple_selects()
    page_select.click_drop_down_place('Mountains')
    page_select.click_drop_down_transport(transport)
    page_select.click_drop_down_period('Tomorrow')
    page_select.submit()
    page_select.check_result(f'to go by {transport.lower()} to the mountains tomorrow')
    page_select.take_screenshots_select_every_element(transport)

@pytest.mark.parametrize('period', [x.value for x in Period])
def test_select_period(page_select, period:str) -> None:
    page_select.open()
    page_select.click_single_ui_elements()
    page_select.click_select()
    page_select.click_multiple_selects()
    page_select.click_drop_down_transport('Car')
    page_select.click_drop_down_place('Restaurant')
    page_select.click_drop_down_period(period)
    page_select.submit()
    page_select.check_result(f'to go by car to the restaurant {period.lower()}')
    page_select.take_screenshots_select_every_element(period)