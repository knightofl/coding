from sympy import Symbol, diff, expand


x = Symbol('x')
fx  = 2*x**3 + 3*x**2 + x + 1

fprime = diff(fx, x)
print(fprime)


fx1 = 2*x + 1
fx2 = 3*x**2 + 2*x
fx = fx1 * fx2
fprime = diff(fx, x)
print(fprime)

fprime = diff(fx1, x) * fx2 + fx1 * diff(fx2, x)
print(fprime)
print(expand(fprime))


fx1 = 2*x**2 + 3*x
fx2 = x**2 + 1
fx = fx1 / fx2
fprime = diff(fx, x)
print(fprime)

fprime = (diff(fx1, x) * fx2 - fx1 * diff(fx2, x)) / (fx2)**2
print(fprime)
