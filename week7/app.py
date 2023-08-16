import os
import mysql.connector
from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from flask import json
from flask import jsonify
from dotenv import load_dotenv
from mysql.connector import pooling


load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# 連線到資料庫
pool = pooling.MySQLConnectionPool(pool_name="mypool",
                                   pool_size=10,
                                   host='localhost',
                                   database='website',
                                   user=DB_USER,
                                   password=DB_PASS)
app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/'
)
app.secret_key = "123456789"


def is_username_registered(username):
    with pool.get_connection() as database:
        with database.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM member WHERE username=%s", (username,))
            result = cursor.fetchall()
            return bool(result)


def register_member(name, username, password):
    with pool.get_connection() as database:
        with database.cursor() as cursor:
            cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)",
                           (name, username, password))
            cursor.commit()


def check_member_credentials(username, password):
    with pool.get_connection() as database:
        with database.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT * FROM member WHERE username=%s AND password=%s", (username, password))
            member = cursor.fetchone()
            return member


def get_form_data(form_type):
    if form_type == 'signup':
        return {
            'username': request.form.get('username'),
            'password': request.form.get('password'),
            'name': request.form.get('name')
        }
    elif form_type == 'signin':
        return {
            'username': request.form.get('username'),
            'password': request.form.get('password')
        }


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/member")
def member():
    if "name" in session:
        name = session.get("name", "小明")
        return render_template("member.html", name=name)
    else:
        return redirect("/")


@app.route("/api/member", methods=['GET', 'PATCH'])
def api_member():
    if request.method == 'GET':
        return get_member()
    elif request.method == 'PATCH':
        return patch_member_name()


def get_member():
    username = request.args.get("username")
    with pool.get_connection() as database:
        with database.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT * FROM member WHERE username=%s", (username,))
            member = cursor.fetchone()
    if member:
        return jsonify(data={
            "id": member['id'],
            "name": member['name'],
            "username": member['username']
        })
    else:
        return jsonify(data=None)


def patch_member_name():
    if "username" not in session:
        return jsonify(error=True)

    new_name = request.json.get("name")
    username = session['username']

    with pool.get_connection() as database:
        with database.cursor(dictionary=True) as cursor:
            cursor.execute(
                "UPDATE member SET name = %s WHERE username = %s", (
                    new_name, username)
            )
            database.commit()
    return jsonify(ok=True)


@app.route("/error")
def error():
    message = request.args.get("message", "帳號、或密碼輸入錯誤")
    return render_template("error.html", message=message)


@app.route("/signup", methods=['POST'])
def signup():
    form_data = get_form_data('signup')
    if is_username_registered(form_data['username']):
        return redirect("/error?message=帳號已經被註冊")
    register_member(form_data['name'],
                    form_data['username'], form_data['password'])
    return redirect("/")


@app.route('/signin', methods=['POST'])
def signin():
    form_data = get_form_data('signin')
    member = check_member_credentials(
        form_data['username'], form_data['password'])
    if member:
        session['id'] = member['id']
        session['name'] = member['name']
        session['username'] = member['username']
        return redirect("/member")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")


@app.route('/signout')
def signout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(port=3000, debug=1)
