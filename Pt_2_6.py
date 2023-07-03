distance = int(input("Сколько километров Вы хотите проехать? "))
fuel_consumption = int(input("Сколько литров топлива расходует автомобиль на 100 километров? "))
tank_fullness = int(input("Сколько литров топлива в вашем баке? "))
result = (tank_fullness / fuel_consumption) * 100
if result >= distance:
    print("Вы проедете необходимое расстояние!")
else:
    print("Вам не хватит бензина!")
