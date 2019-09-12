from flask_restful import Resource, fields, marshal, marshal_with


# from . import goods_bp


# @goods_bp.route('/details')
# def details():
#     return 'details'


class Goods(object):
    """
    模拟返回的数据对象的类
    """

    def __init__(self, name, price):
        self.name = name
        self.price = price


resource_fields = {
    'name': fields.String,
    'price': fields.Float
}


class DetailsResource(Resource):

    # 方式一：装饰器
    # @marshal_with(resource_fields, envelope='data')
    # def get(self):
    #     goods = Goods('iphone', 8000.00)
    #     return goods

    # 方式二：函数
    def get(self):
        goods = Goods('iphone', 8000.00)
        return marshal(goods, resource_fields, envelope='data')
