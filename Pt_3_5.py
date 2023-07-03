def func(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    if counter > 2:
        return False
    else:
        return True


list_of_numbers = [int(input("Заполните список: ")) for x in range(10)]
print(list_of_numbers)

new_list = [n for n in list_of_numbers if func(n)]
print(new_list)
