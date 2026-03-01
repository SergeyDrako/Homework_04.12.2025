import pytest
from playwright.sync_api import Page
from page.drop_down_page import DropDownPage
from page.drop_down_multiple_selects import PageMultiple_Selects
from page.drop_checkbox import DropCheckbox


@pytest.fixture
def select_page(page: Page) -> Page:
   return DropDownPage(page)

@pytest.fixture
def multiple_selects(page: Page) -> Page:
   return PageMultiple_Selects(page)

@pytest.fixture
def but_page(page: Page) -> Page:
   return DropCheckbox(page)

