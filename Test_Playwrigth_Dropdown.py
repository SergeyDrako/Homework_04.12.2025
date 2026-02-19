from playwright.sync_api import Page,expect
import time
import pytest
import enum

# def test_select_language(page:Page) -> None:
#     page.goto("https://www.qa-practice.com/")
#     page.locator("text = Single UI Elements").click()
#     page.locator('a[href="/elements/select"]').click()
#
# # Первый вариант по проще, но более долгий.
#     choose_field = page.locator('#id_choose_language')
#     choose_field.select_option('Ruby')
#     time.sleep(3)
#     page.locator('#submit-id-submit').click()
#     expect(page.locator('#result-text')).to_have_text('Ruby')
#     time.sleep(3)
#
#     choose_field.select_option('C#')
#     time.sleep(3)
#     page.locator('#submit-id-submit').click()
#     expect(page.locator('#result-text')).to_have_text('C#')
#     time.sleep(3)
#
# # Проверили наличие необходимо текста к контейнерах.
#     expect( choose_field).to_contain_text('Python')
#     expect(choose_field).to_contain_text('Ruby')
#     expect(choose_field).to_contain_text('JavaScript')
#     expect(choose_field).to_contain_text('C#')
#
# # Быстрый способ проверить значения в выплывающем списке.
# class Choose_languages(enum.Enum):
#     PYTHON = 'Python'
#     RUBY = 'Ruby'
#     JAVASCRIPT = 'JavaScript'
#     SHARP = 'C#'
#
# @pytest.mark.parametrize('languages', [x.value for x in Choose_languages])
# def test_select_language_2(page:Page,languages: str) -> None:
#     page.goto("https://www.qa-practice.com/")
#     page.locator("text = Single UI Elements").click()
#     page.locator('a[href="/elements/select"]').click()
#
#     choose_field = page.locator('#id_choose_language')
#     choose_field.select_option(languages)
#     page.locator('#submit-id-submit').click()
#     expect(page.locator('#result-text'), languages)
#     time.sleep(3)


class Local(enum.Enum):
    SEA = 'Sea'
    MOUNTAINS = 'Mountains'
    OLD_TOWN = 'Old town'
    OCEAN = 'Ocean'
    RESTAURANT = 'Restaurant'

class Transport(enum.Enum):
    CAR = 'Car'
    BUS = 'Bus'
    TRAIN = 'Train'
    AIR = 'Air'

class Period(enum.Enum):
    TODAY = 'Today'
    TOMORROW = 'Tomorrow'
    NEXT_WEEK = 'Next week'

def test_text_Multiple(page:Page):
    page.goto("https://www.qa-practice.com/")
    page.locator("text = Single UI Elements").click()
    page.locator('a[href="/elements/select"]').click()
    page.locator('a[href="/elements/select/mult_select"]').click()

    expect(page.locator('label[for="id_choose_the_place_you_want_to_go"]')).to_have_text("Choose the place you want to go*")
    expect(page.locator('label[for="id_choose_how_you_want_to_get_there"]')).to_have_text('Choose how you want to get there*')
    expect(page.locator('label[for="id_choose_when_you_want_to_go"]')).to_have_text('Choose when you want to go*')

@pytest.mark.parametrize('place', [x.value for x in Local])
def test_select_Multiple_place(page:Page, place) -> None:
    page.goto("https://www.qa-practice.com/")
    page.locator("text = Single UI Elements").click()
    page.locator('a[href="/elements/select"]').click()
    page.locator('a[href="/elements/select/mult_select"]').click()

    page.locator('#id_choose_the_place_you_want_to_go').select_option(place)
    page.locator('#id_choose_how_you_want_to_get_there').select_option('Air')
    page.locator('#id_choose_when_you_want_to_go').select_option('Next week')
    time.sleep(2)
    page.locator('#submit-id-submit').click()
    expect(page.locator('#result-text')).to_have_text(f'to go by air to the {place.lower()} next week')


@pytest.mark.parametrize('transport', [x.value for x in Transport])
def test_select_transport(page:Page, transport) -> None:
    page.goto("https://www.qa-practice.com/")
    page.locator("text = Single UI Elements").click()
    page.locator('a[href="/elements/select"]').click()
    page.locator('a[href="/elements/select/mult_select"]').click()

    page.locator('#id_choose_how_you_want_to_get_there').select_option(transport)
    page.locator('#id_choose_the_place_you_want_to_go').select_option('Mountains')
    page.locator('#id_choose_when_you_want_to_go').select_option('Tomorrow')
    time.sleep(2)
    page.locator('#submit-id-submit').click()
    expect(page.locator('#result-text')).to_have_text(f'to go by {transport.lower()} to the mountains tomorrow')


@pytest.mark.parametrize('period', [x.value for x in Period])
def test_select_transport(page:Page, period) -> None:
    page.goto("https://www.qa-practice.com/")
    page.locator("text = Single UI Elements").click()
    page.locator('a[href="/elements/select"]').click()
    page.locator('a[href="/elements/select/mult_select"]').click()

    page.locator('#id_choose_how_you_want_to_get_there').select_option('Car')
    page.locator('#id_choose_the_place_you_want_to_go').select_option('Restaurant')
    page.locator('#id_choose_when_you_want_to_go').select_option(period)
    time.sleep(2)
    page.locator('#submit-id-submit').click()
    expect(page.locator('#result-text')).to_have_text(f'to go by car to the restaurant {period.lower()}')