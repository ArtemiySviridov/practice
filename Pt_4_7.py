import itertools
message = input("Введите строку: ")
permutations = itertools.permutations(message)
count = 0
for elem in permutations:
    count += 1
print("Количество перестановок: ", count)
