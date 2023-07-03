from functools import reduce
list_of_numbers = [10, 88, 32, 12, 65, 85, -63]
list_length = len(list_of_numbers)
list_average = reduce(lambda x, y: x + y, list_of_numbers) / list_length
print(f"Среднее значение списка чисел: {list_average}")
