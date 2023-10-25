# FreeCodeCamp - Flask Tutorial 1

## Introduction

Project based on a FreeCodeCamp Flask tutorial:

- **YouTube**: [Flask Course - Python Web Application Development](https://www.youtube.com/watch?v=Qr4QMBUPxWo)
- **Date**: 10/03/2021
- **GitHub**: [FlaskSeries](https://github.com/jimdevops19/FlaskSeries)
- **Technology**: Python (>= 3.8), Flask, SQLite, and Bootstrap 4

Make a website where you can buy and sell stuff.

## Lessons

If you want to see the code for the lesson, use the corresponding tag to switch to that version.

### Lesson 01 - Introduction

Using VSCode, create a virtual environment for this project. I am currently using Windows 11 with Python 3.11.2.

Install dependencies

```shell
pip install flask
```

Test whether Flask is installed correctly:

```shell
flask --version
```

```
Python 3.11.2
Flask 3.0.0
Werkzeug 3.0.0
```

To execute the script:

```shell
flask --app market run
```

Debug mode:

```shell
flask --app market run --debug
```

In debug mode you don't need to restart the server to see the changes you made.

Create a second page:

```python
@app.route('/about')
def about_page():
    return '<h1>Hello, World!</h1><h2>This Site</h2><p>Lorum ipsum ...</p><h2>The Owner</h2><p>Lorum ipsum ...</p>'
```

Turn add a third dynamic route/page:

```python
@app.route('/about')
def about_page():
    return f'<h1>About</h1><h2>This Site</h2><p>Lorum ipsum ...</p>'

@app.route('/about/<username>')
def about_dpage(username):
    return f'<h1>About</h1><h2>{username}</h2><p>Lorum ipsum ...</p>'
```

### Lesson 02 - Styling and Templates

Mostly an introduction to Bootstrap.

### Lesson 3 - Sending Data to Templates

**Jinja2 template**

Example:

A simple example:

In `market.py`:

```python
@app.route('/market')
def market_pafe():
    return render_template('market.html', item_name='Phone')
```

In `market.html`:

```html
<p>{{ item_name }}</p>
```

A less simple example:

In `market.py`:

```python
@app.route('/market')
def market_pafe():
    items = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items=items)
```

In `market.html`:

```html
<table class="table table-hover table-dark">
    <thead>
        <tr>
            <th scope="col">ID</th>
            <th scope="col">Name</th>
            <th scope="col">Barcode</th>
            <th scope="col">Price</th>
            <th scope="col">Options</th>
        </tr>
    </thead>
    <tbody>
        {% for item in items %}
            <tr>
                <td>{{ item.id }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.barcode }}</td>
                <td>{{ item.price }}$</td>
                <td>
                    <button class="btn btn-outline btn-info">More Info</button>
                    <button class="btn btn-outline btn-success">Purchase this Item</button>
                </td>
            </tr>
        {% endfor %}
    </tbody>
</table>
```

### Lesson 04 - Template Inheritance

The idea is to have 1 base HTML template on which all other HTML templates are based. Less copying and pasting, easier maintenance.

Don't hardcode links in the navbar, but use the Flask function `url_for()` to refer to the route:

```html
<a class="nav-link" href="{{ url_for('market_page') }}">Market</a>
```

### Lesson 05 - Models and Databases

Working with a SQLite3 database.

Install SQLAlchemy

```shell
pip install flask-sqlalchemy
```

Creating the database:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)
```

Creating a model that will become a table in the database:

```python
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024), nullable=False, unique=True)
```

Creating the database and adding an item manually via a python shell. You have to open the python shell in the directory that also contains `market.py`.
The method the author used, didn't work on my computer. The DB file also ended up in the `instance` directory instead of the current directory.

In the python shell (this is different from the video, but with the same results):

```python
>>> from market import app
>>> from market import db
>>> with app.app_context():
...     db.create_all()
...
>>> from market import Item
>>> item1 = Item(name='iPhone 10', price=500, barcode='846154104831', description='description for the iPhone 10')
>>> with app.app_context():
...     db.session.add(item1) 
...     db.session.commit()
...
>>> with app.app_context():
...     Item.query.all()    
...
[Item iPhone 10]
>>> item2 = Item(name='Laptop', price=600, barcode='321912987542', description='description for the laptop')       
>>> with app.app_context():
...     db.session.add(item2)
...     db.session.commit()
...     Item.query.all()
...
[Item iPhone 10, Item Laptop]
>>> with app.app_context():
...     for item in Item.query.all():
...             item.id
...             item.name
...             item.price
...             item.barcode
...             item.description
...
1
'iPhone 10'
500
'846154104831'
'description for the iPhone 10'
2
'Laptop'
600
'321912987542'
'description for the laptop'
>>> with app.app_context():
...     Item.query.filter_by(price=500)  
...
<flask_sqlalchemy.query.Query object at 0x0000022A1BC69850>
>>> with app.app_context():
...     for item in Item.query.filter_by(price=500):
...             item.name
...
'iPhone 10'
```

Exit from the python shell with `exit()` or `quit()`.

And start the app:

```shell
flask --app market run --debug
```

### Lesson 06 - Project Restructure

Porblem is to avoid circular imports: packages.

- Create the main application file: `run.py`
- Move imports and app and db initialization from `market.py` to `run.py`
- Move routes from `market.py` to `routes.py`
- Move `class Item` from `market.py` to `models.py`
- Delete `market.py`
- Create directory `market`
- Move files `routes.py` and `models.py` into the `market` directory
- Move directory `templates` into the `market` directory
- In `market` directory, create file `__init__.py`
- Move contents from `run.py` to `__init__.py`
- Add following code to `run.py`:

```python
from market import app

# Checks if the run.py file has executed directly and not imported
if __name__ == "__main__":
    app.run(debug=True)
```

- Running the app via `python .\run.py`, will result in page not found error
- Add the line `from market import routes` to `__init__.py`
- Running app now will result in error: `NameError: name 'app' is not defined`
- Insert the following lines at the top of the file `routes.py`:
    - `from market import app`
    - `from flask import render_template`
    - `from market.models import Item`
- Insert the following lines at the top of the file `models.py`:
    - `from market import db`

Contrary to the tutorial the database in my project was created in a directory `instance` instead of the working directory. And I have to keep it there, I cannot move the directory and the database into the `market` directory. Problem to be solved later.



## To Study

Learn more about

- Jinja
- SQLAlchemy
- Can I specify the location of the database instead of using the default location in an `instance` directory?
