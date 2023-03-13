# Перед студентом стоит задача: на вход функции sieve() поступает список целых чисел.
# В результате выполнения этой функции будет получен кортеж уникальных элементов списка в обратном порядке.
from random import random, randint

numbers = [randint(1, 5) for _ in range(15)]
print(numbers)


def sieve(list_):
    return tuple(sorted(list(set(list_)), reverse=True))


print(sieve(numbers))
