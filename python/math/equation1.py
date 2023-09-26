from sympy import Symbol, solve
from sympy import expand, factor
from sympy import Limit, S


x, y, z = Symbol('x'), Symbol('y'), Symbol('z')

eq1 = 2*x + 3*y + 4
eq2 = 3*x + 2*y - 4

print(solve((eq1, eq2)))


eq1 = x + y - 2
eq2 = y + z - 5
eq3 = z - x - 3
print(solve((eq1, eq2, eq3), dict=True))


eq1 = x**2 - y
eq2 = x + y
print(solve((eq1, eq2), dict=True))


print(expand((x + 1) * (x + 5)))
print(expand((x + 2) * (x + 3)))

print(factor(x**2 + 3*x + 2))
print(factor(x**3 * y - x * y**3))


print(Limit(1/x, x, S.Infinity).doit())
print(Limit(1/x, x, 0).doit())
print(Limit(1/x, x, 0, dir='-').doit())
