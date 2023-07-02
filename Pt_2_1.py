import random
list_of_colors = ("Red", "Yellow", "Green", "Blue", "White")
print("Цвета на выбор: ", *list_of_colors)
random_color_of_list = random.choice(list_of_colors)
persons_way = input("Введите цвет: ")
# while random_color_of_list != persons_way:
#     print("Повторите попытку")
#     persons_way = input("Введите цвет: ")
# print("Отлично!")
while True:
    if persons_way == random_color_of_list:
        print("Правильно!")
        break
    elif random_color_of_list == "Red":
        print("Подсказка: цвет клубники.")
        persons_way = input("Введите цвет: ")
    elif random_color_of_list == "Yellow":
        print("Подсказка: цвет лимона.")
        persons_way = input("Введите цвет: ")
    elif random_color_of_list == "Green":
        print("Подсказка: пришельцы - ... человечки.")
        persons_way = input("Введите цвет: ")
    elif random_color_of_list == "Blue":
        print("Подсказка: лагуна.")
        persons_way = input("Введите цвет: ")
    elif random_color_of_list == "White":
        print("Подсказка: полярный ... медведь.")
        persons_way = input("Введите цвет: ")
    else:
        break
