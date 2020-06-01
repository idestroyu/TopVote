import db.queries as q
import db.llamadas as call
import os

def init_db():
    os.remove("topvote.db")
    conexion = call.conexion()

    call.modify(conexion, q.CREAR_CATEGORIAS)
    call.modify(conexion, q.CREAR_USUARIOS)
    call.modify(conexion, q.CREAR_LISTAS)
    call.modify(conexion, q.CREAR_ELEMENTOS)
    call.modify(conexion, q.CREAR_VOTOS)
    call.modify(conexion, q.CREAR_ALERTAS)

def init_categorias():
    conexion = call.conexion()

    call.modify(conexion, q.INSERTAR_CATEGORIA, "Tecnologia",
                "Aqui encontraras listas de temas tecnologicos o de informatica", "https://d32r1sh890xpii.cloudfront.net/article/718x300/93728e7f7f7483493cc49df735861759.jpg")

    call.modify(conexion, q.INSERTAR_CATEGORIA, "Cine",
                "Comparte tu pasion por el cine en estas listas de peliculas", "https://cdn.vox-cdn.com/thumbor/ybRf9TwAH2J7VeSRxemzJAvNhMw=/0x0:6720x4480/1200x800/filters:focal(2717x1620:3791x2694)/cdn.vox-cdn.com/uploads/chorus_image/image/60141553/shutterstock_1068876371.0.jpg")

    call.modify(conexion, q.INSERTAR_CATEGORIA, "Naturaleza",
                "Las mejores listas sobre la naturaleza", "https://i.ytimg.com/vi/BHACKCNDMW8/maxresdefault.jpg")

    call.modify(conexion, q.INSERTAR_CATEGORIA, "Politica",
                "Encuentra las mejores listas sobre la actualidad o historia politica", "https://static.fanpage.it/wp-content/uploads/2019/06/POLITICA-SFONDI-AREE.jpg")


init_db()
init_categorias()