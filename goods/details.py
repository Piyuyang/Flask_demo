from flask_restful import Resource

# from . import goods_bp


# @goods_bp.route('/details')
# def details():
#     return 'details'


class DetailsResource(Resource):
    def get(self):
        return {"msg": "in DetailsResource"}
