def parse_int_list(strings):
    lists = []
    for string in strings:
        try:
            lists.append(int(string))
        except ValueError:
            print(f"Ошибка: {string}! Водитель только числа")
    return lists

raw = ["10", "20", "abc", "30", "4.5", "40"]
# nums = parse_int_list(raw)
print(parse_int_list(raw))




