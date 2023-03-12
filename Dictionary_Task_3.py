# Дана строка в виде случайной последовательности чисел от 0 до 9.
#
# Требуется создать словарь, который в качестве ключей будет принимать данные числа (т. е. ключи будут типом int),
# а в качестве значений – количество этих чисел в имеющейся последовательности.
# Для построения словаря создайте функцию count_it(sequence),
# принимающую строку из цифр. Функция должна возвратить словарь из
# 3-х самых часто встречаемых чисел.

num_string = '123432343212432545624321341243235'


def count_int(num_string):
    num_list = list(num_string)
    num_dict = {}
    for i in num_list:
        num_dict[i] = num_dict.setdefault(i, 0) + 1
    print(num_dict)
    new_dict = dict(sorted(num_dict.items(), key=lambda item: item[1], reverse=True))
    result_dict = {}
    count = 0
    for key in new_dict:
        result_dict[key] = new_dict[key]
        count += 1
        if count == 3:
            break
    print(new_dict)
    print(result_dict)


count_int(num_string)
