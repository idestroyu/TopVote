
""" CREAR TABLAS """
CREAR_CATEGORIAS = "CREATE TABLE categorias (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
        "nombre varchar(255), " \
        "descripcion varchar(255), " \
        "visitas int, " \
        "imagen varchar(255));"

CREAR_USUARIOS = "CREATE TABLE usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
                 "email varchar(255), " \
                 "password varchar(500), " \
                 "salt varchar(500), " \
                 "username varchar(50) UNIQUE);"

CREAR_LISTAS = "CREATE TABLE listas (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
               "categoria int, " \
               "nombre varchar(255), " \
               "descripcion varchar(255), " \
               "visitas int, " \
               "imagen varchar(255));"

CREAR_ELEMENTOS = "CREATE TABLE elementos (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
               "lista int, " \
               "votos int, " \
               "nombre varchar(255), " \
               "descripcion varchar(255));" \

CREAR_VOTOS = "CREATE TABLE votos (user_id INTEGER NOT NULL, " \
               "list_id int, " \
               "element_id int, " \
               "PRIMARY KEY (user_id, list_id));" \


""" BORRAR TABLAS """
BORRAR_CATEGORIAS = "DROP TABLE IF EXISTS categorias"

BORRAR_USUARIOS = "DROP TABLE IF EXISTS usuarios"

BORRAR_LISTAS = "DROP TABLE IF EXISTS listas"

BORRAR_ELEMENTOS = "DROP TABLE IF EXISTS elementos"


""" INSERTAR EN TABLAS """
INSERTAR_USUARIO = "INSERT INTO usuarios (email, password, username) VALUES (?, ?, ?);"

INSERTAR_LISTA = "INSERT INTO listas (categoria, nombre, descripcion, visitas, imagen) VALUES (?, ?, ?, 0, ?);"

INSERTAR_CATEGORIA = "INSERT INTO categorias (nombre, descripcion, visitas, imagen) VALUES (?, ?, 0, ?);"

INSERTAR_ELEMENTO = "INSERT INTO elementos (lista, votos, nombre, descripcion) VALUES (?, 1, ?, ?);"

UPDATE_VISITAS_LISTA = "UPDATE listas SET visitas = visitas + 1 WHERE id=?;"

UPDATE_VOTOS_ELEMENTO = "UPDATE elementos SET votos = votos + 1 WHERE id=?; " \
                        "INSERT INTO votos (user_id, lista_id, element_id) VALUES (?, ?, ?);"

SEARCH_LIST = "SELECT * FROM listas WHERE LOWER(nombre) LIKE ?;"
