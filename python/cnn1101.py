import numpy as np
import matplotlib.pyplot as plt


def step(x):
    #return (x>1).astype(np.int)
    return np.array(x>0, dtype=np.int)

def AND(x):
    w = np.array([0.5, 0.5])
    b = -0.7
    #return step(np.sum(w * x) + b)
    return step(np.dot(w, x) + b)

def OR(x):
    w = np.array([0.5, 0.5])
    b = -0.2
    return step(np.dot(w, x) + b)

def NAND(x):
    w = np.array([-0.5, -0.5])
    b = 0.7
    return step(np.dot(w, x) + b)
    #return step(not AND(x))

def XOR(x):
    return AND([NAND(x), OR(x)])


test = np.array(((1,1), (1,0), (0,1), (0,0)))
print(test)

for i in test:
    print(f'AND{i} {AND(i)}')

for i in test:
    print(f'OR{i} {OR(i)}')

for i in test:
    print(f'NAND{i} {NAND(i)}')

for i in test:
    print(f'XOR{i} {XOR(i)}')

