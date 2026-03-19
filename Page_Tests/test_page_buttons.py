from playwright.sync_api import Page, expect
import pytest
import enum
from pages.page_buttons import PageButtons
from pages.page_buttons import SelectState
import time

def test_page_buttons_simple_button(page_buttons):
    page_buttons.open()
    page_buttons.click_single_ui_elements()
    page_buttons.click_buttons()
    page_buttons.click_simple_button()
    page_buttons.push_button_click_simple_button()
    page_buttons.check_result('Submitted')
    page_buttons.take_screenshots_buttons('creenshots_simple_button')

def test_page_looks_like_button(page_buttons):
    page_buttons.open()
    page_buttons.click_single_ui_elements()
    page_buttons.click_buttons()
    page_buttons.click_looks_like_button()
    page_buttons.push_button_click_lookslike_button()
    page_buttons.check_result("Submitted")
    page_buttons.take_screenshots_buttons('creenshots_looks_like_button')

@pytest.mark.parametrize('text', [x.value for x in SelectState])
def test_buttons_elements(page_buttons, text:str) -> None:
    page_buttons.open()
    page_buttons.click_single_ui_elements()
    page_buttons.click_buttons()
    page_buttons.click_disabled()
    page_buttons.drop_select_state(text)
    if text == 'Enabled':
        page_buttons.check_status_submit_enabled()
        page_buttons.submit()
        page_buttons.check_result('Submitted')
    elif text == 'Disabled':
        page_buttons.check_status_submit_disabled()
    page_buttons.take_screenshots_buttons(text)