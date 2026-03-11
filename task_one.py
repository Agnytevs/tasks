"""Решение первой задачки."""
def print_fibonacci(numbers:int) -> None:
    """Функция выводит числа фибоначчи до указанного числа."""
    # создаем переменные первых чисел фибоначчи
    number_one, number_two = 0, 1
    # выводим первые два числа
    print(number_one)
    print(number_two)
    # создаем цикл, который выведет все числа фибоначчи
    for _ in range(1, numbers + 1):
        # создаем переменную для следующего
        fib_num = number_one + number_two
        # выводим следующее число фибоначчи
        print(fib_num)
        # меняем переменные для следующего числа
        number_one, number_two = number_two, fib_num


def main() -> None:
    """Основная функция программы."""
    print_fibonacci(100)


# Запуск программы
if __name__ == "__main__":
    main()



