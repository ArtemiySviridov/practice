tv_show = ["News", "Hockey", "One Piece", "Film"]
for show in tv_show:
    print(show)
print()
enter_new_show = input("Введите название телепередачи: ")
enter_position = int(input("После какого элемента вставить: "))
tv_show.insert(enter_position, enter_new_show)
for show in tv_show:
    print(show)
