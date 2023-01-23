# 함수화

import pymysql

# 상용 서비스
TEST_DB_HOST = 'localhost'
RELEASE_DB_HOST = 'pythondb2.cythlhij08x7.ap-northeast-2.rds.amazonaws.com'
USE_DB_HOST = RELEASE_DB_HOST

def oilSearch(queryType=1, price=0, keyword='', id=0):
    connection = None
    rows = None

    try:
        connection = pymysql.connect(host=USE_DB_HOST,
                                     user='root',
                                     password='12341234',
                                     db='pythondb',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            if queryType == 1:
                sql = "SELECT * FROM tbl_oil;"
                cursor.execute(sql)
            elif queryType == 2:
                sql = "SELECT * FROM tbl_oil WHERE gas <= %s ORDER BY gas ASC;"
                cursor.execute(sql, (price,))
            elif queryType == 4:
                sql = "SELECT * FROM tbl_oil WHERE id=%s;"
                cursor.execute(sql, (id,))
            else:
                sql = "SELECT * FROM tbl_oil WHERE name like '%{}%' ORDER BY gas ASC;".format(keyword)
                cursor.execute(sql)    

            if queryType == 4:
                rows = cursor.fetchone()
            else:         
                rows = cursor.fetchall()

    except Exception as e:
        print(e)
        rows = None

    finally:
        if connection:
            connection.close()
    return rows

def updateOilstore(id, gas):
    connection = None
    affecctedRow = 0

    try:
        connection = pymysql.connect(host=USE_DB_HOST,
                                     user='root',
                                     password='12341234',
                                     db='pythondb',
                                     charset='utf8',
                                     cursorclass=pymysql.cursors.DictCursor)

        with connection.cursor() as cursor:
            sql = "UPDATE tbl_oil SET gas=%s WHERE id=%s;"
            cursor.execute(sql, (gas, id))

        connection.commit() # 반영

    except Exception as e:
        print(e)

    finally:
        affecctedRow = connection.affected_rows()
        if connection:
            connection.close()

    return  affecctedRow # 영향받은 row 의 수


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
    print(oilSearch())
    print(oilSearch(queryType=2, price=1580))
    print(oilSearch(queryType=3, keyword='은마'))
    print(updateOilstore(1, 1565))
