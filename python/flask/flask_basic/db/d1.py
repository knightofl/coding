# python 에서 데이터베이스 접속 밈 쿼리 처리 등
# 데이터베이스 종류에 따라 모듈들이 달라짐
# mysql 계열은 pymysql 을 사용해보겠다. => raw query 방식
# 고급방식은 sqlAlchemy 를 사용하며 ORM 으로 처리

# python -m pip install PyMySQL

# 1. 모듈 가져오기
# import as 별칭
import pymysql

connection = None

try:
    # 2. 디비접속
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='1234',
                                 db='pythondb',
                                 charset='utf8')
    # 3. 쿼리
    print('쿼리수행')

except Exception as e:
    print(e)
    
finally:
    # 4. 접속해제
    if connection:
        connection.close()
        print('접속해제 완료')




