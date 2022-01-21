import os
from flask import Flask
app = Flask(__name__)

# @app.route("/hello")
# def hello():
#     foo = os.environ.get('FOO')
#     return f'Hello World! Env Value: {foo}'


@app.route('/')
def hello():
    return '<h1>Hello, World!</h1>'


@app.route('/about/')
def about():
    return '<h1>This is the about page.</h1>'
