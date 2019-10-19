from flask import Flask, render_template, session, request, redirect
from models.mysql_model import *

app = Flask(__name__)

app.config['SECRET_KEY'] = "abang12345QWERTY"

@app.route('/index')
def index():
    stock = [
        "bantal",
        "meja",
        "kursi",
        "jam tangan",
        "dompet kulit",
        "handphone",
        "gesper",
        "tissue",
    ]

    return render_template("index.html", data={"stock":stock, "harga":1200})


@app.route('/home')
def home():
    if 'username' in session:
        return render_template("home.html")
    else:
        return redirect('/login')


@app.route('/about')
def about():
    if 'username' in session:
        return render_template("about.html")
    else:
        return redirect('/login')


@app.route('/contact')
def contact():
    if 'username' in session:
        return render_template("contact.html")
    else:
        return redirect('/login')


@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if 'username' in session:
            return redirect('/index')
        else:
            return render_template("auth/login.html")

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if data_checking(username,password) == 1:
            session['username'] = username
            return redirect('/index')
        else:
            return "invalid username or password"

@app.route('/logout')
def logout():
    session.pop('username')
    return redirect('/login')


@app.route('/dbtest')
def dbtest():
    # cursor = mysql.connection.cursor()
    # cursor.execute("INSERT INTO users (username,password) VALUES (%s,%s)",(username,password))
    # mysql.connection.commit()
    # cursor.close()

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
    mysql.connection.commit()
    cur.close()

    return "ok"





# RUN ------------------------------------------------------+
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

