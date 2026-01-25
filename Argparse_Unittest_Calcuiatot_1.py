import argparse
import datetime
parser = argparse.ArgumentParser(description='Проверка корректности ввода данных в калькулятор')
parser.add_argument('number_1', type = int, help='Первое число для ввода')
parser.add_argument('number_2', type = int, help='Второе число для ввода')
parser.add_argument('operator', type = str, choices =['+','-','*','/','**'] , help='Математические операции')
parser.add_argument('--time_operation', action = 'store_true', help='Длительность выполнения операции')
args = parser.parse_args()


def test_calculator(number_1, number_2, operator, time_operation):
    if time_operation:
        start_time = datetime.datetime.now()
    if operator == '+':
        result = number_1 + number_2
        print (f'{number_1} + {number_2} = {result}')
    elif operator == '-':
        result = number_1 - number_2
        print (f'{number_1} - {number_2} = {result}')
    elif operator == '*':
        result = number_1 * number_2
        print (f'{number_1} * {number_2} = {result}')
    elif operator == '/':
        if number_2 == 0:
            print('Деление на ноль невозможно') #ZeroDivisionError
            return
        else:
            result = number_1 / number_2
            print (f'{number_1} / {number_2} = {result}')
        return number_1 / number_2
    elif operator == '**':
        result = number_1 ** number_2
        print (f'{number_1} ** power_number or {number_2} ** {number_2} = {result}')
    else:
        print(f'Некорректно ведены данные')
    if time_operation:
        finish_time = datetime.datetime.now()
        data_time = finish_time - start_time
        print(f'Длительность выполнения операции: {finish_time - start_time} сек.')
        print(f'Дата выполнения операции: {finish_time - data_time}')


test_calculator(args.number_1,args.number_2,args.operator,args.time_operation)
