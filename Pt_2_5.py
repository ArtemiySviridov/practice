import random
wins = 0
losses = 0
losses_at_all = 0

while losses_at_all < 3:
    user_choice = input("Выберите орла (0) или решку (1): ")

    if user_choice == '0' or user_choice == '1':
        computer_choice = random.randint(0, 1)

        if int(user_choice) == computer_choice:
            print("Вы выиграли!")
            wins += 1
            losses_at_all = 0
        else:
            print("Вы проиграли!")
            losses += 1
            losses_at_all += 1
    else:
        print("Игра завершена.")
        break

print("Игра завершена.")
print("Количество выигрышей:", wins)
print("Количество проигрышей:", losses)
