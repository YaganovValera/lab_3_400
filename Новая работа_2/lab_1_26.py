"""
Написать программу, которая читая символы из бесконечной последовательности, распознает, преобразует и выводит на
экран лексемы по определенному правилу.Лексемы разделены пробелами.Преобразование делать по возможности через словарь.
Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа. Регулярные выражения
использовать нельзя.
Вариант 26.
Шеснадцатиричные четные числа, не превышающие 2048 и содержащие более К цифр.
Вывести числа и их количество. Максимальное число вывести прописью.
"""


# Функция,которая преобрзует цифры в пропись (словарь)
def replace_digits_with_words(input_string, digit_dict):
    for char in input_string:
        print(digit_dict[char], end='')


DIGIT_DICT = {
    '0': 'ноль ', '1': 'один ', '2': 'два ', '3': 'три ', '4': 'четыре ',
    '5': 'пять ', '6': 'шесть ', '7': 'семь ', '8': 'восемь ', '9': 'девять '
}
k = int(input("Введите число:"))                                              # ручное ограничение на размер
BUFFER_len = len(hex(2048)[2:])                                               # размер буфера чтения
max_item = -1                                                   # максимальное число
count_num = 0                                                   # количество чисел
current_index = 0                                               # текущий индекс считывания в файле
with open("laba_1.txt", "r") as file:
    while True:
        item_file = file.read(BUFFER_len)                       # считываем буфер(длина 2048 в 16-ой системе)
        if not item_file:
            break
        if item_file[0] == '0':                                 # пропускаем нули в начале буфера
            current_index += 1
            file.seek(current_index)
            continue
        for index_item in range(max(1, k+1), BUFFER_len+1):
            result = item_file[0:index_item]
            try:
                result_ten = int(result, 16)
                if (result_ten < 2048) and (result_ten % 2 == 0):
                    max_item = max(max_item, result_ten)
                    count_num += 1
                    print(result + " - " + str(result_ten), end='; ')
            except Exception:
                continue

        current_index += 1
        file.seek(current_index)                                 # переходим к следующему блоку

print("")
if count_num == 0:
    print("Ни одно число не подошло")
else:
    print("Кол-во чисел: ", count_num)
    replace_digits_with_words(str(max_item), DIGIT_DICT)

