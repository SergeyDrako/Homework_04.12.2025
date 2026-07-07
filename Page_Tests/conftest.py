import pytest
import allure
from playwright.sync_api import Page
from pages.page_select import PageSelect
from pages.page_buttons import PageButtons
from pages.page_checkbox import PageCheckbox
from pages.page_text_area import PageTextArea
from pages.page_practice_form import PagePracticeForm
from pages.page_alerts import PageAlerts
from pages.page_inputs import PageInputs
from pages.page_drag_n_drop import Page_Drag_n_Drop
from utils_logger_test_QA_Practic.utils_test_logger import TestLogger

@pytest.fixture
def logger(request):
    test_name = request.node.name
    return TestLogger(test_name)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Скриншот делаем только если тест упал во время выполнения (call)
    if rep.when == 'call' and rep.failed:
        # Ищем объект страницы в аргументах теста
        page = item.funcargs.get('page')

        # Если page не передан напрямую, ищем его внутри ваших PageObjects
        if not page:
            for fixture_obj in item.funcargs.values():
                if hasattr(fixture_obj, 'page'):
                    page = fixture_obj.page
                    break

        if page and not page.is_closed():
            try:
                # Делаем скриншот в ПАМЯТЬ (байты), а не в файл.
                # Это гарантирует, что Allure получит данные сразу.
                screenshot = page.screenshot(full_page=True, timeout=5000)
                allure.attach(
                    screenshot,
                    name=f"ERROR_SCREENSHOT_{item.name}",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"\n[Ошибка Allure] Не удалось создать скриншот: {e}")

        # Добавляем лог ошибки (текстом)
        allure.attach(
            str(rep.longrepr),  # Весь текст ошибки (traceback)
            name="Full_Python_Error",
            attachment_type=allure.attachment_type.TEXT
        )

@pytest.fixture
def page_select(page: Page,logger) -> PageSelect:
   return PageSelect(page,logger)

@pytest.fixture
def page_buttons(page: Page, logger) -> PageButtons:
   return PageButtons(page,logger)

@pytest.fixture
def page_checkbox(page: Page,logger) -> PageCheckbox:
   return PageCheckbox(page,logger)

@pytest.fixture
def page_text_area(page: Page,logger) -> PageTextArea:
      return PageTextArea(page,logger)

@pytest.fixture
def page_practice_form(page: Page,logger) -> PagePracticeForm:
    return PagePracticeForm(page,logger)

@pytest.fixture
def page_alerts(page: Page,logger) -> PageAlerts:
    return PageAlerts(page,logger)

@pytest.fixture
def page_inputs(page: Page,logger) -> PageInputs:
    return PageInputs(page,logger)

@pytest.fixture
def page_drag_n_drop(page: Page,logger) -> Page_Drag_n_Drop:
    return Page_Drag_n_Drop(page,logger)