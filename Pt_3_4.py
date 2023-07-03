list_of_numbers = [int(input("Заполните список: ")) for x in range(10)]
print(list_of_numbers)
new_list = [n ** 2 for n in list_of_numbers]
print(new_list)
