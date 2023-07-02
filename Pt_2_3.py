number = int(input("Введите число: "))
number_to_stroke = str(number)
number_length = len(number_to_stroke)
summ = 0
for digit in number_to_stroke:
    summ += int(digit) ** number_length

if number == summ:
    print("Вы ввели число Армстронга!")
else:
    print("Вы ввели не число Армстронга!")
