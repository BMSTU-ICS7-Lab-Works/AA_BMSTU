import numpy as np
import random
from time import process_time

def get_time():
    print("Количество итераций: 10000")
    matrs1 = []
    matrs2 = []
    resmatrs = []
    print("Размер матрицы: 4x4")
    for k in range(10000):
        matr1 = rand_matr(4, 4)
        matr2 = rand_matr(4, 4)
        resmatr = np.zeros((4, 4))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        classic_mult(resmatrs[j], matrs1[j], matrs2[j], 4, 4, 4)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Классическое умножение = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    for k in range(10000):
        matr1 = rand_matr(4, 4)
        matr2 = rand_matr(4, 4)
        resmatr = np.zeros((4, 4))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        Vinograd_mult(resmatrs[j], matrs1[j], matrs2[j], 4, 4, 4)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Алгоритм Винограда = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    for k in range(10000):
        matr1 = rand_matr(4, 4)
        matr2 = rand_matr(4, 4)
        resmatr = np.zeros((4, 4))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        Vinograd_opt(resmatrs[j], matrs1[j], matrs2[j], 4, 4, 4)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Улучшенный алгоритм Винограда = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    print("Количество итераций: 10000")
    print("Размер матрицы: 5x5")
    for k in range(10000):
        matr1 = rand_matr(5, 5)
        matr2 = rand_matr(5, 5)
        resmatr = np.zeros((5, 5))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        classic_mult(resmatrs[j], matrs1[j], matrs2[j], 5, 5, 5)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Классическое умножение = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    for k in range(10000):
        matr1 = rand_matr(5, 5)
        matr2 = rand_matr(5, 5)
        resmatr = np.zeros((5, 5))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        Vinograd_mult(resmatrs[j], matrs1[j], matrs2[j], 5, 5, 5)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Алгоритм Винограда = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    for k in range(10000):
        matr1 = rand_matr(5, 5)
        matr2 = rand_matr(5, 5)
        resmatr = np.zeros((5, 5))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        Vinograd_opt(resmatrs[j], matrs1[j], matrs2[j], 5, 5, 5)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Улучшенный алгоритм Винограда = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    print("Количество итераций: 10000")
    print("Размер матрицы: 8x8")
    for k in range(10000):
        matr1 = rand_matr(8, 8)
        matr2 = rand_matr(8, 8)
        resmatr = np.zeros((8, 8))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        classic_mult(resmatrs[j], matrs1[j], matrs2[j], 8, 8, 8)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Классическое умножение = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    for k in range(10000):
        matr1 = rand_matr(8, 8)
        matr2 = rand_matr(8, 8)
        resmatr = np.zeros((8, 8))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        Vinograd_mult(resmatrs[j], matrs1[j], matrs2[j], 8, 8, 8)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Алгоритм Винограда = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    for k in range(10000):
        matr1 = rand_matr(8, 8)
        matr2 = rand_matr(8, 8)
        resmatr = np.zeros((8, 8))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        Vinograd_opt(resmatrs[j], matrs1[j], matrs2[j], 8, 8, 8)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Улучшенный алгоритм Винограда = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    print("Количество итераций: 10000")
    print("Размер матрицы: 9x9")
    for k in range(10000):
        matr1 = rand_matr(9, 9)
        matr2 = rand_matr(9, 9)
        resmatr = np.zeros((9, 9))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        classic_mult(resmatrs[j], matrs1[j], matrs2[j], 9, 9, 9)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Классическое умножение = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    for k in range(10000):
        matr1 = rand_matr(9, 9)
        matr2 = rand_matr(9, 9)
        resmatr = np.zeros((9, 9))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        Vinograd_mult(resmatrs[j], matrs1[j], matrs2[j], 9, 9, 9)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Алгоритм Винограда = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

    for k in range(10000):
        matr1 = rand_matr(9, 9)
        matr2 = rand_matr(9, 9)
        resmatr = np.zeros((9, 9))
        matrs1.append(matr1)
        matrs2.append(matr2)
        resmatrs.append(resmatr)

    start_t = process_time()
    for j in range(10000):
        Vinograd_opt(resmatrs[j], matrs1[j], matrs2[j], 9, 9, 9)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Улучшенный алгоритм Винограда = ", end_t)
    matrs1.clear()
    matrs2.clear()
    resmatrs.clear()

def tests():
    m1 = np.zeros((3, 3))
    m2 = rand_matr(3, 3)
    print("Матрица A")
    print_matr(m1, 3, 3)
    print("Матрица B")
    print_matr(m2, 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (классический алгоритм)")
    print_matr(classic_mult(resm, m1, m2, 3, 3, 3), 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (алгоритм Винограда)")
    print_matr(Vinograd_mult(resm, m1, m2, 3, 3, 3), 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (улучшенный алгоритм Винограда)")
    print_matr(Vinograd_opt(resm, m1, m2, 3, 3, 3), 3, 3)
    ###
    m1 = np.eye(3)
    m2 = rand_matr(3, 3)
    print("Матрица A")
    print_matr(m1, 3, 3)
    print("Матрица B")
    print_matr(m2, 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (классический алгоритм)")
    print_matr(classic_mult(resm, m1, m2, 3, 3, 3), 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (алгоритм Винограда)")
    print_matr(Vinograd_mult(resm, m1, m2, 3, 3, 3), 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (улучшенный алгоритм Винограда)")
    print_matr(Vinograd_opt(resm, m1, m2, 3, 3, 3), 3, 3)
    ###
    m1 = rand_matr(3, 3)
    m2 = rand_matr(3, 1)
    print("Матрица A")
    print_matr(m1, 3, 3)
    print("Матрица B")
    print_matr(m2, 3, 1)
    resm = np.zeros((3, 1))
    print("Результат AXB (классический алгоритм)")
    print_matr(classic_mult(resm, m1, m2, 3, 3, 1), 3, 1)
    resm = np.zeros((3, 1))
    print("Результат AXB (алгоритм Винограда)")
    print_matr(Vinograd_mult(resm, m1, m2, 3, 3, 1), 3, 1)
    resm = np.zeros((3, 1))
    print("Результат AXB (улучшенный алгоритм Винограда)")
    print_matr(Vinograd_opt(resm, m1, m2, 3, 3, 1), 3, 1)
    ###
    m1 = rand_matr(3, 3)
    m2 = rand_matr(3, 3)
    print("Матрица A")
    print_matr(m1, 3, 3)
    print("Матрица B")
    print_matr(m2, 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (классический алгоритм)")
    print_matr(classic_mult(resm, m1, m2, 3, 3, 3), 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (алгоритм Винограда)")
    print_matr(Vinograd_mult(resm, m1, m2, 3, 3, 3), 3, 3)
    resm = np.zeros((3, 3))
    print("Результат AXB (улучшенный алгоритм Винограда)")
    print_matr(Vinograd_opt(resm, m1, m2, 3, 3, 3), 3, 3)

def Vinograd_mult(resmatr, matr1, matr2, n, m, k):
    mulh = [0] * n
    mulv = [0] * k

    i = 0
    while i < n:
        j = 0
        while j < m//2:
              mulh[i] = mulh[i] + matr1[i][j * 2] * matr1[i][j * 2 + 1]
              j += 1
        i += 1

    i = 0
    while i < k:
        j = 0
        while j < m//2:
            mulv[i] = mulv[i] + matr2[j * 2][i] * matr2[j * 2 + 1][i]
            j += 1
        i += 1

    i = 0
    while i < n:
        j = 0
        while j < k:
            resmatr[i][j] = -mulh[i] - mulv[j]
            l = 0
            while l < m // 2:
                resmatr[i][j] = resmatr[i][j] + \
                                (matr1[i][2 * l + 1] + matr2[2 * l][j]) * (matr1[i][2 * l] + matr2[2 * l + 1][j])
                l += 1
            j += 1
        i += 1

    if m % 2 == 1:
        i = 0
        while i < n:
            j = 0
            while j < k:
                resmatr[i][j] = resmatr[i][j] + matr1[i][m - 1] * matr2[m - 1][j]
                j += 1
            i += 1
    return resmatr

def Vinograd_opt(resmatr, matr1, matr2, n, m, k):
    mulh = [0] * n
    mulv = [0] * k

    mminmod2 = m - m % 2
    i = 0
    while i < n:
        j = 0
        while j < mminmod2:
            mulh[i] += matr1[i][j] * matr1[i][j + 1]
            j += 2
        i += 1

    i = 0
    while i < k:
        j = 0
        while j < mminmod2:
            mulv[i] += matr2[j][i] * matr2[j + 1][i]
            j += 2
        i += 1

    i = 0
    while i < n:
        j = 0
        while j < k:
            buf = -mulh[i] - mulv[j]
            l = 0
            while l < mminmod2:
                buf += (matr1[i][l + 1] + matr2[l][j]) * (matr1[i][l] + matr2[l + 1][j])
                l += 2
            resmatr[i][j] = buf
            j += 1
        i += 1

    if m % 2 == 1:
        i = 0
        mminus = m - 1
        while i < n:
            j = 0
            while j < k:
                resmatr[i][j] += matr1[i][mminus] * matr2[mminus][j]
                j += 1
            i += 1
    return resmatr


def classic_mult(resmatr, matr1, matr2, n, m, k):
    i = 0
    while i < n:
        j = 0
        while j < k:
            l = 0
            while l < m:
                resmatr[i][j] += matr1[i][l] * matr2[l][j]
                l += 1
            j += 1
        i += 1
    return resmatr


def size_inp():
    print("Матрица A [NXM]")
    print("Матрица B [MXK]")
    n, m, k = map(int, input("Введите n, m, k: ").split(' '))
    return n, m, k

def rand_matr(n, m):
    matr = np.zeros((n, m))
    for i in range(n):
        for j in range(m):
            matr[i][j] = random.randint(-5, 5)
    return matr

def print_matr(matr, n, m):
    for i in range(n):
        for j in range(m):
            print(int(matr[i][j]), end=' ')
        print("")

def menu():
    print("Menu:")
    print("1. Перемножение случайных матриц с заданным размером (классическое)")
    print("2. Перемножение случайных матриц с заданным размером (Винограда)")
    print("3. Перемножение случайных матриц с заданным размером (улучшенного Винограда)")
    print("4. Посчитать время")
    print("5. Тесты")
    print("0. exit")

if __name__ == '__main__':

    while (1):
        matr1 = []
        matr2 = []
        menu()
        choice = int(input("Make your choice: "))
        if choice == 1:
            n, m, k = size_inp()
            matr1 = rand_matr(n, m)
            matr2 = rand_matr(m, k)
            print("First matr")
            print_matr(matr1, n, m)
            print("Second matr")
            print_matr(matr2, m, k)
            print("Result matr")
            resmatr = np.zeros((n, k))
            print_matr(classic_mult(resmatr, matr1, matr2, n, m, k), n, k)
        elif choice == 2:
            n, m, k = size_inp()
            matr1 = rand_matr(n, m)
            matr2 = rand_matr(m, k)
            print("First matr")
            print_matr(matr1, n, m)
            print("Second matr")
            print_matr(matr2, m, k)
            print("Result matr")
            resmatr = np.zeros((n, k))
            print_matr(Vinograd_mult(resmatr, matr1, matr2, n, m, k), n, k)
        elif choice == 3:
            n, m, k = size_inp()
            matr1 = rand_matr(n, m)
            matr2 = rand_matr(m, k)
            print("First matr")
            print_matr(matr1, n, m)
            print("Second matr")
            print_matr(matr2, m, k)
            print("Result matr")
            resmatr = np.zeros((n, k))
            print_matr(Vinograd_opt(resmatr, matr1, matr2, n, m, k), n, k)
        elif choice == 4:
            get_time()
        elif choice == 5:
            tests()
        elif choice == 0:
            print("Finishing...")
            break
        else:
            print("Incorrect input!")



