# 문자열
# '', ""
# ''' ''', """ """

a = "hi"
print(a, type(a))

# 문자열 더하기
b = " hello"
print(a + b)

# 인덱싱 => 차원축소
# 변수명[인덱스]
c = "hello world"
print(c[1])
print(c[-1])

# 슬라이싱 => 차원유지
# 변수명[시작인덱스:끝인덱스:스텝(생략되면 1)]
print(c[2:5])
print(c[-5:-1])
print(c[1:-1])

print(c[:5])
print(c[6:])

# 원본복사
print(c[:])

# 포매팅
print("%d + %d = %d" % (1, 2, 1+2))

# 타입을 모를 때의 포매팅
print("%s + %s = %s" % (1, 2, 1+2))

# 명확하게 포매팅 세팅할 때
print("{0} + {1} = {2}".format(1, 2, 1+2))
print("{x} + {y} = {sum}".format(x=1, y=2, sum=1+2))