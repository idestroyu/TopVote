from flask import Flask
from flask import render_template

import db.llamadas as calls

app = Flask(__name__, template_folder='templates')

def coger_categorias():
    conexion = calls.conexion()
    return calls.select(conexion, "SELECT * FROM `categorias`")

@app.route('/')
def index():
    return render_template('index.html', categorias=coger_categorias())

@app.route('/login')
def login():
    return render_template('login.html', categorias=coger_categorias())\

@app.route('/register')
def register_page():
    return render_template('register.html', categorias=coger_categorias())

@app.route('/user/register', methods = ['POST'])
def register_user():
    conexion = calls.conexion()


if __name__ == '__main__':
    app.run()