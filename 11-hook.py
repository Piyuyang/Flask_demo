"""
after_request和teardown_appcontext需要接收response作为参数
after_request需要将参数中的response返回
"""
from flask import Flask

app = Flask(__name__)


@app.before_first_request
def fun1():
    print("before first request")


@app.before_request
def fun2():
    print("before request")


@app.after_request
def fun3(response):
    print("after request")
    return response


@app.teardown_appcontext
def fun4(response):
    print("teardown appcontext")


@app.route('/')
def index():
    print("in view")
    return "ok"


if __name__ == '__main__':
    app.run()
