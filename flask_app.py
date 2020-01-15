from flask import Flask, request
from flask import render_template, redirect, url_for
from flask_login import current_user, login_user

import db.llamadas as calls
from db.queries import INSERTAR_USUARIO, INSERTAR_LISTA
from users.registro import hash_password, verify_password

app = Flask(__name__, template_folder='templates')

def coger_categorias():
    conexion = calls.conexion()
    return calls.fetch_all(conexion, "SELECT * FROM `categorias`")

def render(template, **kwargs):
    return render_template(template, categorias=coger_categorias(), **kwargs)

@app.route('/')
def index():
    top_listas = calls.fetch_all(calls.conexion(), "SELECT * "
                                                   "FROM listas INNER JOIN categorias "
                                                   "WHERE listas.categoria = categorias.Id ORDER BY listas.visitas DESC LIMIT 4")
    print(top_listas)
    return render('index.html', top_listas=top_listas)

@app.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect("/")
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
        flash('Invalid username or password')
        return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    return redirect(url_for('index'))
    return render('login.html')

@app.route('/register')
def register_page():
    return render('register.html')

@app.route('/lists')
def create_list_page():
    return render('crear_lista.html')

@app.route('/categories', methods = ['GET'])
def categories():
    category = request.args.get('id')

    conexion = calls.conexion()
    listas = calls.fetch_all(conexion, "SELECT * FROM listas WHERE categoria = %s", category)

    return render('listas.html', listas=listas)

@app.route('/user/login', methods = ['POST'])
def login_user():
    username = request.form['username']
    password = request.form['password']

    conexion = calls.conexion()
    salt = calls.fetch_all(conexion, "SELECT salt FROM usuarios WHERE username=%s", username)[0]["salt"]
    key = verify_password(password, bytes(salt, "utf-8"))

    result = calls.fetch_all(conexion, "SELECT * FROM usuarios WHERE username=%s AND password=%s", username, key)

@app.route('/user/register', methods = ['POST'])
def register_user():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    hashed_password, salt = hash_password(password)

    conexion = calls.conexion()
    calls.modify(conexion, INSERTAR_USUARIO, email, hashed_password, salt, username)

@app.route('/lists/create', methods=['POST'])
def create_list():
    category = request.form['category_id']
    title = request.form['title']
    description = request.form['description']
    image = request.form['image']

    conexion = calls.conexion()
    calls.modify(conexion, INSERTAR_LISTA, category, title, description, image)


if __name__ == '__main__':
    app.run()