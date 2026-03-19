import pytest
from playwright.sync_api import Page
from pages.page_select import PageSelect
from pages.page_buttons import PageButtons
from pages.page_checkbox import ClickCheckbox
from pages.page_text_area import PageTextArea
from pages.page_practive_form import PagePracticeForm
from pages.page_alerts import PageAlerts

@pytest.fixture
def page_select(page: Page) -> PageSelect:
   return PageSelect(page)

@pytest.fixture
def page_buttons(page: Page) -> PageButtons:
   return PageButtons(page)

@pytest.fixture
def page_checkbox(page: Page) -> Page:
   return ClickCheckbox(page)

@pytest.fixture
def page_text_area(page: Page) -> PageTextArea:
      return PageTextArea(page)

@pytest.fixture
def page_practice_form(page: Page) -> PagePracticeForm:
    return PagePracticeForm(page)

@pytest.fixture
def page_alerts(page: Page) -> PageAlerts:
    return PageAlerts(page)