from playwright.sync_api import Page, expect
import pytest
import enum
from pages.page_text_area import PageTextArea
import time

def test_page_text_area_inputs(page_text_area)->None:
    page_text_area.open()
    page_text_area.click_single_ui_elements()
    page_text_area.click_text_area()
    page_text_area.click_button_textarea()
    page_text_area.check_visible_text_area_box_text()
    page_text_area.check_field_is_required_text_area_box_text()
    page_text_area.click_window_text_area_box_text()
    page_text_area.input_box_text_area_box_text("Hello Python. My name is Sergey. "
                                                "I'm 34 years old. Я узучаю язык программирования Python?!№")
    page_text_area.submit()
    page_text_area.check_result("Hello Python. My name is Sergey. I'm 34 years old. "
                                "Я узучаю язык программирования Python?!№")
    page_text_area.take_screenshots_text_area('creenshots_page_text_area_box_text')

def test_page_multiple_text_area(page_text_area)->None:
    page_text_area.open()
    page_text_area.click_single_ui_elements()
    page_text_area.click_text_area()
    page_text_area.click_button_multiple_textareas()
    page_text_area.check_visible_multiple_textareas_first_chapter()
    page_text_area.check_field_is_required_multiple_textareas_first_chapter_box_text()
    page_text_area.click_window_box_text_multiple_textareas_first_chapter()
    page_text_area.input_box_multiple_textareas_first_chapter_box_text("Hello Python. My name is Sergey. I'm 34 years old. "
                                                                       "Я узучаю язык программирования python?!№")
    page_text_area.check_visible_multiple_textareas_second_chapter()
    page_text_area.click_window_box_text_multiple_textareas_second_chapter()
    page_text_area.input_box_multiple_textareas_second_chapter_box_text('The weather has temperature plus 10 and a very sunny day today.')
    page_text_area.check_visible_multiple_textareas_third_chapter()
    page_text_area.click_window_box_text_multiple_textareas_third_chapter()
    page_text_area.input_box_multiple_textareas_third_chapter_box_text('My address: city Minsk, street Zhudro,54-89.'
                                                                       'I would like to get my order at this address')
    page_text_area.submit()
    page_text_area.check_result_multiple_textareas("Hello Python. My name is Sergey. I'm 34 years old. "
                                                   "Я узучаю язык программирования python?!№ "
                                                   "The weather has temperature plus 10 and a very sunny day today."
                                                   " My address: city Minsk, street Zhudro,54-89."
                                                   "I would like to get my order at this address")
    page_text_area.take_screenshots_text_area('creenshots_text_page_multiple_textareas')
