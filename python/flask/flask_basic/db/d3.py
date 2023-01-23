# select 쿼리 결과가 딕셔너리 구조로 와야된다
# 컬럼의 순서가 변경되어도 컬럼명으로 데이터를 획득할 수 있도록

import pymysql

connection = None

try:
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='pythondb',
                                 charset='utf8')
    # 쿼리
    with connection.cursor(pymysql.cursors.DictCursor) as cursor: # 커서를 딕셔너리로
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




