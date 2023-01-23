from flask import Flask, request, render_template, redirect, url_for, jsonify
from db.d8 import sLogin, oilSearch, updateOilstore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', oils=oilSearch())

@app.route('/search', methods=['POST'])
def search():
    kw = request.form['keyword']
    if kw.isnumeric():
        # 검색어 획득 : request.form['keyword]
        # 쿼리수행 : oilSearch(3, keyword=)
        # 결과를 json 으로 반환 : jsonify()
        return jsonify(oilSearch(queryType=2, price=int(kw)))
        # API 만 지원하는 url 이고 이것으로만 구성된 서버는 미들웨어
        # 네이티브앱과 통신하는 모바일 서버가 이런 스타일
    else:
        return jsonify(oilSearch(queryType=3, keyword=kw))

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

@app.route('/info/<int:id>', methods=['GET', 'POST'])
def info(id):
    if request.method =='GET':
        # 파라미터 u 획득.
        # post 방식은 form, get 방식은 args
        isUpdate = True if request.args.get('u') else False # 3항 연산자

        return render_template('info.html', oilStore=oilSearch(queryType=4, id=id), isUpdate=isUpdate)

    else:
        # 실제 수정처리
        # 파리미터 획득
        gas = request.form.get('gas')
        # 값체크 처리는 생략
        # 디비 쿼리 (update) 수행 -> 리턴 값은 영향을 받은 row 의 수
        if updateOilstore(id, gas):
            # 수행결과를 받아서 성공하면 (영향을 받은 row 의 수가 1개 이상)
            # 성공하면 -> 수정되었습니다. -> 메인페이지
            return render_template('error.html', errMsg='수정성공', dst=url_for('home'))

        else:
            # 실패하면 -> 수정실패 -> 해당 주유소 미리보기
            return render_template('error.html', errMsg='수정실패', dst=url_for('info', id=id))


if __name__ == "__main__":
    app.run(debug=True)
