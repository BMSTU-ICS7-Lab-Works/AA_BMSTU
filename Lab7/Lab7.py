from random import *
from time import *

def filler(length):
    mas = []
    for i in range(length):
        d = {'key': i,
             'time': generate_time()}
        mas.append(d)
    return mas

def generate_time():
    time = str(randint(0, 23)) + ":" + str(randint(0, 59))
    return time

def brute(mas, key):
    for d in mas:
        if d['key'] == key:
            return d
    return "No such deliveryman"

def binary(mas, key):
    s = 0
    e = len(mas) - 1
    mid = (s + e) // 2
    if mas[s]['key'] > key:
        return "No such deliveryman"

    elif mas[e]['key'] < key:
        return "No such deliveryman"

    if mas[s]['key'] == key:
        return mas[s]
    elif mas[e]['key'] == key:
        return mas[e]
    tmp = mas[mid]['key']
    while key != tmp:
        if key < tmp:
            e = mid
        else:
            s = mid
        mid = (s + e) // 2
        tmp = mas[mid]['key']
    return mas[mid]


def segalg(mas, key, seg_cnt):
    pmas = preproc(seg_cnt)
    
    for d in mas:
        if d['key'] == key:
            return d
    return "No such deliveryman"
    
def preproc(seg_cnt):
    p = 100 / ((1 + seg_cnt) * seg_cnt // 2) / 100

    pmas = []

    for i in range(seg_cnt):
        pmas.append((seg_cnt - i) * p)
    for i in range(1, seg_cnt):
        pmas[i] += pmas[i - 1]

    return pmas

def test():
    mas = filler(5)
    okstr = "No such deliveryman"
    if brute(mas, 5) == okstr and\
    binary(mas, 5) == okstr and\
    segalg(mas, 5, 3) == okstr:
        if brute(mas, -1) == okstr and\
        binary(mas, -1) == okstr and\
        segalg(mas, -1, 3) == okstr:
            if brute(mas, 1) != okstr and\
            binary(mas, 1) != okstr and\
            segalg(mas, 1, 3) != okstr:
                if brute(mas, 0) != okstr and\
                binary(mas, 0) != okstr and\
                segalg(mas, 0, 3) != okstr:
                    print('Brute search: OK')
                    print('Binary search: OK')
                    print('Segment search: OK')

def timeit():
    mas = filler(10000)
    t1 = process_time()
    for i in range(10000):
        a = brute(mas, i)
    t2 = process_time()
    
    print("Bruteforce search time: ",(t2 - t1) / 10000)

    t1 = process_time()
    for i in range(10000):
        a = binary(mas, i)
    t2 = process_time()
    print("Binary search time: ",(t2 - t1) / 10000)

    t1 = process_time()
    for i in range(10000):
        a = segalg(mas, i, 5)
    t2 = process_time()
    print("Segment search time (5 segments): ",(t2 - t1) / 10000)

    t1 = process_time()
    for i in range(10000):
        a = segalg(mas, i, 10)
    t2 = process_time()
    print("Segment search time (10 segments): ",(t2 - t1) / 10000)

    
mas = filler(5)
    
print(brute(mas, 3))
print(segalg(mas, 3, 3))
print(binary(mas, 3))

test()
timeit()
