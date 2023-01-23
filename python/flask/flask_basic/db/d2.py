import pymysql

connection = None

try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='pythondb',
                                 charset='utf8')
    # 쿼리
    with connection.cursor() as cursor: # cursor = connection.cursor()
        # wirh 문은 i/O 계열에서 자동으로 닫기처리
        # 쿼리 수행을 위해서는 커서를 획득해야 된다.
        sql = "select * from tbl_users where uid='centum' and upw='1234';"
        cursor.execute(sql)
        # 결과 패치
        row = cursor.fetchone()
        print('%s님 반갑습니다.' %(row[3]))
    # cursor.close()    

except Exception as e:
    print(e)
finally:
    if connection:
        connection.close()
        print('접속해제 완료')




