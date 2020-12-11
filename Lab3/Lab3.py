import numpy as np
import random
from time import process_time

def get_time():
    print("Количество итераций: 100000")
    print("Длина массива: 5")
    print("Наполнение: случайные числа")
    n = 5
    arrs = []
    for i in range(100000):
        arrs.append(rand_mas(n))
    start_t = process_time()
    for j in range(100000):
        bubble_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка пузырьком = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(rand_mas(n))
    start_t = process_time()
    for j in range(100000):
        insertion_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка вставками = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(rand_mas(n))
    start_t = process_time()
    for j in range(100000):
        select_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка выбором = ", end_t)
    arrs.clear()

    print("Количество итераций: 100000")
    print("Длина массива: 10")
    print("Наполнение: случайные числа")

    n = 10
    arrs = []
    for i in range(100000):
        arrs.append(rand_mas(n))
    start_t = process_time()
    for j in range(100000):
        bubble_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка пузырьком = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(rand_mas(n))
    start_t = process_time()
    for j in range(100000):
        insertion_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка вставками = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(rand_mas(n))
    start_t = process_time()
    for j in range(100000):
        select_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка выбором = ", end_t)
    arrs.clear()

    
    print("Количество итераций: 100000")
    print("Длина массива: 5")
    print("Наполнение: отсортированные числа")

    n = 5
    arrs = []
    for i in range(100000):
        arrs.append(sorted_mas(n))
    start_t = process_time()
    for j in range(100000):
        bubble_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка пузырьком = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(sorted_mas(n))
    start_t = process_time()
    for j in range(100000):
        insertion_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка вставками = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(sorted_mas(n))
    start_t = process_time()
    for j in range(100000):
        select_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка выбором = ", end_t)
    arrs.clear()
    
    print("Количество итераций: 100000")
    print("Длина массива: 10")
    print("Наполнение: отсортированные числа")

    n = 10
    arrs = []
    for i in range(100000):
        arrs.append(sorted_mas(n))
    start_t = process_time()
    for j in range(100000):
        bubble_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка пузырьком = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(sorted_mas(n))
    start_t = process_time()
    for j in range(100000):
        insertion_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка вставками = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(sorted_mas(n))
    start_t = process_time()
    for j in range(100000):
        select_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка выбором = ", end_t)
    arrs.clear()

    print("Количество итераций: 100000")
    print("Длина массива: 5")
    print("Наполнение: отсортированные в обратном порядке числа")

    n = 5
    arrs = []
    for i in range(100000):
        arrs.append(sorted_back_mas(n))
    start_t = process_time()
    for j in range(100000):
        bubble_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка пузырьком = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(sorted_back_mas(n))
    start_t = process_time()
    for j in range(100000):
        insertion_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка вставками = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(sorted_back_mas(n))
    start_t = process_time()
    for j in range(100000):
        select_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка выбором = ", end_t)
    arrs.clear()

    print("Количество итераций: 100000")
    print("Длина массива: 10")
    print("Наполнение: отсортированные в обратном порядке числа")

    n = 10
    arrs = []
    for i in range(100000):
        arrs.append(sorted_back_mas(n))
    start_t = process_time()
    for j in range(100000):
        bubble_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка пузырьком = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(sorted_back_mas(n))
    start_t = process_time()
    for j in range(100000):
        insertion_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка вставками = ", end_t)
    arrs.clear()

    arrs = []
    for i in range(100000):
        arrs.append(sorted_back_mas(n))
    start_t = process_time()
    for j in range(100000):
        select_sort(arrs[j], n)
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("Сортировка выбором = ", end_t)
    arrs.clear()

def tests():
    arr = []
    n = 5
    arr = sorted_mas(n)
    resarr = arr[:]
    print("Изначально отсортированный массив")
    print_arr(arr)
    
    print("Результат сортировки пузырьком")
    print_arr(bubble_sort(arr, n))
    arr = resarr[:]
    
    print("Результат сортировки вставками")
    print_arr(insertion_sort(arr, n))
    arr = resarr[:]
    
    print("Результат сортировки выбором")
    print_arr(select_sort(arr, n))

    arr = sorted_back_mas(n)
    resarr = arr[:]
    print("Изначально отсортированный в обратном порядке массив")
    print_arr(arr)
    
    print("Результат сортировки пузырьком")
    print_arr(bubble_sort(arr, n))
    arr = resarr[:]

    print("Результат сортировки вставками")
    print_arr(insertion_sort(arr, n))
    arr = resarr[:]
    
    print("Результат сортировки выбором")
    print_arr(select_sort(arr, n))

    arr = rand_mas(n)
    resarr = arr[:]
    print("Массив, содержащий отрицательные числа")
    print_arr(arr)
    
    print("Результат сортировки пузырьком")
    print_arr(bubble_sort(arr, n))
    arr = resarr[:]

    print("Результат сортировки вставками")
    print_arr(insertion_sort(arr, n))
    arr = resarr[:]
    
    print("Результат сортировки выбором")
    print_arr(select_sort(arr, n))

    arr = rand_mas(n)
    arr[1] = arr[4]
    arr[2] = arr[3]
    resarr = arr[:]
    print("Массив, содержащий одинаковые элементы")
    print_arr(arr)
    
    print("Результат сортировки пузырьком")
    print_arr(bubble_sort(arr, n))
    arr = resarr[:]

    print("Результат сортировки вставками")
    print_arr(insertion_sort(arr, n))
    arr = resarr[:]
    
    print("Результат сортировки выбором")
    print_arr(select_sort(arr, n))
    arr = resarr[:]
    

def bubble_sort(arr, n):
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1
    return arr


def insertion_sort(arr, n):
    i = 1
    while i < n:
        key = arr[i]
        j = i - 1
        while j >=0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        i += 1
    return arr


def select_sort(arr, n):
    i = n
    while i > 1:
        maximum = 0
        j = 0
        while j < i:
            if arr[j] > arr[maximum]:
                maximum = j
            j += 1
        arr[i-1], arr[maximum] = arr[maximum], arr[i-1]
        i -= 1
    return arr

def rand_mas(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(-1000, 1000))
    return arr

def sorted_mas(n):
    arr = []
    randn = random.randint(-1000, 1000)
    for i in range(randn, randn + n):
        arr.append(i)
    return arr


def sorted_back_mas(n):
    arr = []
    randn = random.randint(-1000, 1000)
    for i in range(randn + n, randn, -1):
        arr.append(i)
    return arr


def print_arr(arr):
    print(str(arr))

def menu():
    print("Menu:")
    print("1. Сортировка случайного массива с заданным размером (пузырёк)")
    print("2. Сортировка случайного массива с заданным размером (вставками)")
    print("3. Сортировка случайного массива с заданным размером (выбором)")
    print("4. Посчитать время")
    print("5. Тесты")
    print("0. exit")

if __name__ == '__main__':

    while (1):
        arr = []
        menu()
        choice = int(input("Make your choice: "))
        if choice == 1:
            n = int(input("Введите размер массива: "))
            arr = rand_mas(n)
            print("Unsorted arr")
            print_arr(arr)
            arr = bubble_sort(arr, n)
            print("Sorted arr")
            print_arr(arr)
        elif choice == 2:
            n = int(input("Введите размер массива: "))
            arr = rand_mas(n)
            print("Unsorted arr")
            print_arr(arr)
            arr = insertion_sort(arr, n)
            print("Sorted arr")
            print_arr(arr)
        elif choice == 3:
            n = int(input("Введите размер массива: "))
            arr = rand_mas(n)
            print("Unsorted arr")
            print_arr(arr)
            arr = select_sort(arr, n)
            print("Sorted arr")
            print_arr(arr)
        elif choice == 4:
            get_time()
        elif choice == 5:
            tests()
        elif choice == 0:
            print("Finishing...")
            break
        else:
            print("Incorrect input!")



