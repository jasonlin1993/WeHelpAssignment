from flask import Flask
from flask import request
from flask import render_template
from flask import session
from flask import redirect
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

# 連線到資料庫
db = mysql.connector.connect(
    user=DB_USER,
    password=DB_PASS,
    host='localhost',
    database='website'
)

app = Flask(
    __name__,
    static_folder='static',
    static_url_path='/'
)
app.secret_key = "test"


def get_messages():
    cursor = db.cursor()
    cursor.execute(
        "SELECT member.name, message.content FROM member INNER JOIN message ON member.id=message.member_id ORDER BY message.time DESC;")
    messages = cursor.fetchall()
    cursor.close()
    return messages


def is_username_registered(username):
    cursor = db.cursor()
    cursor.execute(
        # 判斷帳號使否重複，不會使用 LIKE 來做比對，完全比對就使用 = 就好
        "SELECT * FROM member WHERE username=(%s)", (username,))
    result = cursor.fetchall()
    cursor.close()
    return bool(result)


def register_member(name, username, password):
    cursor = db.cursor()
    cursor.execute("INSERT INTO member(name, username, password) VALUES(%s, %s, %s)",
                   (name, username, password))
    db.commit()
    cursor.close()


def check_member_credentials(username, password):
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM member WHERE username=%s AND password=%s", (username, password))
    member = cursor.fetchone()
    cursor.close()
    return member


def create_message(member_id, content):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO message (member_id, content) VALUES (%s, %s)", (member_id, content))
    db.commit()
    cursor.close()


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
    elif form_type == 'create_message':
        return {
            'content': request.form.get('content')
        }


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/member")
def member():
    if "name" in session:
        name = session.get("name", "小明")
        messages = get_messages()
        return render_template("member.html", name=name, messages=messages)
    else:
        return redirect("/")


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
        session['id'] = member[0]
        session['name'] = member[1]
        session['username'] = member[2]
        return redirect("/member")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")


@app.route("/createMessage", methods=['POST'])
def createMessage():
    form_data = get_form_data('create_message')
    member_id = session['id']
    create_message(member_id, form_data['content'])
    return redirect("/member")


@app.route('/signout')
def signout():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(port=3000, debug=1)
