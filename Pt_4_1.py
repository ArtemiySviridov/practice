number = input("Введите целое число: ")
list_of_numbers = list(number)
max_from_list = sorted(list_of_numbers, reverse=True)
print(*max_from_list)
