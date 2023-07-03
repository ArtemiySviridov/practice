summ = 0
while True:
    number = int(input("Введите число: "))
    if number < 0:
        summ = summ + number
        print(f"Полученная сумма: {summ}")
    else:
        break
