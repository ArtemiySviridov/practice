def find_palindromes(message):
    all_palindromes = []
    for i in range(len(message)):
        for j in range(i+1, len(message) + 1):
            substring = message[i:j]
            if substring == substring[::-1] and len(substring) > 1:
                all_palindromes.append(substring)
    return all_palindromes


string = input("Введите строку: ")
palindromes = find_palindromes(string)
print("Палиндромы в строке:", palindromes)
