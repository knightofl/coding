# sql 문의 파라미터를 외부로

import pymysql

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
        # sql 표현에서 파라미터 전달시 '' 유무 주의
        # 파라미터는 tuple 로 전달
        row = cursor.fetchone()
        print('%s님 반갑습니다.' %(row['name']))  

except Exception as e:
    print(e)
    
finally:
    if connection:
        connection.close()
        print('접속해제 완료')




