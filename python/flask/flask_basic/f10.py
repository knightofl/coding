# restful 을 이용한 로그인 처리
# html 처리 render_template() => jinja2 엔진
# 현재 py 위치 기준으로 ./templates/login.html 필요

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h2>flask home</h2>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # 아이디, 비번 획득
        # 누락이 있으면 (비정상 접근시) 커트
        # 디비로 가서 쿼리(회원인지 체크)
        # 회원이면 메인서비스, 아니면 돌려보냄
        uid = request.form['uid']
        upw = request.form['upw']

        if uid and upw:
            return "<h1>post %s %s</h1>" % (uid, upw)
        else:
            return render_template('error.html',
            errMsg='아이디와 비번을 모두 입력하세요')

if __name__ == "__main__":
    app.run(debug=True)
