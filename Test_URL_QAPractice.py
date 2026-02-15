from playwright.sync_api import Page,expect
import time

def test_text_input(page:Page) -> None:
    page.goto("https://www.qa-practice.com/")
    page.locator("text = Single UI Elements").click()
    page.locator("text = Inputs").click()

    input_field = page.locator("#id_text_string")                   # Проверка поля ввода текста
    expect(input_field).to_have_count(1)
    expect(input_field).to_be_visible()
    expect(input_field).to_have_attribute('type','text')
    expect(input_field).to_have_attribute('name','text_string')
    input_field.fill('First Test') # тест что пользователь видет тест
    time.sleep(3)
    page.screenshot(path="./screenshot.png")

def test_buttons_elements(page: Page):
    page.goto("https://www.qa-practice.com/")
    page.locator("text = Single UI Elements").click()
    page.locator("text = Buttons").click()
    page.locator("text = Disabled").click()

    buttons_field = page.locator("#id_select_state")
    expect(buttons_field).to_have_count(1)
    expect(buttons_field).to_be_visible()
    expect(buttons_field).to_have_attribute('name', 'select_state')
    expect(buttons_field).to_have_attribute('name', 'select_state')
    expect(buttons_field).to_contain_text('Disabled')
    expect(buttons_field).to_contain_text('Disabled')
    expect(buttons_field).to_contain_text('Enabled')
    page.screenshot(path="./screenshot.png")

def test_checkbox_elements_one(page: Page):
    page.goto("https://www.qa-practice.com/")
    # page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    page.locator("text = Single UI Elements").click()
    page.locator('a[href="/elements/checkbox"]').click()
    # page.locator(".sub-menu", has_text="Checkbox").click()
    page.locator('a[href="/elements/checkbox/mult_checkbox"]').click()

    check_field_one = page.locator('#id_checkboxes_0')
    expect(check_field_one).to_have_count(1)
    expect(check_field_one).to_be_visible()
    check_field_one.check()
    time.sleep(3)
    page.screenshot(path="./screenshot.png")
    expect(check_field_one).to_be_checked()  # Изначально не выбран
    time.sleep(3)
    check_field_one.uncheck()
    expect(check_field_one).not_to_be_checked()# После снятия выбора не выбран
    time.sleep(3)
    page.screenshot(path="./screenshot.png")
    expect(check_field_one).to_have_attribute('name', 'checkboxes')
    expect(check_field_one).to_have_attribute('value', 'one')
    expect(check_field_one).to_be_editable()
    expect(check_field_one).to_have_accessible_name('One')
    page.screenshot(path="./screenshot.png")
    # expect(check_field_one).to_contain_text('One') # Спросить почему не рабает??
    # expect(check_field_one).toBeVisible() # Если автоматического ожидания недостаточно, можно для явной проверки состояния.

def test_checkbox_elements_two(page: Page):
    page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    check_field_two = page.locator("#id_checkboxes_1")
    expect(check_field_two).to_have_count(1)
    expect(check_field_two).to_be_visible()
    expect(check_field_two).to_have_attribute('name', 'checkboxes')
    expect(check_field_two).to_have_attribute('value', 'two')
    expect(check_field_two).to_have_accessible_name('Two')
    time.sleep(3)
    # expect(check_field_two).to_contain_text('Two')
    check_field_two.check()
    time.sleep(3)
    expect(check_field_two).to_be_checked() # проверяем, установлен ли флажок
    page.screenshot(path="./screenshot.png")
    expect(check_field_two).to_be_editable() # проверяем, можность работы ячейки на измнения
    time.sleep(3)
    check_field_two.uncheck()
    time.sleep(3)
    expect(check_field_two).not_to_be_checked()  # После снятия выбора не выбран
    page.screenshot(path="./screenshot.png")

def test_checkbox_elements_three(page: Page):
    page.goto("https://www.qa-practice.com/elements/checkbox/mult_checkbox")
    check_field_three = page.locator("#id_checkboxes_2")
    expect(check_field_three).to_have_count(1)
    expect(check_field_three).to_be_visible()
    expect(check_field_three).to_have_accessible_name('Three')
    # expect(check_field_three).to_contain_text('Three')
    expect(check_field_three).to_have_attribute('name', 'checkboxes')
    expect(check_field_three).to_have_attribute('value', 'three')
    check_field_three.check()
    time.sleep(3)
    expect(check_field_three).to_be_checked() # Изначально не выбран
    page.screenshot(path="./screenshot.png")
    check_field_three.uncheck()
    time.sleep(3)
    expect(check_field_three).not_to_be_checked()  # После снятия выбора не выбран
    page.screenshot(path="./screenshot.png")
    expect(check_field_three).to_have_accessible_name('Three')

def test_textarea_elements(page: Page):
    page.goto("https://www.qa-practice.com/")
    page.locator("text = Single UI Elements").click()
    time.sleep(3)
    page.locator('a[href="/elements/textarea/single"]').click()

    text_area_field = page.locator("#id_text_area")
    expect(text_area_field).to_have_count(1)
    expect(text_area_field).to_be_visible()
    expect(text_area_field).to_have_attribute('name', 'text_area')
    text_area_field.fill('Hello World')  # тест что пользователь видет тест
    time.sleep(3)
    page.screenshot(path="./screenshot.png")
    expect(text_area_field).to_have_value('Hello World')

 # Проверка кнопки Submit
def test_textarea_submit (page: Page):
    page.goto("https://www.qa-practice.com/")
    page.locator("text = Single UI Elements").click()
    time.sleep(3)
    page.locator('a[href="/elements/textarea/single"]').click()
 #  submit_button = page.locator('#submit-id-submit')
    submit_button = page.locator(".btn.btn-primary") # настройка локатора через class
    expect(submit_button).to_have_count(1)
    expect(submit_button).to_be_visible()
    submit_button.click()
    expect(submit_button).to_have_attribute('type', 'submit')
    expect(submit_button).to_have_attribute('name', 'submit')
    expect(submit_button).to_have_attribute('value', 'Submit')
    expect(submit_button).to_contain_text('Submit')
    page.screenshot(path="./screenshot.png")
