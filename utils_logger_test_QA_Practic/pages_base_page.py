from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page, logger):
        self.page = page
        self.logger = logger

    def open(self, url: str):
        self.logger.log_issue("INFO", f"Open page: {url}")
        self.page.goto(url)

    # def click(self, locator, name="Элемент"):
    #     self.logger.log_issue("INFO", f"Клик по: {name}")
    #     locator.click()