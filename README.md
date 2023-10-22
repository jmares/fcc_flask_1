# FreeCodeCamp - Flask Tutorial 1

## Introduction

Project based on the FreeCodeCamp Flask tutorial:

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

