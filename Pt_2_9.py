number = input("Введите натуральное число: ")
max_digit = max(number)
front_index = number.index(max_digit) + 1
back_index = number[::-1].index(max_digit) + 1
print(f"Порядковый номер максимальной цифры с начала введенного числа: {front_index}")
print(f"Порядковый номер максимальной цифры с конца введенного числа: {back_index}")
