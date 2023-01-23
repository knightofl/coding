# 동적 파라미터 (url 주소에 데이터를 실어서 보냄)
# http 프로토콜 헤더를 타고 전달. 보안에 취약.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>hello flask</h2>"

# 연결된 파라미터명을 함수의 인자로 전달해야 내부에서 사용가능
# 동적 파라미터는 <동작 파라미터명>
@app.route('/userinfo/<news_id>')
def userinfo(news_id):
    return "<h1>news_id = " + news_id + "</h1>"

# 동적 파라미터에 타입제한 int, float, path 가능
@app.route('/add/<int:x>/<int:y>')
def add(x, y):
    return "<h1>%d + %d = %d</h1>" % (x, y, x+y)

# path 형은 동적 파라미터 n 개를 자유롭게 보냄
@app.route('/free/<path:arg>')
def free(arg):
    print(arg.split('/'))
    return "<h1>" + arg + "</h1>"

if __name__ == "__main__":
    app.run(debug=True)
