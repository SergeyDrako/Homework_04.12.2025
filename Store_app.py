from colorama import Fore, Back, Style
from Cashier import Cashier
from Menu import *
import bank_log
import logging

logger = logging.getLogger('bank_log')
cashier = Cashier()
state = 'main'
logger.info(f'Начало продаж.')

while True:
    if state == 'main':
        decision = main_menu()
        match decision:
            case '1':
                logger.info("Действия на кассе продавцом")
                state = 'cashier'
            case '2':
                logger.info("Cобытия на складе")
                state = 'warehouse'
            case '3': break
            case _:
                logger.info('Произошел выбор несуществующей позции')
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')

    elif state == 'cashier':
        decision = cashier_menu()
        match decision:
            case '1': cashier.sell_product()
            case '2': print(cashier)
            case '3': state = 'main'
            case _:
                logger.error('Произошел выбор несуществующей позции')
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')

    elif state == 'warehouse':
        decision = warehouse_menu()
        match decision:
            case '1':
                logger.info("Запрос добавление")
                cashier.add_product()
            case '2':
                logger.info("Запрос на удаление")
                cashier.remove_product()
            case '3':
                logger.info("Запрос на замену количества")
                cashier.change_quantity()
            case '4':
                logger.info("Запрос на замену цены")
                cashier.change_price()
            case '5': cashier.products
            case '6': state = 'main'
            case _:
                logger.error('Произошел выбор несуществующей позции')
                print(f'\n{Back.RED}{Fore.BLACK}Выберите один из пунктов меню\n'
                      f'{Style.RESET_ALL}')