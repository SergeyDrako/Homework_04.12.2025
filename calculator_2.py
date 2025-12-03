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



calculator(1,2,'+')
print(calculator(1,2,'+'))