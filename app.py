import os
from flask import Flask

app = Flask(__name__)
version = os.environ['VERSION']


@app.route('/')
def index():
    version = os.environ['VERSION']
    return f'app running version {version}'

@app.route('/second')
def index():
    return f'second route'


if __name__ == "__main__":
    pass