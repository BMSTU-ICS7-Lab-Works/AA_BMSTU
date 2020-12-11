import numpy as np
import random, string
from time import process_time


def levenshtein(a, b):
    n, m = len(a), len(b)
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            insert, delete, replace = previous_row[j] + 1,\
                                      current_row[j - 1] + 1,\
                                      previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                replace += 1
            current_row[j] = min(insert, delete, replace)

    return current_row[n]


def damerau_levenshtein(matr, a, b):
    n = len(a) + 1
    m = len(b) + 1
    for i in range(1, m):
        for j in range(1, n):
            if a[j - 1] != b[i - 1]:
                replace = 1
            else:
                replace = 0
            matr[i][j] = min(
                matr[i - 1][j] + 1,
                matr[i][j - 1] + 1,
                matr[i - 1][j - 1] + replace
                )
            if i and j and a[j - 1] == b[i - 2] and a[j - 2] == b[i - 1]:
                matr[i][j] = min(matr[i][j], matr[i - 2][j - 2] + replace)

    return matr[m - 1][n - 1]



def recursion_levenshtein(a, b):
    if not a:
        return len(b)
    if not b:
        return len(a)
    return min(recursion_levenshtein(a[1:], b[1:]) + (a[0] != b[0]),
               recursion_levenshtein(a[1:], b) + 1,
               recursion_levenshtein(a, b[1:]) + 1)


def recursion_levenshtein_opt(a, b, j, i, matr):
    if i == 0:
        return j
    if j == 0:
        return i
    if a[j - 1] == b[i - 1]:
        replace = 0
    else:
        replace = 1
    
    if matr[i][j] == -1:
        matr[i][j] = min(recursion_levenshtein_opt(a, b, j - 1, i - 1, matr) + replace,
                         recursion_levenshtein_opt(a, b, j - 1, i, matr) + 1,
                         recursion_levenshtein_opt(a, b, j, i - 1, matr) + 1)
    return matr[i][j]


def create_matrix(a, b):
    matrix = np.full((b, a), -1)
    for i in range(b):
        matrix[i][0] = i
    for j in range(a):
        matrix[0][j] = j
    return matrix

def get_memory():
    print("Memories are")
    m2 = np.array([])
    print("Empty mas", m2.__sizeof__())
    m2 = np.append(m2, 1)
    print("memory of mas", m2, m2.__sizeof__())
    m2 = np.append(m2, 2)
    m2 = np.append(m2, 2)
    m2 = np.append(m2, 2)
    m2 = np.append(m2, 2)
    print("memory of mas", m2, m2.__sizeof__())
    print("int size ", int(100).__sizeof__())
    print("Empty str ", str("").__sizeof__())
    print("str mem ", str("chich"), str("chich").__sizeof__())
    m3 = np.full((5, 5), 0)
    print("memory of mas", m3, m3.__sizeof__())
    m4 = np.array([[],[]])
    print("memory of mas [[][]]", m4.__sizeof__())
    m5 = np.array([[]])
    print("memory of mas [[]]", m5.__sizeof__())

def generate_string(l):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(l))


def get_time():
    print("Calculating..")
    print("Number of iterations are 10000")
    
    str_mas1 = []
    str_mas2 = []
    #len 5 10k iters
    print("words len is 5")
    for k in range(10000):
        str_mas1.append(generate_string(5))
        str_mas2.append(generate_string(5))
    matr = []
    for l in range(10000):
        matr.append(create_matrix(len(str_mas1[l]) + 1, len(str_mas2[l]) + 1))

    start_t = process_time()
    for j in range(10000):
        damerau_levenshtein(matr[j], str_mas1[j], str_mas2[j])
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("dam-lev = ", end_t)
    matr.clear()

    start_t = process_time()
    for j in range(10000):
        levenshtein(str_mas1[j], str_mas2[j])
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("lev = ", end_t)

    str_mas1.clear()
    str_mas2.clear()
    
    #len 10 10k iters
    print("Number of iterations are 10000")
    print("words len is 10")
    for k in range(10000):
        str_mas1.append(generate_string(10))
        str_mas2.append(generate_string(10))
    matr = []
    for l in range(10000):
        matr.append(create_matrix(len(str_mas1[l]) + 1, len(str_mas2[l]) + 1))

    start_t = process_time()
    for j in range(10000):
        damerau_levenshtein(matr[j], str_mas1[j], str_mas2[j])
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("dam-lev = ", end_t)
    matr.clear()

    start_t = process_time()
    for j in range(10000):
        levenshtein(str_mas1[j], str_mas2[j])
    end_t = process_time()
    end_t -= start_t
    end_t /= 10000
    print("lev = ", end_t)

    str_mas1.clear()
    str_mas2.clear()
    print("Number of iterations are 15")
    print("words len is 5")
    for k in range(15):
        str_mas1.append(generate_string(5))
        str_mas2.append(generate_string(5))

    matr = []
    for l in range(15):
        matr.append(create_matrix(len(str_mas1[l]) + 1, len(str_mas2[l]) + 1))

    start_t = process_time()
    for j in range(15):
        recursion_levenshtein_opt(str_mas1[j], str_mas2[j], len(str_mas1[j]), len(str_mas2[j]), matr[j])
    end_t = process_time()
    end_t -= start_t
    end_t /= 15
    print("rec_matr = ", end_t)
    matr.clear()

    start_t = process_time()
    for j in range(15):
        recursion_levenshtein(str_mas1[j], str_mas2[j])
    end_t = process_time()
    end_t -= start_t
    end_t /= 15
    print("rec = ", end_t)

    str_mas1.clear()
    str_mas2.clear()
    print("Number of iterations are 15")
    print("words len is 10")
    for k in range(15):
        str_mas1.append(generate_string(10))
        str_mas2.append(generate_string(10))

    matr = []
    for l in range(15):
        matr.append(create_matrix(len(str_mas1[l]) + 1, len(str_mas2[l]) + 1))

    start_t = process_time()
    for j in range(15):
        recursion_levenshtein_opt(str_mas1[j], str_mas2[j], len(str_mas1[j]), len(str_mas2[j]), matr[j])
    end_t = process_time()
    end_t -= start_t
    end_t /= 15
    print("rec_matr = ", end_t)
    matr.clear()

    start_t = process_time()
    for j in range(15):
        recursion_levenshtein(str_mas1[j], str_mas2[j])
    end_t = process_time()
    end_t -= start_t
    end_t /= 15
    print("rec = ", end_t)

    str_mas1.clear()
    str_mas2.clear()
    print('we end it bois')

def menu():
    print("Menu:")
    print("1. Classic Levenshtein")
    print("2. Levenshtein recursion")
    print("3. Levenshtein recursion with matrix")
    print("4. Damerau-Levenshtein")
    print("5. Calculate time")
    print("6. Tests")
    print("0. exit")

def tests():
    s1, s2 = "", ""
    print('S1 = ""', 'S2 = ""')
    print("Левенштейн D = ", levenshtein(s1, s2))
    print("Левенштейн рек. D = ", recursion_levenshtein(s1, s2))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Левенштейн рек. с доп. проверками D = ",
          recursion_levenshtein_opt(s1, s2, len(s1), len(s2), m))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Дамерау-Левенштейн D = ", damerau_levenshtein(m, s1, s2))

    s1, s2 = "telo", "telo"
    print('S1 = telo', 'S2 = telo')
    print("Левенштейн D = ", levenshtein(s1, s2))
    print("Левенштейн рек. D = ", recursion_levenshtein(s1, s2))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Левенштейн рек. с доп. проверками D = ",
          recursion_levenshtein_opt(s1, s2, len(s1), len(s2), m))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Дамерау-Левенштейн D = ", damerau_levenshtein(m, s1, s2))
    
    s1, s2 = "telo", "tlo"
    print('S1 = ', s1, 'S2 = ', s2)
    print("Левенштейн D = ", levenshtein(s1, s2))
    print("Левенштейн рек. D = ", recursion_levenshtein(s1, s2))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Левенштейн рек. с доп. проверками D = ",
          recursion_levenshtein_opt(s1, s2, len(s1), len(s2), m))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Дамерау-Левенштейн D = ", damerau_levenshtein(m, s1, s2))

    s1, s2 = "telo", "talo"
    print('S1 = ', s1, 'S2 = ', s2)
    print("Левенштейн D = ", levenshtein(s1, s2))
    print("Левенштейн рек. D = ", recursion_levenshtein(s1, s2))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Левенштейн рек. с доп. проверками D = ",
          recursion_levenshtein_opt(s1, s2, len(s1), len(s2), m))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Дамерау-Левенштейн D = ", damerau_levenshtein(m, s1, s2))

    s1, s2 = "blank", ""
    print('S1 = ', s1, 'S2 = ', s2)
    print("Левенштейн D = ", levenshtein(s1, s2))
    print("Левенштейн рек. D = ", recursion_levenshtein(s1, s2))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Левенштейн рек. с доп. проверками D = ",
          recursion_levenshtein_opt(s1, s2, len(s1), len(s2), m))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Дамерау-Левенштейн D = ", damerau_levenshtein(m, s1, s2))

    s1, s2 = "telo", "tleo"
    print('S1 = ', s1, 'S2 = ', s2)
    print("Левенштейн D = ", levenshtein(s1, s2))
    print("Левенштейн рек. D = ", recursion_levenshtein(s1, s2))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Левенштейн рек. с доп. проверками D = ",
          recursion_levenshtein_opt(s1, s2, len(s1), len(s2), m))
    m = create_matrix(len(s1) + 1, len(s2) + 1)
    print("Дамерау-Левенштейн D = ", damerau_levenshtein(m, s1, s2))
    
if __name__ == '__main__':
    while (1):
        menu()
        choice = int(input("Make your choice: "))
        if choice == 1:
            print("Enter s1 and s2 with a space between")
            s1, s2 = str(input()).split()
            print("D is ", levenshtein(s1, s2))
        elif choice == 2:
            print("Enter s1 and s2 with a space between")
            s1, s2 = str(input()).split()
            print("D is ", recursion_levenshtein(s1, s2))
        elif choice == 3:
            print("Enter s1 and s2 with a space between")
            s1, s2 = str(input()).split()
            m = create_matrix(len(s1) + 1, len(s2) + 1)
            print("D is ", recursion_levenshtein_opt(s1, s2,
                                                     len(s1), len(s2), m))
        elif choice == 4:
            print("Enter s1 and s2 with a space between")
            s1, s2 = str(input()).split()
            m = create_matrix(len(s1) + 1, len(s2) + 1)
            print("D is ", damerau_levenshtein(m, s1, s2))
        elif choice == 5:
            get_time()
        elif choice == 6:
            tests()
        elif choice == 0:
            print("Finishing...")
            break
        else:
            print("Incorrect input!")

    

