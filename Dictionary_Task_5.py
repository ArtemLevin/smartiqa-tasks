import collections
import random

dict_1 = collections.OrderedDict({random.randint(1, 5): _ for _ in [random.randint(1, 10) for _ in range(1, 5)]})
dict_2 = collections.OrderedDict({random.randint(1, 5): _ for _ in [random.randint(1, 10) for _ in range(1, 5)]})
dict_3 = collections.OrderedDict({random.randint(1, 5): _ for _ in [random.randint(1, 10) for _ in range(1, 5)]})
print(dict_1, "\n", dict_2, "\n", dict_3)
new_dict = {}
d = collections.ChainMap(dict_1, dict_2, dict_3)
for _ in range(0, 3):
    for key in d.maps[_]:
        if key not in new_dict or d.maps[_][key] > new_dict[key]:
            new_dict[key] = d.maps[_][key]
print(new_dict)