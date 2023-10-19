from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello, World!</h1><h2>Some Text</h2><p>Lorum ipsum ...</p>'

@app.route('/about')
def about_page():
    return f'<h1>About</h1><h2>This Site</h2><p>Lorum ipsum ...</p>'

@app.route('/about/<username>')
def about_dpage(username):
    return f'<h1>About</h1><h2>{username}</h2><p>Lorum ipsum ...</p>'