"""Решение третьей задачи."""
def prepare_data(bushes:int, bush:int) -> int and list:
    """Подготавливает данные для работы алгоритма."""
    # если куст всего один, то добавляем один "призрачный" для правильной работы кода
    if bushes == 1:
        bush.append(0)
        bushes = len(bush)
    return bushes, bush


def calculate_max_harvest(bushes:int, bush:int) -> int:
    """Вычисляет максимальный урожай с использованием динамического программирования."""
    # подготавливаем данные
    bushes, bush = prepare_data(bushes, bush)

    # инициализируем dp
    dp = [0] * max(bushes, 2)

    # база для ДП
    # среди кустов (0, 0] берем единственный вариант
    dp[0] = bush[0]

    # среди кустов (0, 1] берем лучший вариант
    if bushes > 1:
        dp[1] = max(bush[0], bush[1])

    # проходимся по всем кустам, начиная с 3
    for i in range(2, bushes):
        # либо мы не берем текущий куст, либо берем его и лучший результат на i-2
        dp[i] = max(dp[i - 1], dp[i - 2] + bush[i])

    # dp[bushes - 1] - ответ на задачу
    return dp[bushes - 1]


def main() -> None:
    """Главная функция программы."""
    bushes = int(input())
    bush = [int(i) for i in input().split()]

    # вычисляем и выводим результат
    result = calculate_max_harvest(bushes, bush)
    print(result)


# Запуск программы
if __name__ == "__main__":
    main()

