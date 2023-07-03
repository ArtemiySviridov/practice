start_point = int(input("Введите начало диапазона: "))
final_point = int(input("Введите конец диапазона: "))
summ = 0
for num in range(start_point + 1, final_point):
    summ += num
print(f"Сумма элементов диапазона от {start_point} до {final_point} = {summ}")
