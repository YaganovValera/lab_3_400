"""
Написать программу, которая читая символы из бесконечной последовательности, распознает, преобразует и выводит на
экран лексемы по определенному правилу.Лексемы разделены пробелами.Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения
использовать нельзя.
Вариант 14.
Четные двоичные числа, не превышающие 2048, у которых вторая справа цифра равна 0. Выводит на экран цифры числа,
исключая нули. Вычисляется среднее число между минимальным и максимальным и выводится прописью.
"""


# Функция,которая преобрзует цифры в пропись (словарь)
def replace_digits_with_words(input_string, digit_dict):
    for char in input_string:
        print(digit_dict[char], end='')


BUFFER_len = len(bin(2048)[2:])                                         # размер буфера чтения
DIGIT_DICT = {
    '0': 'ноль ', '1': 'один ', '2': 'два ', '3': 'три ', '4': 'четыре ',
    '5': 'пять ', '6': 'шесть ', '7': 'семь ', '8': 'восемь ', '9': 'девять '
}
BIN_2048 = int(bin(2048)[2:])                                   # 2048 в двоичной системе
max_item = -1                                                   # максимальное число
min_item = float('inf')                                         # минимальное число
current_index = 0                                               # текущий индекс считывания в файле

with open("laba_1.txt", "r") as file:
    while True:
        item_file = file.read(BUFFER_len)                       # считываем 11 символов (длина 2048 в 2-ой системе)
        if not item_file:
            break
        if item_file.isdigit():                                 # проверяем на наличие цифр
            if item_file[0] == '0':                             # пропускаем нули в начале буфера
                current_index += 1
                file.seek(current_index)
                continue
            for index_item in range(3, BUFFER_len+1):
                result = item_file[0:index_item]
                if set(result).intersection({'2', '3', '4', '5', '6', '7', '8', '9'}):  # проверяем нет ли лишних цифр
                    break
                if int(result) <= BIN_2048 and result[-2:] == '00':
                    max_item = max(max_item, int(result))
                    min_item = min(min_item, int(result))
                    # Еслы выводить в 10-ой системе: result = str(int(result, 2))
                    print(result.replace('0', ''), end=' ')
        current_index += 1
        file.seek(current_index)                                 # переходим к следующему блоку

print("")
if max_item == -1:
    print("Ни одно число не подошло")
else:
    mid_item = (int(str(max_item), 2) + int(str(min_item), 2)) / 2
    replace_digits_with_words(str(int(mid_item)), DIGIT_DICT)
