stroke = input("Введите строку состоющую из букв: ")
dictionary = {}
vowel_dict = "ауоыиэяюёе"
for symbol in stroke:
    if symbol in vowel_dict:
        dictionary[symbol] = True
    else:
        dictionary[symbol] = False
print(dictionary)
