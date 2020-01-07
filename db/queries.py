CREAR_CATEGORIAS = "CREATE TABLE categorias (Id int NOT NULL AUTO_INCREMENT, " \
        "nombre varchar(255), " \
        "descripcion varchar(255), " \
        "visitas int, " \
        "imagen varchar(255), PRIMARY KEY (Id));"

CREAR_USUARIOS = "CREATE TABLE usuarios (Id int NOT NULL AUTO_INCREMENT, " \
                 "email varchar(255), " \
                 "password varchar(500), " \
                 "username int, PRIMARY KEY (Id));"

CREAR_LISTAS = "CREATE TABLE listas (Id int NOT NULL AUTO_INCREMENT, " \
               "categoria int, " \
               "nombre varchar(255), " \
               "descripcion varchar(255), " \
               "visitas int, " \
               "imagen varchar(255), PRIMARY KEY (Id));"

