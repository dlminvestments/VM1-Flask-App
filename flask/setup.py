pip install -U Flask

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
$ env FLASK_APP=server.py flask run
 * Serving Flask app "server"
 * Running on http://127.0.0.1:5000 /
