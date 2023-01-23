# 딕셔너리 : 키와 값의 세트, 키는 중복될 수 없음
# {}

a = {}
b = dict()
print(a, type(a))
print(b, type(b))

a['lan'] = 'python'
print(a, len(a))

# 인덱싱
c = {'red':1, 'blue':2, 'green':3}
print(c['red'])

# 슬라이싱 안됨

# 삭제
del c['blue']
print(c, len(c))

c['orange'] = 9
print(c.items())
print(c.keys())
print(c.values())

print('*' * 20)

# 반복문 for
# for in
for i in c:
    print(i)

for i in c.keys():
    print(i)

for i in c.values():
    print(i)

for i in c.items():
    print(i)

for key in c:
    print("key=%s, value=%s" % (key, c[key]))

for item in c.items():
    print(type(item), len(item), item[0], item[1])

# 굳이 인덱스 쓰고 싶다면
for e in enumerate(c):
    print(e)

for e in enumerate(c.values()):
    print(e)

for index, value in enumerate(c.values()):
    print(index, value)      