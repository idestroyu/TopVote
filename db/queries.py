CREAR_CATEGORIAS = "CREATE TABLE categorias (Id int NOT NULL AUTO_INCREMENT, " \
        "nombre varchar(255), " \
        "descripcion varchar(255), " \
        "visitas int, " \
        "imagen varchar(255), PRIMARY KEY (Id));"

CREAR_USUARIOS = "CREATE TABLE usuarios (Id int NOT NULL AUTO_INCREMENT, " \
                 "email varchar(255), " \
                 "password varchar(500), " \
                 "salt varchar(500), " \
                 "username varchar(50), PRIMARY KEY (Id));"

CREAR_LISTAS = "CREATE TABLE listas (Id int NOT NULL AUTO_INCREMENT, " \
               "categoria int, " \
               "nombre varchar(255), " \
               "descripcion varchar(255), " \
               "visitas int, " \
               "imagen varchar(255), PRIMARY KEY (Id));"

INSERTAR_USUARIO = "INSERT INTO usuarios (email, password, salt, username) VALUES (%s, %s, %s, %s);"

INSERTAR_LISTA = "INSERT INTO listas (categoria, nombre, descripcion, visitas, imagen) VALUES (%s, %s, %s, 0, %s);"

ENCONTRAR_USUARIO = "INSERT INTO usuarios (email, password, salt, username) VALUES (%s, %s, %s, %s);"

ENCONTRAR_LISTA = "INSERT INTO usuarios (email, password, salt, username) VALUES (%s, %s, %s, %s);"
