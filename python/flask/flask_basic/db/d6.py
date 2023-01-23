# 함수화

import pymysql

def sLogin():
    connection = None

    try:
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='1234',
                                    db='pythondb',
                                    charset='utf8',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "select * from tbl_users where uid=%s and upw=%s;"
            cursor.execute(sql, ('centum', '1234'))
            row = cursor.fetchone()
            print('%s님 반갑습니다.' %(row['name']))  

    except Exception as e:
        print(e)
        
    finally:
        if connection:
            connection.close()
            print('접속해제 완료')


sLogin()


