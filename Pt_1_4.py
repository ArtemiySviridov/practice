enter_num = int(input("Введите число от 10 до 20: "))
while (enter_num < 10) or (enter_num > 20):
    if enter_num < 10:
        print("Число меньше требуемого диапазона!")
        enter_num = int(input("Введите число от 10 до 20: "))
    if enter_num > 20:
        print("Число больше требуемого диапазона!")
        enter_num = int(input("Введите число от 10 до 20: "))
print("Спасибо!")