number = int(input("Введите натуральное число: "))
even_number = lambda x: x % 2 == 0
if even_number(number):
    print("Число четное!")
else:
    print("Число нечетное!")
