import os
import logging
from datetime import datetime


class TestLogger:
    def __init__(self, test_name):
        self.base_log_dir = "logs_my_project"
        self.test_dir = os.path.join(self.base_log_dir, test_name)
        os.makedirs(self.test_dir, exist_ok=True)

        log_file = os.path.join(self.test_dir, f"execution.log")

        self.logger = logging.getLogger(test_name)
        self.logger.setLevel(logging.INFO)

        if self.logger.hasHandlers():
            self.logger.handlers.clear()

        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def log_issue(self, level, message, page=None):
        timestamp = datetime.now().strftime('%H-%M-%S')
        screenshot_path = ""

        if page:
            screenshot_name = f"screenshot_{level}_{timestamp}.png"
            screenshot_path = os.path.join(self.test_dir, screenshot_name)
            page.screenshot(path=screenshot_path, full_page=True)

        full_msg = f"{message} | Screenshot: {screenshot_path}" if screenshot_path else message

        if level.upper() == "ERROR":
            self.logger.error(full_msg)
        elif level.upper() == "WARNING":
            self.logger.warning(full_msg)
        else:
            self.logger.info(full_msg)