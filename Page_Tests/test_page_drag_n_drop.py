from playwright.sync_api import expect
import allure
import pytest
import enum
from pages.page_drag_n_drop import Page_Drag_n_Drop
import time

@allure.title("Test Page Drag n Drop button Boxes")
def test_page_drag_n_drop_boxes(page, page_drag_n_drop):
    page_drag_n_drop.open()
    page_drag_n_drop.click_single_ui_elements()
    page_drag_n_drop.click_drop_and_drop()
    page_drag_n_drop.click_button_boxes()
    page_drag_n_drop.check_visible_box_drag_me()
    page_drag_n_drop.check_visible_box_drop_here()
    page_drag_n_drop.drag_and_drop_drag_me_drop_here()
    page_drag_n_drop.check_result_text('Dropped!')
    page_drag_n_drop.take_screenshots_buttons('screenshots_looks_like_boxes_dropped')

@allure.title("Test Page Drag n Drop button Images")
def test_page_drag_n_drop_image_down_box(page, page_drag_n_drop):
    page_drag_n_drop.open()
    page_drag_n_drop.click_single_ui_elements()
    page_drag_n_drop.click_drop_and_drop()
    page_drag_n_drop.click_button_images()
    page_drag_n_drop.check_visible_image_smile()
    page_drag_n_drop.drag_image_by_coordinates_for_down_box()
    time.sleep(3)
    page_drag_n_drop.check_result_text_in_images_down_box('Dropped!')
    page_drag_n_drop.take_screenshots_buttons('screenshots_looks_like_image_down_box')
    page_drag_n_drop.drag_image_by_coordinates_for_top_box()
    time.sleep(3)
    page_drag_n_drop.check_result_text_in_images_top_box('Dropped!')
    page_drag_n_drop.take_screenshots_buttons('screenshots_looks_like_image_top_box')

