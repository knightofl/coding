# 집합
# 중복제거. 정렬은 운 좋으면.

a = [1,2,3,4,5,6,7,8,9,4,5,6,7]
print(a)

b = set(a)
print(b, type(b))

a = list(b)
print(a, type(a))

# 합집합, 차집합, 교집합
a = set([1, 2, 4, 5, 6, 7])
b = set([2, 3, 4, 5])

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(b.difference(a))