def simple_nums(number1):
    counter = 0
    for num in range(1, number1 + 1):
        if number1 % num == 0:
            counter += 1
    if counter == 2:
        return True
    else:
        return False


lower_border = int(input("Введите нижнюю границу диапазона: "))
upper_border = int(input("Введите верхнюю границу диапазона: "))

for number in range(lower_border, upper_border + 1):
    if simple_nums(number):
        print(number)
