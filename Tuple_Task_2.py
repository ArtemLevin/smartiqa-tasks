# Функция slicer() на вход принимает кортеж и случайный элемент. Требуется вернуть новый кортеж, начинающийся
# с первого появления элемента в нем и заканчивающийся вторым его появлением включительно.
# Если элемента нет вовсе – вернуть пустой кортеж.
# Если элемент встречается только один раз, то вернуть кортеж,
# который начинается с него и идет до конца исходного.

def slicer(my_tuple, element: int):
    if element not in my_tuple:
        return ()
    elif my_tuple.count(element) == 1:
        return my_tuple
    else:
        index = my_tuple.index(element)
        return tuple(list(my_tuple)[index:(my_tuple.index(element, index + 1) + 1)])


print(slicer([10, 2, 3, 4, 10, 6, 7], 1))

