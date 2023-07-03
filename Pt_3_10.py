stroke = input("Введите строку: ")
stroke = stroke.replace(" ", "")
dictionary = {letter: stroke.count(letter) for letter in stroke}
print(dictionary)
