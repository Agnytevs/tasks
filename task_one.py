# Создаем первые две переменные и выводим их
number_one = 0
number_two = 1
print(number_one)
print(number_two)
# Создаем цикл For, для вывода оставшихся 98 чисел
for i in range(49):
    # Выполняем вывод суммы чисел
    print(number_one + number_two)
    # Обновляем переменные
    number_three = number_one + number_two
    number_one = number_two
    #Выполняем вывод новой суммы чисел
    print(number_one + number_three)
    # Опять обновляем переменные
    number_two = number_one + number_three
    number_one = number_three