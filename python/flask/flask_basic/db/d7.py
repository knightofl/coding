# 함수화

import pymysql

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

if __name__ == '__main__':
    lSuccess = sLogin('centum', '1234')
    if lSuccess:
        print('%s님 반갑습니다' % lSuccess['name'])
    else:
        print('아이디나 비밀번호가 틀렸습니다')


