"""
请求上下文：request，session
应用上下文：
    current_app 在不方便使用app获取属性数据的时候，可以直接使用current_app来代替app
    g 在flask处理一个请求的周期中，调用的多个函数间利用g对象传递参数
"""
from flask import Flask, g
from users import users_bp

app = Flask(__name__)
app.database = 'my_database'
app.register_blueprint(users_bp)


@app.before_request
def fun2():
    g.table = 'my_table'
    print("before request")


@app.route('/')
def index():
    print(g.table)
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
