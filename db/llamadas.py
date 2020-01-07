import pymysql

def conexion():
    return pymysql.connect(host='localhost',
                           user='root',
                           password='Folcov1963Roccos12',
                           db='top_vote',
                           charset='utf8mb4',
                           cursorclass=pymysql.cursors.DictCursor)



def select(conexion, query):

    with conexion.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `categorias`"
        cursor.execute(sql)
        categorias = cursor.fetchall()
    return categorias

