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


matrix_hight1 = int(input("Введите количество строк в первой матрице: "))
print("""Введите первую матрицу в формате:
    1 2 3
    4 5 6
    7 8 9
    """)
matrix1 = matrix_create(matrix_hight1)

matrix_hight2 = int(input("Введите количество строк во второй матрице: "))
print("Введите вторую матрицу:")
matrix2 = matrix_create(matrix_hight2)

print(matrix1)
print(matrix2)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
