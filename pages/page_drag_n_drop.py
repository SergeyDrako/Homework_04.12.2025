from playwright.sync_api import expect
import allure
import enum
import os
import re
import pytest
from datetime import datetime
from pathlib import Path
from playwright.sync_api import sync_playwright
from utils_logger_test_QA_Practic.pages_base_page import BasePage

class Page_Drag_n_Drop(BasePage):
    def __init__(self, page, logger):
        super().__init__(page, logger)
        self.url = "https://www.qa-practice.com/"
        self.choose_singleUI = page.locator("text = Single UI Elements")
        self.choose_drag_and_drop = page.locator('a[href="/elements/dragndrop"]')
        self.choose_button_boxes = page.locator('a[href="/elements/dragndrop/boxes"]')
        self.choose_button_images = page.locator('a[href="/elements/dragndrop/images"]')
        self.choose_box_drag_me = page.locator('#rect-draggable')
        self.choose_box_drop_here = page.locator('#rect-droppable')
        self.choose_box_images_number_1 = page.locator('#rect-droppable1')
        self.choose_box_images_number_2 = page.locator('#rect-droppable2')
        self.choose_smile = page.locator(".rect-draggable.ui-draggable.ui-draggable-handle")
        self.choose_result = page.locator('#text-droppable')
        self.choose_result_text_in_images_top_box = page.locator("#rect-droppable1")
        self.choose_result_text_in_images_down_box = page.locator("#rect-droppable2")

    @allure.step('Open the website')
    def open(self):
        super().open(self.url)

    @allure.step('click in the page Single UI elements')
    def click_single_ui_elements(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_singleUI}")
        self.choose_singleUI.click()

    @allure.step('click in the page Drop and Drop')
    def click_drop_and_drop(self) -> None:
        self.logger.log_issue("INFO", f"Click on page: {self.choose_drag_and_drop}")
        self.choose_drag_and_drop.click()

    @allure.step('Click on the buttons Boxes')
    def click_button_boxes(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_button_boxes}")
        self.choose_button_boxes.click()

    @allure.step('Click on the button images')
    def click_button_images(self) -> None:
        self.logger.log_issue("INFO", f"Click on: {self.choose_button_images}")
        self.choose_button_images.click()

    @allure.step('check visible box Drag me')
    def check_visible_box_drag_me(self) -> None:
        self.logger.log_issue("INFO", "Checking the visibility box Drag me")
        expect(self.choose_box_drag_me).to_be_visible()

    @allure.step('check visible box Drop here')
    def check_visible_box_drop_here(self) -> None:
        self.logger.log_issue("INFO", "Checking the visibility box Drop here")
        expect(self.choose_box_drop_here).to_be_visible()

    @allure.step('check visible image smile')
    def check_visible_image_smile(self) -> None:
        self.logger.log_issue("INFO", "Checking the visibility image smile")
        expect(self.choose_smile).to_be_visible(timeout=5000)

    @allure.step('Перетаскивает блок "Drag me" в блок "Drop here"')
    def drag_and_drop_drag_me_drop_here(self)-> None:
        self.logger.log_issue("INFO","Перетаскивает блок 'Drag me' в блок 'Drop here'")
        self.choose_box_drag_me.drag_to(self.choose_box_drop_here)

    @allure.step('Перетаскивает смайлик из нижнего квадрата в верхний ')
    def drag_and_drop_smile_from_box_2_to_box_1(self) -> None:
        self.logger.log_issue("INFO", "Перетаскивает блок 'Drag me' в блок 'Drop here'")
        self.choose_smile.drag_to(self.choose_box_images_number_1)

    @allure.step('Перетаскивает картинку по координатам в нижний бокс')
    def drag_image_by_coordinates_for_down_box(self) -> None:
        self.logger.log_issue("INFO", "Starting drag and drop image by coordinates in down box")

        # 1. Получаем координаты и размеры картинки-смайлика
        source_box = self.choose_smile.bounding_box()

        #  Находим точный центр картинки
        start_x = source_box["x"] + source_box["width"] / 2
        start_y = source_box["y"] + source_box["height"] / 2

        # 2. Получаем координаты зоны, КУДА нужно сбросить
        target_box = self.choose_box_images_number_2.bounding_box()

        # Находим точный центр целевой зоны
        end_x = target_box["x"] + target_box["width"] / 2
        end_y = target_box["y"] + target_box["height"] / 2

        # 3. Выполняем низкоуровневое перемещение мыши
        self.page.mouse.move(start_x, start_y)  # Наводим курсор на центр смайлика
        self.page.mouse.down()  # Зажимаем левую кнопку мыши

        # Перемещаем мышь к цели. steps=20 делает движение плавным (имитация человека)
        self.page.mouse.move(end_x, end_y, steps=20)

        self.page.mouse.up()  # Отпускаем кнопку мыши
        self.page.mouse.move(0, 0)
        self.logger.log_issue("INFO", "Drag and drop image completed")

    @allure.step('Перетаскивает картинку по координатам в верхний бокс')
    def drag_image_by_coordinates_for_top_box(self) -> None:
        self.logger.log_issue("INFO", "Starting drag and drop image by coordinates in top box")

        # 1. Получаем координаты и размеры картинки-смайлика
        source_box = self.choose_smile.bounding_box()

        #  Находим точный центр картинки
        start_x = source_box["x"] + source_box["width"] / 2
        start_y = source_box["y"] + source_box["height"] / 2

        # 2. Получаем координаты зоны, КУДА нужно сбросить
        target_box = self.choose_box_images_number_1.bounding_box()

        # Находим точный центр целевой зоны
        end_x = target_box["x"] + target_box["width"] / 2
        end_y = target_box["y"] + target_box["height"] / 2

        # 3. Выполняем низкоуровневое перемещение мыши
        self.page.mouse.move(start_x, start_y)  # Наводим курсор на центр смайлика
        self.page.mouse.down()  # Зажимаем левую кнопку мыши

        # Перемещаем мышь к цели. steps=20 делает движение плавным (имитация человека)
        self.page.mouse.move(end_x, end_y, steps=20)

        self.page.mouse.up()  # Отпускаем кнопку мыши
        self.page.mouse.move(0, 0)
        self.logger.log_issue("INFO", "Drag and drop image completed")

    @allure.step('Check text after dragging')
    def check_result_text(self, expected: str) -> None:
        self.logger.log_issue("INFO", f"Check text after dragging: {expected}")
        expect( self.choose_result).to_contain_text(expected)

    @allure.step('Check text after dragging tob box')
    def check_result_text_in_images_top_box(self, expected: str) -> None:
        self.logger.log_issue("INFO", f"Check text after dragging tob box: {expected}")
        expect(self.choose_result_text_in_images_top_box).to_have_text(expected)

    @allure.step('Check text after dragging down box')
    def check_result_text_in_images_down_box(self, expected: str) -> None:
        self.logger.log_issue("INFO", f"Check text after dragging down box: {expected}")
        expect(self.choose_result_text_in_images_down_box).to_have_text(expected)

    @allure.step('take screenshots full page Drag and drop')
    def take_screenshots_buttons(self, name: str,
                                 base_folder: str = r"E:\Study IT\Final_project_Test_QA_Practic\screenshots_all_page"):
        folder = Path(base_folder) / "screenshots_page_drag_n_drop"
        os.makedirs(folder, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"{timestamp}_{name}.png"
        file_path = os.path.join(folder, filename)
        self.page.screenshot(path=file_path, full_page=True)
        print(f"Скриншот сохранен: {filename}")



