from flask import Blueprint
from flask_restful import Api

from .details import DetailsResource

goods_bp = Blueprint('goods', __name__)

# from . import details
goods_api = Api(goods_bp)
goods_api.add_resource(DetailsResource, '/details')
