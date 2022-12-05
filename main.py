
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=["GET"])
def app(event):
    return "Hello, world!"
