from playwright.sync_api import expect
import allure
import pytest
import enum
from pages.page_alerts import PageAlerts
import time

@allure.title('test alert box there is text: "I am an alert!"')
def test_alert_box(page_alerts)-> None:
    page_alerts.open()
    page_alerts.click_single_ui_elements()
    page_alerts.click_alerts()
    page_alerts.dialog_handler_alerts_box()
    page_alerts.click_button()
    page_alerts.take_screenshots_text_area('creenshots_page_alerts')

@allure.title('test confirmation box there is text: "You selected\nCancel"')
def test_confirmation_box(page_alerts)-> None:
    page_alerts.open()
    page_alerts.click_single_ui_elements()
    page_alerts.click_alerts()
    page_alerts.click_confirmation_box()
    page_alerts.click_button()
    page_alerts.dialog_handler_confirmation_box()
    page_alerts.check_confirmation_box('You selected\nCancel')
    page_alerts.take_screenshots_text_area("creenshots_confirmation_box")

@allure.title('test prompt box dismiss there is text: "You canceled the prompt"')
def test_prompt_box_dismiss(page_alerts)-> None:
    page_alerts.open()
    page_alerts.click_single_ui_elements()
    page_alerts.click_alerts()
    page_alerts.click_prompt_box()
    page_alerts.dialog_handler_prompt_box_dismiss()
    page_alerts.click_button()
    page_alerts.check_prompt_box('You canceled the prompt')
    page_alerts.take_screenshots_text_area('creenshots_prompt_box_dismiss')

@allure.title('test prompt box accept there is text: "I like Python"')
def test_prompt_box_accept(page_alerts)-> None:
    page_alerts.open()
    page_alerts.click_single_ui_elements()
    page_alerts.click_alerts()
    page_alerts.click_prompt_box()
    page_alerts.dialog_handler_prompt_box_accept('I like Python')
    page_alerts.click_button()
    page_alerts.check_prompt_box('I like Python')
    page_alerts.take_screenshots_text_area('creenshots_prompt_box_accept')
