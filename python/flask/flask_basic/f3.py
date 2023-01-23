# flask 의 기본형태
#
# 1. 모듈(라이브러리) 가져오기
# from 모듈명 import 클래스, 함수, 변수(상수)
from flask import Flask

# 2. Flask 객체 생성
# 파이썬 변수는 앞에 기호가 없고 타입추론으로 타입결정
# 문장 끝에 세미콜론(;) 없다
# 파이썬은 열을 잘 맞춰야 된다 => 코드블럭({}) 표시가 없다
app = Flask(__name__)
# print(__name__)
# __name__ 의 값은 파이썬 기본구동시 __main__, 모듈로 사용되면 해당파일명

# 3. 라우트
# 클라이언트의 url 요청을 분석하여 어던 함수가 처리될지 매칭하고 요청을 던져줌
@app.route('/')
def home(): # 함수 정의할 때 def 함수명(매개변수):
    return "<h2>hello flask</h2>"

# 4. 서버가동
app.run(debug=True)
# 기본 포트는 127.0.0.1:5000
