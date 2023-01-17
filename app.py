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

@app.route('/more_additions')
def index():
    return f'more_additions'


if __name__ == "__main__":
    pass