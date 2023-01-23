# 튜플 - 순서가 있고, 변경 불가
# ()
# 구성원이 1개면 (구성원,)

a = (1)
b = (1,)
print(type(a), type(b))

c = (5, 6, 3)

# 인덱싱
print(c[1])

# 슬라이싱
print(c[:2])

# 여러개의 값을 리턴
x, y, z = c
print(x, y, z)