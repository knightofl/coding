# 리스트
# 순서 있고, 중복 허용 => 다른 언어의 배열과 비슷
# []

a = []
b = list()

print(a, type(a))
print(b, type(b))

# append 는 마지막 멤버로 추가
a.append("cat")
print(a)
a.append("dog")
print(a)
a.append(3)
print(a)
a.append(b)
a.append(b[:])
print(a)

b.append(2)
print(b)
print(a)

c = [5, 6, 7]
print(a + c)
print(a)
print(a.extend(c))
print(a)

# 인덱싱
print(a[1])

# 슬라이싱
print(a[2:4])

# 삭제
print(len(a))
del a[4]
print(a)

a.remove('cat')
print(a)

del a[:]
print(a, len(a))

# 정렬
a = [7, 1, 5, 4, 9, 2]
print(a)
a.sort()
print(a)