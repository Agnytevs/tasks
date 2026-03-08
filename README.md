# Олимпиадные задачи

Данный репозиторий содержит решения трех олимпиадных задач, выполненных на языке Python.

# Структура репозитория

- task_one
  - task_one.py
- task_two
  - task_two.py
- task_three
  - task_three.py
- README.md

# Запуск
Все решения принимают данные из стандартного ввода (stdin) и выводят результат в стандартный вывод (stdout).

Пример запуска любой задачи:

```bash
cd task_one
python task_one.py
# далее нужно ввести данные, если это необходимо
```

# Список задач
## Задача 1

### Условие:
> Напишите код, который вычисляет первые 100 чисел Фибоначчи. 
Последовательность Фибоначчи — это последовательность, в которой первые два числа равны 0 и 1, а каждое последующее равно сумме двух предыдущих.

### Алгоритм решения:
...

Сложность: O(1) по времени, O(1) по памяти.

```python
NUMBER_ONE = 0
NUMBER_TWO = 1
print(NUMBER_ONE, NUMBER_TWO)
for i in range(48):
    print(NUMBER_ONE + NUMBER_TWO)
    NUMBER_THREE = NUMBER_ONE + NUMBER_TWO
    NUMBER_ONE = NUMBER_TWO
    print(NUMBER_ONE + NUMBER_THREE)
    NUMBER_TWO = NUMBER_ONE + NUMBER_THREE
    NUMBER_ONE = NUMBER_THREE 
```
## Задача 2

### Условие:
> Напишите код, который вычисляет первые 100 чисел Фибоначчи. 
Последовательность Фибоначчи — это последовательность, в которой первые два числа равны 0 и 1, а каждое последующее равно сумме двух предыдущих.

### Алгоритм решения:
...

Сложность: O(1) по времени, O(1) по памяти.

```python
NUMBER_ONE = 0
NUMBER_TWO = 1
print(NUMBER_ONE, NUMBER_TWO)
for i in range(48):
    print(NUMBER_ONE + NUMBER_TWO)
    NUMBER_THREE = NUMBER_ONE + NUMBER_TWO
    NUMBER_ONE = NUMBER_TWO
    print(NUMBER_ONE + NUMBER_THREE)
    NUMBER_TWO = NUMBER_ONE + NUMBER_THREE
    NUMBER_ONE = NUMBER_THREE 
```
