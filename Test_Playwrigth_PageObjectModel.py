from playwright.sync_api import Page,expect
import time
import pytest
import enum
from page.drop_down_multiple_selects import PageMultiple_Selects
from page.drop_down_multiple_selects import Local
from page.drop_down_multiple_selects import Transport
from page.drop_down_multiple_selects import Period

def test_text_Multiple(multiple_selects):
    # page_select_inputs = PageSelectInputs(page)
    multiple_selects.open()
    multiple_selects.single()
    multiple_selects.select()
    multiple_selects.multiple_selects()
    multiple_selects.check_text_contents_place("Choose the place you want to go*")
    multiple_selects.check_text_contents_transport('Choose how you want to get there*')
    multiple_selects.check_text_contents_period('Choose when you want to go*')
    multiple_selects.click_requirements()
    time.sleep(4)

@pytest.mark.parametrize('place', [x.value for x in Local])
def test_select_Multiple_place(multiple_selects, place: str) -> None:
    multiple_selects.open()
    multiple_selects.single()
    multiple_selects.select()
    multiple_selects.multiple_selects()

    multiple_selects.click_drop_transport('Air')
    multiple_selects.click_drop_place(place)
    multiple_selects.click_drop_period('Next week')
    multiple_selects.submit()
    multiple_selects.check_result(f'to go by air to the {place.lower()} next week')

@pytest.mark.parametrize('transport', [x.value for x in Transport])
def test_select_transport(multiple_selects, transport:str) -> None:
    multiple_selects.open()
    multiple_selects.single()
    multiple_selects.select()
    multiple_selects.multiple_selects()

    multiple_selects.click_drop_place('Mountains')
    multiple_selects.click_drop_transport(transport)
    multiple_selects.click_drop_period('Tomorrow')
    time.sleep(2)
    multiple_selects.submit()
    multiple_selects.check_result(f'to go by {transport.lower()} to the mountains tomorrow')

@pytest.mark.parametrize('period', [x.value for x in Period])
def test_select_period(multiple_selects, period:str) -> None:
    multiple_selects.open()
    multiple_selects.single()
    multiple_selects.select()
    multiple_selects.multiple_selects()

    multiple_selects.click_drop_transport('Car')
    multiple_selects.click_drop_place('Restaurant')
    multiple_selects.click_drop_period(period)
    time.sleep(2)
    multiple_selects.submit()
    multiple_selects.check_result(f'to go by car to the restaurant {period.lower()}')



