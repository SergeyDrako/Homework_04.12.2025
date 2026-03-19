import os
import logging
from datetime import datetime

log_dir = "../logs my project"
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"test_run_page_text_area_QA_Practice{datetime.now().date()}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def log_test_issue(level, message, page=None):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    screenshot_path = ""

    if page:
        screenshot_dir = os.path.join(log_dir, "screenshots ERROR_DUG_WARNING")
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"screenshot_ERROR_DUG_WARNING_{timestamp}.png")
        page.screenshot(path=screenshot_path, full_page=True)

    full_msg = f"{message} \n Screenshot: {screenshot_path}" if screenshot_path else message

    if level.upper() == "ERROR":
        logger.error(full_msg)
    elif level.upper() == "WARNING":
        logger.warning(full_msg)
    else:
        logger.info(full_msg)

# Для отлова одной ошибки. Разовоая акция.
# def log_test_error(message: str, page=None):
#     log_dir = "logs my project"
#     screenshot_dir = os.path.join(log_dir, "screenshots Bug")
#     os.makedirs(screenshot_dir, exist_ok=True)
#
#     timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
#
#     screenshot_path = ""
#     if page:
#         screenshot_path = os.path.join(screenshot_dir, f"error_{timestamp}.png")
#         page.screenshot(path=screenshot_path, full_page=True)
#
#     file_path = os.path.join(log_dir, f"test_errors_{datetime.now().date()}.txt")
#     with open(file_path, "a", encoding="utf-8") as file:
#         file.write(f"[{timestamp}] ERROR and BUG LOG:\n")
#         file.write(f"{message}\n")
#         if screenshot_path:
#             file.write(f"Screenshot saved to: {screenshot_path}\n")
#         file.write("-" * 60 + "\n")