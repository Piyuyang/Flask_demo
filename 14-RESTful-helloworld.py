import re

from flask import Flask
from flask_restful import Api, Resource, inputs
from flask_restful.reqparse import RequestParser

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


def mobile(mobile_str):
    """
    自定义格式检验
    :param mobile_str: 手机号字符串
    :return:
    """
    if re.match(r'^1[3-9]\d{9}$', mobile_str):
        return mobile_str
    else:
        raise ValueError('{} is not a valid mobile'.format(mobile_str))


class IndexResource(Resource):
    # method_decorators = [decoration1, decoration2]

    # 相当于下面这种装饰顺序
    # 输出为：
    # in decoration2
    # in decoration1
    # in resource

    # @decoration2
    # @decoration1
    def get(self):
        print('in resource')

        # 检验、转换请求数据
        rp = RequestParser()
        rp.add_argument('username', type=str, required=True, help='missing username')
        # rp.add_argument('id', action='append')
        rp.add_argument('id', action='store')
        rp.add_argument('mobile', type=mobile)
        data = rp.parse_args()
        # return {"msg": "index page"}
        return {'data': data}

    def post(self):
        pass


app.register_blueprint(goods_bp)
api.add_resource(IndexResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
