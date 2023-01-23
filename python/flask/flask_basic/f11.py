from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

def sLogin(uid, upw):
    connection = None
    row = None

    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='1234',
                                    db='pythondb',
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "SELECT * FROM tbl_users WHERE uid=%s AND upw=%s;"
            cursor.execute(sql, (uid, upw))
            row = cursor.fetchone()

    except Exception as e:
        print(e)
        row = None # 향후 확장을 위해 None 으로 초기화
    finally:
        if connection:
            connection.close()
    return row


@app.route('/')
def home():
    return "<h2>flask home</h2>"

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
                return ('%s님 반갑습니다' % row['name'])
            else:
                return ('아이디나 비밀번호가 틀렸습니다')

        else:
            return render_template('error.html',
            errMsg='아이디와 비번을 모두 입력하세요')

if __name__ == "__main__":
    app.run(debug=True)
