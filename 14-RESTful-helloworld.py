from flask import Flask
from flask_restful import Api, Resource

from goods import goods_bp

app = Flask(__name__)
api = Api(app)


def decoration1(func):
    def wrapper(*args, **kwargs):
        print('in decoration1')
        return func(*args, **kwargs)

    return wrapper


def decoration2(func):
    def wrapper(*args, **kwargs):
        print('in decoration2')
        return func(*args, **kwargs)

    return wrapper


class IndexResource(Resource):
    method_decorators = [decoration1, decoration2]

    # 相当于下面这种装饰顺序
    # 输出为：
    # in decoration2
    # in decoration1
    # in resource

    # @decoration2
    # @decoration1
    def get(self):
        print('in resource')
        return {"msg": "index page"}

    def post(self):
        pass


app.register_blueprint(goods_bp)
api.add_resource(IndexResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
