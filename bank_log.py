import logging

formatter = logging.Formatter('time: %(asctime)s - name file: %(filename)s - '
                              'name logger: %(name)s - level: %(levelname)s - message: %(message)s',
                              datefmt = '%d/%m/%Y %I:%M:%S %p')

logger = logging.getLogger('bank_log')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('Data_log_shop.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)