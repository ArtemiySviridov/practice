dictionary = {}
alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
for symbol in alphabet:
    dictionary[symbol] = alphabet.index(symbol) + 1
print(dictionary)
