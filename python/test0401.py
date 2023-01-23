tu1 = ('a1','b1','c1')
tu2 = ('a2','b2','c2')

tu3 = tu1 + tu2
print(tu3)
print(tu3[4])
print(tu3[3:7])

tu4 = tu3 * 3
print(tu4)
print(tu4.count('a1'))
print(tu4.index('b2'))

tu5 = tu4 + ([1,2,3],['a','b','c'])
print(tu5)

tu5[-2][0] = 5
tu5[-1][1] = 'd'
print(tu5)

