# coding: utf-8
import numpy as np

def _numerical_gradient_1d(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    for i in range(x.size):
        tmp = x[i]
        x[i] = float(tmp) + h
        fxh1 = f(x)
        
        x[i] = tmp - h 
        fxh2 = f(x)
        grad[i] = (fxh1 - fxh2) / (2*h)
        
        x[i] = tmp
        
    return grad


def numerical_gradient_2d(f, X):
    if X.ndim == 1:
        return _numerical_gradient_1d(f, X)
    else:
        grad = np.zeros_like(X)
        
        for idx, x in enumerate(X):
            grad[idx] = _numerical_gradient_1d(f, x)
        
        return grad


def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    
    it = np.nditer(x, flags=['multi_index'], op_flags=['readwrite'])
    while not it.finished:
        i = it.multi_index
        tmp = x[i]
        x[i] = float(tmp) + h
        fxh1 = f(x)
        
        x[i] = tmp - h 
        fxh2 = f(x)
        grad[i] = (fxh1 - fxh2) / (2*h)
        
        x[i] = tmp
        it.iternext()   
        
    return grad
