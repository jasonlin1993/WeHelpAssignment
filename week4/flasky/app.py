from flask import Flask  
from flask import request 
from flask import render_template 
from flask import session
from flask import redirect

app = Flask(
    __name__,
    static_folder='static',  
    static_url_path='/' 
)

app.secret_key="test"

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/member")
def member():
    if "account" in session:
        return render_template("member.html")
    else:
        return redirect("/")

@app.route("/error")
def error():
    message=request.args.get("message", "帳號、或密碼輸入錯誤")
    return render_template("error.html", message=message)

@app.route('/signin', methods=['POST'])
def signin():
    account = request.form.get('account')
    password = request.form.get('password')

    # 1. 我們要處理帳號或密碼是空白的狀況，錯誤訊息不同。
    if not account  or not password:
        return redirect("/error?message=請輸入帳號、密碼")
    
    elif account == 'test' and password == 'test':
        session['account']=account
        return redirect("/member")
    
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route('/signout')
def signout():
    del session["account"]
    return redirect("/")

@app.route("/square/<int:count>")
def square(count):
    ans = count * count
    return render_template("squareNumber.html", result=ans)

if __name__ == "__main__":
    app.run(port=3000)
