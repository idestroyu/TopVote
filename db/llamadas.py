import sqlite3
import os


def conexion():
    localizacion = os.path.dirname(os.path.realpath(__file__))

    conn = sqlite3.connect(localizacion + '/topvote.db')

    # Para que nos devuelva lista de diccionarios
    conn.row_factory = sqlite3.Row

    return conn
def fetch_all(conexion, query, *args):
    cursor = conexion.cursor()
    cursor.execute(query, args)
    return cursor.fetchall()

def modify(conexion, query, *args):
    cursor = conexion.cursor()
    cursor.execute(query, args)
    id = cursor.lastrowid
    conexion.commit()
    return id