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