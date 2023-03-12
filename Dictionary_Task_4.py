# Создайте словарь с количеством элементов не менее 5-ти. Поменяйте местами первый и последний элемент объекта.
# Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
# Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).

import random
from collections import OrderedDict

init_dict = OrderedDict({random.randint(1, 10): i for i in [random.randint(1, 100) for i in range(6)]})
print(init_dict)

first = list(init_dict.items())[0]
last = list(init_dict.items())[-1]
print(first)
print(last)
init_dict.move_to_end(first[0])
init_dict.move_to_end(last[0], last=False)
print(init_dict)
