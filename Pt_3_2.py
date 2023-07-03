from functools import reduce

n = int(input("Введите число: "))
list1 = [1, 1]
while list1[1] <= n:
    print(list1[1])
    x = reduce(lambda z, y: z + y, list1)
    list1[0] = list1[1]
    list1[1] = x
    print(list1)
