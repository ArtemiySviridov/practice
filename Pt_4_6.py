alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
message = input("Введите строку: ").upper()
result = ''

for letter in message:
    letter_index_in_alphabet = alphabet.index(letter)
    new_index_of_letter = letter_index_in_alphabet + 13
    if letter in alphabet:
        result += alphabet[new_index_of_letter]

print(result)
