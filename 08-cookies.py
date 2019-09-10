from flask import Flask, make_response, request

app = Flask(__name__)


@app.route('/set')
def set_cookies():
    """
    设置
    :return:
    """
    res = make_response("set cookies")
    # set_cookie(名称, 值, max_age=过期时间)
    res.set_cookie('user_id', '123', max_age=3600)
    return res


@app.route('/get')
def get_cookies():
    """
    读取
    :return:
    """
    print(request.cookies.get('user_id'))
    return 'OK'


@app.route('/del')
def del_cookies():
    """
    清除
    :return:
    """
    res = make_response("delete cookies")
    res.delete_cookie('user_id')
    return res


if __name__ == '__main__':
    app.run(debug=True)
