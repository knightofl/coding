import numpy as np


def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    return np.dot(x, w) + b > 0
        

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2

    return np.dot(x, w) + b > 0


def NAND(x1, x2):
    return not AND(x1, x2)


def XOR(x1, x2):
    return AND(NAND(x1, x2), OR(x1,x2))


test =((1,1), (1,0), (0,1), (0,0))

for i in test:
    print(f'AND{i} {AND(i[0], i[1])}')

for i in test:
    print(f'OR{i} {OR(i[0], i[1])}')

for i in test:
    print(f'NAND{i} {NAND(i[0], i[1])}')

for i in test:
    print(f'XOR{i} {XOR(i[0], i[1])}')

