from . import goods_bp


@goods_bp.route('/details')
def details():
    return 'details'
