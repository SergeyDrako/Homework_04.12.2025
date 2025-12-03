def calculator():
    a=int(input('введіте первое число: '))
    b=int(input('введіте второе число: '))
    operator=input('выберите операцию: ')
    if operator=='+':
        print('вы выбрали сумму')
        print('результат:', a+b)
    elif operator=='-':
        print('вы выбрали вычитание')
        print('результат:', a-b)
    elif operator=='*':
        print('вы выбрали умножение')
        print('результат:', a*b)
    elif operator=='/':
        print('вы выбрали деление')
        print('результат:', a/b)
    elif operator=='**':
        print('вы выбрали возведение в степень: ', b)
        print('результат:', a**b)
    else:
        print('Некорректная операція')
        print('результат:', None)



calculator()
