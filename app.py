from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index_page():
   message = 'Добро пожаловать! 123456qwerty'
   return render_template('index.html', message=message)