# 변수명 앞에 아무것도 오지 않는다
# 문장 끝에 세미콜론 없다
# 파이썬의 모든 것은 객체 => 참조(레퍼런스)로 관리
# 열을 맞춰야 된다

a = 1
print(a, type(a))

a = 1.1
print(a, type(a))

# 이미 정해진 내장함수명을 변수명으로 사용하면 오동작
print(str(a), type(str(a)))

str = "hello"
print(str, type(str))
print(str(a), type(str(a)))

# 타입 : 정수, 부동소수, 문자열, 불리언
# 시퀀스 타입 : 문자열, 리스트, 튜플, 딕셔러니, 집합
