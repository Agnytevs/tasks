"""Этот код решает первую задачу."""
number_one, number_two = 0, 1
for _ in range(100):
    print(number_one + number_two)
    number_one, number_two = number_two, number_one + number_two
