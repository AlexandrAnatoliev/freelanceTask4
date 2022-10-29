# freelanceTask4

# Описание
#
# Написание лабораторных работ
# Необходимо написать 2 лабораторные работы
# 1. Реализовать сложение, умножение, транспонирование и умножение на число матриц (ВАЖНО: без использования numpy)
# 2. Реализовать решение системы линейных уравнений (СЛАУ)

# Функция для создания квадратной матрицы:
# 1 0 1
# 0 1 1 => [[1,0,1],[0,1,1],[1,1,1]]
# 1 1 1

def square_matrix_create():
    string1 = list(map(float, input().split()))  # считываем первую строку матрицы
    matrix_size = len(string1)  # вычисляем размер матрицы
    matrix = []
    matrix.append(string1)
    # Создаем матрицу
    for i in range(matrix_size - 1):
        string1 = list(map(float, input().split()))
        matrix.append(string1)
    return matrix


# Функция для создания матрицы произвольного размера

def matrix_create(matrix_hight):
    matrix = []
    # Создаем матрицу
    for i in range(matrix_hight):
        string1 = list(map(float, input().split()))
        matrix.append(string1)
    return matrix


# Функция для сложения двух матриц

def matrix1_plus_matrix2(matrix1, matrix2):
    matrix3 = []
    for i, row in enumerate(matrix1):
        r = []
        for j, x in enumerate(row):
            r.append(x + matrix2[i][j])
        matrix3.append(r)
    return matrix3


# Функция для вычитания двух матриц

def matrix1_minus_matrix2(matrix1, matrix2):
    matrix3 = []
    for i, row in enumerate(matrix1):
        r = []
        for j, x in enumerate(row):
            r.append(x - matrix2[i][j])
        matrix3.append(r)
    return matrix3


# Функция для транспонирования матрицы (поменять значения столбцов и строк местами) - работает только для квадр матрицы

def square_matrix_transpose(matrix):
    matrix_transpose = []
    for i in range(len(matrix)):
        row = matrix[i][:]  # Можно создать копию списка,но не копию вложенного списка!
        matrix_transpose.append(row)
    for i in range(len(matrix_transpose)):
        for j in range(i + 1, len(matrix_transpose)):
            matrix_transpose[i][j], matrix_transpose[j][i] = matrix_transpose[j][i], matrix_transpose[i][j]
    return matrix_transpose


# Функция для транспонирования матрицы
def matrix_transpose(matrix):
    matrix_transpose = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        matrix_transpose.append(row)
    return matrix_transpose

matrix_hight1 = int(input("Введите количество строк в первой матрице: "))
print("""Введите первую матрицу в формате:
    1 2 3
    4 5 6
    ...
    """)
matrix1 = matrix_create(matrix_hight1)

matrix_hight2 = int(input("Введите количество строк во второй матрице: "))
print("Введите вторую матрицу:")
matrix2 = matrix_create(matrix_hight2)

matrix3 = matrix1_plus_matrix2(matrix1, matrix2)
matrix4 = matrix1_minus_matrix2(matrix1, matrix2)
matrix1_tr = matrix_transpose(matrix1)
matrix2_tr = matrix_transpose(matrix2)

print("Первая матрица: ", matrix1)
print("Вторая матрица", matrix2)
print("Сумма матриц: ", matrix3)
print("Разность матриц", matrix4)
print("Транспонированная первая матрица", matrix1_tr)
print("Транспонированная вторая матрица", matrix2_tr)
