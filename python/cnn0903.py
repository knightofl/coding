import numpy as np


# 다중선형회귀는 해석미분으로
def analytic_gradient(weight, t_data):
    a0, a1, b = weight
    x0, x1, y = t_data
    dx = np.zeros_like(weight)
    n = len(x0)
    
    loss = a0*x0 + a1*x1 + b - y
    dx[0] = (2/n) * np.sum(loss * x0) 
    dx[1] = (2/n) * np.sum(loss * x1)
    dx[2] = (2/n) * np.sum(loss)

    return dx


t = np.array([2,4,6,8])
p = np.array([0,4,2,3])
s = np.array([81,93,91,97])

weight = np.array([0.,0.,0.])
lr = 0.01
step = 30000

for i in range(step):
    gradient = analytic_gradient(weight, t_data=(t,p,s))
    print(f'step={i+1}, gradient={gradient}, weight={weight}')
    weight -= lr * gradient
