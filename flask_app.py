from flask import Flask, request
from flask import render_template, redirect, session, jsonify

import db.llamadas as calls
from db.queries import INSERTAR_USUARIO, INSERTAR_LISTA, INSERTAR_ELEMENTO, UPDATE_VISITAS_LISTA, \
    SEARCH_LIST, INSERTAR_VOTO, BORRAR_VOTO, UPDATE_VOTOS_ELEMENTO_RESTAR, UPDATE_VOTOS_ELEMENTO_SUMAR
from users.registro import hash_password, verify_password

app = Flask(__name__, template_folder='templates')

# Para que nos deje utilizar sesiones de usuario
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

def coger_categorias():
    conexion = calls.conexion()
    return calls.fetch_all(conexion, "SELECT * FROM `categorias`")

def render(template, **kwargs):
    return render_template(template, categorias=coger_categorias(), session=session, **kwargs)

@app.route('/')
def index():
    top_listas = calls.fetch_all(calls.conexion(), "SELECT * "
                                                   "FROM listas ORDER BY listas.visitas DESC LIMIT 4")
    return render('index.html', top_listas=top_listas)

@app.route('/create-list')
def create_list_page():
    return render('crear_lista.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'loggedin' in session:
            return redirect("/")
        else:
            return render('login.html')
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conexion = calls.conexion()

        resultados = calls.fetch_all(conexion, "SELECT * FROM usuarios WHERE username=?", username)
        if resultados and verify_password(password, resultados[0]["password"]):
            session['loggedin'] = True
            session['username'] = username
            return jsonify(message="Inicio de sesion correcto"), 200
        return jsonify(message="El usuario no pudo ser verificado"), 400

@app.route('/register', methods = ['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render('register.html')
    elif request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        hashed_password = hash_password(password)

        conexion = calls.conexion()

        # Rechazar registro si usuario o email ya existe en la base de datos
        usuario_existente = calls.fetch_all(conexion, "SELECT * FROM usuarios WHERE email=? or username=?", email, username)
        if len(usuario_existente) > 0:
            return jsonify(message="Ya existe un usuario con ese email o nombre de usuario"), 400

        # Agregar usuario a la base de datos
        calls.modify(conexion, INSERTAR_USUARIO, email, hashed_password, username)

        # Recordar en la sesion
        session['loggedin'] = True
        session['username'] = username
        return redirect('/')

@app.route('/profile', methods = ['GET'])
def profile():

    # Listar categoria con el id pedido
    conexion = calls.conexion()
    user_id = current_user_id(conexion)

    created_lists = calls.fetch_all(conexion, "SELECT * FROM listas WHERE usuario_creador = ?", user_id)
    voted_lists = calls.fetch_all(conexion, "SELECT DISTINCT * FROM votos INNER JOIN listas WHERE user_id = ? AND list_id = id", user_id)

    return render('profile.html', username=session["username"], created_lists=created_lists, voted_lists=voted_lists)

@app.route('/logout', methods = ['GET'])
def logout():
    # Borrar la sesion
    session.pop('loggedin', None)
    session.pop('username', None)

    return redirect('/')


@app.route('/categories', methods = ['GET'])
def view_category():
    if not 'loggedin' in session:
        return redirect("/login")

    category = request.args.get('id')

    # Listar categoria con el id pedido
    conexion = calls.conexion()
    listas = calls.fetch_all(conexion, "SELECT * FROM listas WHERE categoria = ?", category)
    categoria = calls.fetch_all(conexion, "SELECT * FROM categorias WHERE id = ?", category)

    return render('categoria.html', listas=listas, categoria=categoria[0])

@app.route('/lists', methods = ['GET'])
def view_list():
    if not 'loggedin' in session:
        return redirect("/login")

    lista_id = request.args.get('id')

    conexion = calls.conexion()
    user_id = current_user_id(conexion)
    elementos = calls.fetch_all(conexion, "SELECT * FROM elementos WHERE lista = ? ORDER BY votos DESC", lista_id)
    lista = calls.fetch_all(conexion, "SELECT * FROM listas WHERE id = ?", lista_id)[0]

    resultados_votado = calls.fetch_all(conexion, "SELECT element_id FROM votos WHERE list_id = ? AND user_id = ?;", lista_id, user_id)

    votado = resultados_votado[0]["element_id"] if len(resultados_votado) > 0 else None

    calls.modify(conexion, UPDATE_VISITAS_LISTA, lista["id"])

    return render("lista.html", elementos=elementos, lista=lista, votado=votado)

@app.route('/lists/create', methods=['POST'])
def create_list():
    if not 'loggedin' in session:
        return redirect("/login")

    category = request.form['category_id']
    title = request.form['title']
    description = request.form['description']
    image = request.form['image']

    conexion = calls.conexion()
    user_id = current_user_id(conexion)
    calls.modify(conexion, INSERTAR_LISTA, category, user_id, title, description, image)

    return jsonify(message="Lista creada"), 200

@app.route('/elements/create', methods=['GET', 'POST'])
def create_element():
    if request.method == 'GET':
        if not 'loggedin' in session:
            return redirect("/login")
        else:
            conexion = calls.conexion()
            list = calls.fetch_all(conexion, "SELECT * FROM listas WHERE id=?", request.args.get('lista'))[0]
            return render('crear_elemento.html', lista=list)
    elif request.method == 'POST':
        lista_id = request.form['list_id']
        name = request.form['name']
        description = request.form['description']

        conexion = calls.conexion()

        lista = calls.fetch_all(conexion, "SELECT * FROM listas WHERE id = ?", lista_id)[0]

        calls.modify(conexion, INSERTAR_ELEMENTO, lista_id, name, description)
        return jsonify(message="Elemento creado correctamente"), 200

@app.route('/elements/vote', methods=['POST'])
def vote_element():
    elemento_id = request.values["elemento_id"]

    conexion = calls.conexion()

    lista_id = calls.fetch_all(conexion, "SELECT lista FROM elementos WHERE id = ?;", elemento_id)[0]["lista"]
    user_id = current_user_id(conexion)

    if len(calls.fetch_all(conexion, "SELECT * FROM votos WHERE list_id = ? AND user_id = ?;", lista_id, user_id)) == 0:
        calls.modify(conexion, UPDATE_VOTOS_ELEMENTO_SUMAR, elemento_id)
        calls.modify(conexion, INSERTAR_VOTO, user_id, lista_id, elemento_id)
        return jsonify(message="Elemento votado correctamente"), 200
    return jsonify(message="Elemento votado correctamente"), 409

@app.route('/elements/deletevote', methods=['DELETE'])
def delete_element():
    elemento_id = request.values["elemento_id"]

    conexion = calls.conexion()

    lista_id = calls.fetch_all(conexion, "SELECT lista FROM elementos WHERE id = ?;", elemento_id)[0]["lista"]
    user_id = current_user_id(conexion)

    calls.modify(conexion, BORRAR_VOTO, user_id, elemento_id, lista_id)
    calls.modify(conexion, UPDATE_VOTOS_ELEMENTO_RESTAR, elemento_id)

    return jsonify(message="Elemento borrado correctamente"), 200


@app.route("/lists/search", methods=['GET'])
def search_list():
    query = request.args.get('query')

    conexion = calls.conexion()

    lists = calls.fetch_all(conexion, SEARCH_LIST, '%{}%'.format(query.lower()))
    return render('search.html', listas=lists, query=query)


def current_user_id(conexion):
    return calls.fetch_all(conexion, "SELECT id FROM usuarios WHERE username = ?;", session["username"])[0]["id"]


if __name__ == '__main__':
    app.run()