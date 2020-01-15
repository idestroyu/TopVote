import pymysql

def conexion():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='Folcov1963Roccos12',
                           db='top_vote',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)



def fetch_all(conexion, query, *args):
    with conexion.cursor() as cursor:
        cursor.execute(query, args)
        return cursor.fetchall()

def modify(conexion, query, *args):
    with conexion.cursor() as cursor:
        cursor.execute(query, args)
    conexion.commit()


