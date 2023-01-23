# url 추가하기

from flask import Flask

app = Flask(__name__)

@app.route('/') # @ 는 데코레이션 함수
def home():
    return "<h3>hello flask</h3>"

@app.route('/login') # ~/login url 정의
def login():
    return "<h2>login 페이지</h2>"

if __name__ == "__main__":
    app.run(debug=True)

else:
    print("본 모듈은 단독으로 구동될 때 정상작동합니다.")
    print("모듈화 사용불가.")
