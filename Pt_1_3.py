first_num, second_num, third_num = map(int, input("Введите три числа: ").split())
list_of_num = [first_num, second_num, third_num]
print("Введенные числа: ", list_of_num)
print("Максимальный элемент списка: ", max(list_of_num))
print("Сортировка по убыванию: ", *(sorted(list_of_num, reverse=True)))
