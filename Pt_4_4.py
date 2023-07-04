from functools import reduce
from itertools import combinations

k = int(input("Введите число для сравнения с суммой:"))
numbers = [1, 2, 3, 4]
unique_combinations = []

for r in range(1, len(numbers) + 1):
    combinations_r = combinations(numbers, r)
    unique_combinations.extend(combinations_r)
sum_comb = []
for i in unique_combinations:
    summa = reduce(lambda x, y: x + y, i)
    if summa == k:
        sum_comb.append(i)
print("Уникальные комбинации: ", unique_combinations)
print("Комбинации соответствующие введенному числу: ", sum_comb)
