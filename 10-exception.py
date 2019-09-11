from flask import Flask, abort

app = Flask(__name__)


@app.errorhandler(ZeroDivisionError)
def func(e):
    return "被除数不能为0"


@app.route('/')
def index():
    # abort(404)
    a = 1 / 0
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
