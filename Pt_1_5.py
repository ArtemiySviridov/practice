points = int(input("Введите количество очков за матч: "))
if points == 0:
    print("Проигрыш")
if points == 1:
    print("Ничья")
if points == 3:
    print("Выигрыш")
else:
    print("Введено неверное число!")