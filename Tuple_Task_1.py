# Напишите функцию tpl_sort(), которая сортирует кортеж, состоящий из целых чисел по возрастанию и возвращает его.
# Если хотя бы один элемент не является целым числом, то функция возвращает исходный кортеж.

def tpl_sort():
    tuple_ = (5, 3, 1.0, 15, 2, 1)
    for el in tuple_:
        if el is float:
            return tuple_
    return tuple(sorted(list(tuple_)))


print(tpl_sort())
