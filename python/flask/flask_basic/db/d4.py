import pymysql

connection = None

try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='pythondb',
                                 charset='utf8',
                                 cursorclass=pymysql.cursors.DictCursor)
                                 # 이후 열리는 모든 커서의 타입은 DictCursor
                                 # 쿼리 결과문은 항상 딕셔너리

    with connection.cursor() as cursor:
        sql = "select * from tbl_users where uid='centum' and upw='1234';"
        cursor.execute(sql)
        row = cursor.fetchone()
        print('%s님 반갑습니다.' %(row['name']))  

except Exception as e:
    print(e)
    
finally:
    if connection:
        connection.close()
        print('접속해제 완료')




