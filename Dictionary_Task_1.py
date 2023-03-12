import random

my_list = [random.randint(1, 100) for _ in range(10)]


def list_to_dict(my_list):
    my_dict = {}
    for i in my_list:
        my_dict[i] = i
    print(my_list, '\n', my_dict)


list_to_dict(my_list)


def l_2_d(my_list):
    return {element: element for element in my_list}


print(l_2_d(my_list))
