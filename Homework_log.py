# import logging

# # Exercise_1
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%m/%d/%Y %I:%M:%S %p')
#
# logging.info('Тест запущен')
#
# #Exercise_2
# file_handler = logging.FileHandler('test_results.log',encoding='utf-8')
# logger = logging.getLogger()
# logger.addHandler(file_handler )
# logging.info('Тест запущен')

#Exercise_3
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler('Exercise_3.log',encoding='utf-8')
# file_handler.setLevel(logging.DEBUG)
#
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
# logger.info("В консоль и файл")
# logger.debug("Только в файл")

#Exercise_4
# import logging
# logging.basicConfig(
#                     filename='report_log.log',encoding='utf-8',
#                     level=logging.INFO,
#                     format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt = '%m/%d/%Y %I:%M:%S %p')
#
# url = "https://api.example.com/users"
# expected_status = 200
#
# logging.info("Запуск теста")
# logging.info(f"URL: {url}")
# logging.error(f"Ожидали статус: {expected_status}, пришел статус: 404")

#Exercise_5

import logging
import requests
#
# # Настройка логирования с указанием кодировки
# logging.basicConfig(filename='Test_URL.log',encoding='utf-8',
#                     level=logging.ERROR,
#                     format='%(asctime)s - %(filename)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt = '%d/%m/%Y %H:%M:%S %p')
#
# # чтобы выводить сообщения на кирилице
formatter = logging.Formatter('time: %(asctime)s - name file: %(filename)s - '
                              'name logger: %(name)s - level: %(levelname)s - message: %(message)s',
                              datefmt = '%d/%m/%Y %H:%M:%S %p')

logger = logging.getLogger('bank_log_shop')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Test_URL.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

try:
    response = requests.get("http://bad-url")
    logger.debug("Ответ:%s", response.status_code)
    assert response.status_code == 200, f"Ожидали получить 200 — успех. Получил: {response.status_code}"

except requests.exceptions.HTTPError as http_err:
    logger.error(f"Ошибка при запросе к несуществующей конечной точке (404 Not Found)")
except requests.exceptions.Timeout as timeout_err:
    logger.error(f'Превышено время ожидания : {timeout_err}')
except requests.exceptions.ConnectionError as connection_err:
    logger.error(f"Ошибка соединения: {connection_err}")
except requests.exceptions.RequestException as req_err:
    logger.info(f"Произошла другая ошибка запроса: {req_err}")
except Exception as err:
    logger.exception(f"Непредвиденная ошибка: {err}")



