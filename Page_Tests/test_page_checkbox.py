from playwright.sync_api import Page, expect
import pytest
import enum
from pages.page_checkbox import ClickCheckbox
import time

def test_checkbox_elements_single_checkbox(page_checkbox):
    page_checkbox.open()
    page_checkbox.click_single_ui_elements()
    page_checkbox.click_checkbox()
    page_checkbox.click_single_checkbox()
    page_checkbox.click_select_me_or_not()
    page_checkbox.check_status_submit_enabled()
    page_checkbox.click_submit()
    page_checkbox.check_result('select me or not')
    page_checkbox.take_screenshots_checkbox('creenshots_checkbox_single_checkbox')

def test_check_elements_checkboxes_one(page_checkbox):
    page_checkbox.open()
    page_checkbox.click_single_ui_elements()
    page_checkbox.click_checkbox()
    page_checkbox.click_checkboxes()
    page_checkbox.click_choise_one()
    page_checkbox.check_status_submit_enabled()
    page_checkbox.click_submit()
    page_checkbox.check_result('one')
    page_checkbox.take_screenshots_checkbox('creenshots_checkbox_checkboxs_one')

def test_check_elements_checkboxes_two(page_checkbox):
    page_checkbox.open()
    page_checkbox.click_single_ui_elements()
    page_checkbox.click_checkbox()
    page_checkbox.click_checkboxes()
    page_checkbox.click_choise_two()
    page_checkbox.check_status_submit_enabled()
    page_checkbox.click_submit()
    page_checkbox.check_result('two')
    page_checkbox.take_screenshots_checkbox('creenshots_checkbox_checkboxs_two')

def test_check_elements_checkboxes_three(page_checkbox):
    page_checkbox.open()
    page_checkbox.click_single_ui_elements()
    page_checkbox.click_checkbox()
    page_checkbox.click_checkboxes()
    page_checkbox.click_choise_three()
    page_checkbox.check_status_submit_enabled()
    page_checkbox.click_submit()
    page_checkbox.check_result('three')
    page_checkbox.take_screenshots_checkbox('creenshots_checkbox_checkboxs_three')

def test_check_elements_checkboxes_all_elements(page_checkbox):
    page_checkbox.open()
    page_checkbox.click_single_ui_elements()
    page_checkbox.click_checkbox()
    page_checkbox.click_checkboxes()
    page_checkbox.click_choise_one()
    page_checkbox.click_choise_two()
    page_checkbox.click_choise_three()
    page_checkbox.check_status_submit_enabled()
    page_checkbox.click_submit()
    page_checkbox.check_result('one, two, three')
    page_checkbox.take_screenshots_checkbox('creenshots_checkbox_checkboxs_all_elements')

def test_check_elements_checkboxes_is_empty(page_checkbox):
    page_checkbox.open()
    page_checkbox.click_single_ui_elements()
    page_checkbox.click_checkbox()
    page_checkbox.click_checkboxes()
    page_checkbox.check_status_submit_enabled()
    page_checkbox.click_submit()
    page_checkbox.check_checkboxs_result_is_empty()
    page_checkbox.take_screenshots_checkbox('creenshots_checkbox_checkboxs_is_empty')