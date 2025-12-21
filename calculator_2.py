def calculator(a,b,operator):
    if operator== '+':
        return 'результат:' + str(a+b)
    elif operator== '-':
        return 'результат:' + str(a-b)
    elif operator== '*':
        return 'результат:' + str(a*b)
    elif operator== '/':
        return 'результат:' + str(a/b)
    elif operator== '**':
        return 'результат:' + str(a**b)
    else:
        return ('Некорректная операція')



print(calculator(5,3,'*'))