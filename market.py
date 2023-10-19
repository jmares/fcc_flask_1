from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1><h2>Some Text</h2><p>Lorum ipsum ...</p>'
