print("Уравнение имеет вид: ax^2+bx+x=0")
a = int(input("Введите значение коэффициента а: "))
b = int(input("Введите значение коэффициента b: "))
c = int(input("Введите значение коэффициента c: "))
print()
x = 0
x1 = 0
x2 = 0
discriminant = b ** 2 - 4 * a * c
if discriminant == 0:
    x = (b ** 2) / (2 * a)
    print(f"Дискриминант равен: {discriminant}")
    print(f"Уравнение имеет один корень: \nx = {x}")
elif discriminant > 0:
    print(f"Дискриминант равен: {discriminant}")
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print(f"Уравнение имеет два корня: \nx1 = {x1} \nx2 = {x2}")
else:
    print(f"Дискриминант равен: {discriminant}")
    print("Дискриминант меньше нуля. Корней нет!")
