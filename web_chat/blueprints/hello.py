from flask import Blueprint

main = Blueprint("main", __name__, url_prefix="/")

@main.route('/')
def hello_world():
    return 'Hello, World!'

