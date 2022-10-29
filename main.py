# freelanceTask4

# Описание
#
# Написание лабораторных работ
# Необходимо написать 2 лабораторные работы
# 1. Реализовать сложение, умножение, транспонирование и умножение на число матриц (ВАЖНО: без использования numpy)
# 2. Реализовать решение системы линейных уравнений (СЛАУ)

print("""Введите первую матрицу в формате:
    1 2 3
    4 5 6
    7 8 9
    """)

# Создание квадратной матрицы:
# 1 0 1
# 0 1 1 => [[1,0,1],[0,1,1],[1,1,1]]
# 1 1 1


string1 = list(map(float, input().split()))  # считываем первую строку матрицы
matrix_size = len(string1)  # вычисляем размер матрицы
matrix1 = []
matrix1.append(string1)
# Создаем матрицу
for i in range(matrix_size - 1):
    string1 = list(map(float, input().split()))
    matrix1.append(string1)

print(string1)
print(matrix1)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
