from flask import Flask, redirect, url_for, render_template, request
from flask_cms.db.d8 import sLogin

# 세션은 서버메모리 저장 (파일럿 수준), 서버쪽 디비에 저장,
# 제3의 서드파트 모듈사용등을 고려
# 여기서는 서버 메모리 저장방식

app = Flask(__name__)

# 세션키를 지정. 향후는 해쉬값을 활용하여 세팅.
app.secret_key = 'lkfjdslfjewlew3l2k4nedr23nr32rl32lk'


@app.route('/')
def home():
    # 세션체크, 없으면 로그인으로
    return render_template('index.html', title='SB Admin v2.0')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        uid = request.form['uid']
        upw = request.form['upw']

        if uid and upw:
            row = sLogin(uid, upw)

            if row:
                #return render_template('error.html', errMsg='%s님 반갑습니다' % row['name'])
                return redirect(url_for('home'))
            else:
                return render_template('error.html',
                       errMsg='아이디나 비밀번호가 틀렸습니다')

        else:
            return render_template('error.html',
                   errMsg='아이디와 비번을 모두 입력하세요')


@app.route('/logout')
def logout():
    # 세션제거
    return redirect( url_for('home') )


if __name__ == '__main__':
    app.run(host='0.0.0.0')