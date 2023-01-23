# 코드내에서 url 을 호출할 때 직접 하드코딩하지 않으며
# url 은 라우트에서만 정의하고 나머지 참조는 url_for() 사용
# url_for('특정 url 과 연결된 함수명 기술')

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>flask home</h2>"

@app.route('/login')
def login():
    return "<h2>flask login</h2>"

@app.route('/news/<id>')
def news(id):
    return "<h2>flask news</h2>" + id

# url 요청테스트
# with 문은 I/O 계열에서 주로 사용.
# => 개발자가 close 를 자꾸 까먹어서. with 가 자동으로 닫아줌

with app.test_request_context():
    print('홈페이지 url = ', url_for('home'))
    print('로그인 url = ', url_for('login'))
    print('동적파라미터 뉴스 url = ', url_for('news', id='123'))


if __name__ == "__main__":
    app.run(debug=True)
