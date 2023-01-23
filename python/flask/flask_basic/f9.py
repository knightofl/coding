# get, post 방식
# restful 처리
# ~/login : get 방식으로는 로그인 폼 구성 (html)
# ~/login : get 방식으로는 로그인 처리 구성

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>flask home</h2>"

# 기본 라우트를 기술하면 get 방식 의미
# 기본 get 방식 외에 post 도 사용되게 처리
# 메소드 방식은 http 의 헤더에 설정되어 요청됨
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return "<h1>get</h1>"
    else:
        return "<h1>post</h1>"

if __name__ == "__main__":
    app.run(debug=True)
