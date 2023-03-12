# Дана строка в виде случайной последовательности чисел от 0 до 9.
#
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence),
# принимающую строку из цифр. Функция должна возвратить словарь из
# 3-х самых часто встречаемых чисел.

num_string = '123432343212432545624321341243235'


def count_int(num_string):
    new_dict = {int(item): num_string.count(item) for item in num_string}
    print(new_dict)
    new_list = sorted(new_dict.items(), key=lambda el: el[1], reverse=True)
    print(new_list)
    return dict(new_list[:3])


print(count_int(num_string))
