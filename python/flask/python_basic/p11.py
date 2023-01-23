# 모듈화, 패키지

# 패키지는 폴더. 내부에는 하위버전 호환을 위해 __init__.py 파일을 생성
# p11.py 에서 p11 이 모듈명.
# 모듈명에 도트(.) 가 포함되면 안된다. 패키지로 인식되므로

# from 패키지명.패키지명...(모듈명) import 변수, 함수, 클래스, 모듈명...
# import 패키지명(모듈명) 함수, 변수, 클래스 등 하위로 내려갈 수 있고 as 별칭 사용도 가능


# 패키지를 지정하면 __init.py 가 대응된다
from a import PI1
print(PI1)

# 패키지.모듈로 타고 가면 해당모듈의 변수, 함수, 클래스 참조가능
from a.a_sub import PI2
print(PI2)

# b 패키지를 지정하면 __init.py 가 대응된다
from a.b import PI3
print(PI3)

# 패키지.모듈로 타고 가면 해당모듈의 변수, 함수, 클래스 참조가능
from a.b.b_sub import PI4
print(PI4)


import a.b.b_sub as m1
print(m1.PI4)

import a.b as m2
print(m2.PI3)