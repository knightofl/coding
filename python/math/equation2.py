from sympy import Derivative, symbols 


x = symbols('x')
fx = 2*x**2 + 4*x + 7

def average(a, b):
    m = max(a, b)
    n = min(a, b)

    fb = fx.subs(x, m)
    fa = fx.subs(x, n)

    return (fb - fa) / (b - a)


print(average(0, 2))


fprime = Derivative(fx, x).doit()
print(fprime)

a = 3
n = fprime.subs({x: a})
print(f'fx에서 x={a}에서의 미분계수는 {n} 입니다')


fx = 2*x**2 - 1
fprime = Derivative(fx, x).doit()
print(fprime)

a = 6
n = fprime.subs(x, 6)
print(f'fx에서 x={a}에서의 미분계수는 {n} 입니다')

