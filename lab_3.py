import random


# Функция вывода матриц
def print_matrix(matrix):
    for row in matrix:
        print("|", end='')
        for element in row:
            print("{:3}".format(element), end=' ')
        print("|")
    print("")


# Операции над матрицами
def operations_matrix(matrix1, matrix2, sign, len_matrix):
    # Создаем пустую матрицу для результата
    result = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    for row in range(len_matrix):
        for column in range(len_matrix):
            if sign == '+':
                result[row][column] = matrix1[row][column] + matrix2[row][column]
            elif sign == '-':
                result[row][column] = matrix1[row][column] - matrix2[row][column]
            elif sign == '*' and type(matrix2) == int:
                result[row][column] = matrix1[row][column] * matrix2
            else:
                for k in range(len_matrix):
                    result[row][column] += matrix1[row][k] * matrix2[k][column]
    return result


# Транспонирование матрицы
def transpose_matrix(matrix, len_matrix):
    # Создаем новую пустую матрицу для хранения результата
    transposed = [[0 for _ in range(len_matrix)] for _ in range(len_matrix)]
    # Транспонируем матрицу
    for i in range(len_matrix):
        for j in range(len_matrix):
            transposed[j][i] = matrix[i][j]
    return transposed


# Вводим значения K и N с клавиатуры
# K = int(input("Введите размер подматрицы K: "))
# N = int(input("Введите размер матрицы N: "))
K = 2
N = 10

# Создаем пустую матрицу A(N, N)
matrix_A = [[0 for _ in range(N)] for _ in range(N)]
# Определяем размер каждой подматрицы
SIZE_submat = N // 2

# Заполняем матрицу A(N, N) случайными числами
for row in range(N):
    for column in range(N):
        matrix_A[row][column] = random.randint(-10, 10)

# Этап №1. Выводим матрицу A
print("Матрица A(N, N):")
print_matrix(matrix_A)

# Этап №2. Создаем и заполняем подматрицу C
matrix_C = [[0 for _ in range(SIZE_submat)] for _ in range(SIZE_submat)]
for row in range(SIZE_submat):
    matrix_C[row] = matrix_A[N-SIZE_submat + row][N-SIZE_submat:]
print("Матрица С(N, N):")
print_matrix(matrix_C)

# Подсчет отрицательных  элементов в нечетных столбцах в области 4
count_in_area_4 = 0
for row in range(SIZE_submat // 2):
    for column in range(row):
        if ((column+1) % 2 != 0) and matrix_C[row][column] < 0:
            count_in_area_4 += 1
for row in range(SIZE_submat // 2, SIZE_submat):
    for column in range(SIZE_submat - row - 1):
        if ((column+1) % 2 != 0) and matrix_C[row][column] < 0:
            count_in_area_4 += 1

# Подсчет положительных элементов в четных столбцах в области 2
# 0 считаем за положительное число
count_in_area_2 = 0
for row in range(SIZE_submat // 2):
    for column in range(SIZE_submat - row, SIZE_submat):
        if ((column+1) % 2 == 0) and matrix_C[row][column] >= 0:
            count_in_area_2 += 1
for row in range(SIZE_submat // 2, SIZE_submat):
    for column in range(row + 1, SIZE_submat):
        if ((column+1) % 2 == 0) and matrix_C[row][column] >= 0:
            count_in_area_2 += 1

# Выводим результаты подсчета
print("Положительные элементы в области 2:", count_in_area_2)
print("Отрицательные элементы в области 4:", count_in_area_4)


# Создаем и заполняем матрицу F
matrix_F = [[item for item in row] for row in matrix_A]

# если количество чисел во 2 области больше
if count_in_area_2 > count_in_area_4:
    # меняем в С симметрично области 1 и 3 местами
    for row in range(SIZE_submat // 2 - (SIZE_submat % 2 == 0)):
        matrix_C[row][1+row:(SIZE_submat-1)-row], matrix_C[SIZE_submat - 1 - row][1+row:(SIZE_submat-1)-row] = \
            matrix_C[SIZE_submat - 1 - row][1+row:(SIZE_submat-1)-row], matrix_C[row][1+row:(SIZE_submat-1)-row]
    print("Матрица C после замены местами области 1 и 3:")
    print_matrix(matrix_C)
    for row in range(SIZE_submat):
        matrix_F[N - SIZE_submat + row][N - SIZE_submat:] = matrix_C[row]
else:
    # меняем С и E несимметрично
    for row in range(SIZE_submat):
        matrix_F[N - SIZE_submat + row][N - SIZE_submat:], matrix_F[row][0:SIZE_submat] = \
            matrix_F[row][0:SIZE_submat], matrix_F[N - SIZE_submat + row][N - SIZE_submat:]
print("Матрица F после всех изменений: ")
print_matrix(matrix_F)

print("Суммирование матриц (F + A): ")
sum_AF = operations_matrix(matrix_F, matrix_A, '+', N)
print_matrix(sum_AF)

print("Транспонирование матрицы (A^T): ")
trans_A = transpose_matrix(matrix_A, N)
print_matrix(transpose_matrix(matrix_A, N))

print("Произведение матриц (F+A)*A^T: ")
end_result = operations_matrix(sum_AF, trans_A, '*', N)
print_matrix(end_result)

print("Произведение K*F: ")
mult_KF = operations_matrix(matrix_F, K, '*', N)
print_matrix(mult_KF)

print("итоговый результат ((F+A)*A^T – K * F): ")
end_result = operations_matrix(end_result, mult_KF, '-', N)
print_matrix(end_result)
