number = int(input("Введите натуральное число: "))
for num in range(number):
    if num ** 2 <= number:
        num += 1
    else:
        print(f"Первое натуральное число, квадрат которого больше введенного числа: {num}")
        break
