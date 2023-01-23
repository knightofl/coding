from itertools import permutations, combinations


l = [1, 2, 3]
a = permutations(l)
print(list(a))

b = combinations(l, 2)
print(list(b))