def calculator():
    try:
        a=int(input('введите первое число: '))
        b=int(input('введите второе число: '))
    except(ValueError):
        print('Ведите целочисленное значение')
    else:
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
            try:
                print('вы выбрали деление')
                print('результат:', a/b)
            except(ZeroDivisionError):
                print("на ноль делить нельзя")
        elif operator=='**':
            print('вы выбрали возведение в степень: ', b)
            print('результат:', a**b)
        else:
            raise ValueError("Такая переция не поддерживается")
try:
    calculator()
except ValueError as e:
    print(e)