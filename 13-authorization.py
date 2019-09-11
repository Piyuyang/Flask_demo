"""
需求：
构建认证机制
对于特定视图可以提供强制要求用户登录的限制
对于所有视图，无论是否强制要求用户登录，都可以在视图中尝试获取用户认证后的身份信息
"""
import functools

from flask import Flask, g, abort

app = Flask(__name__)


@app.before_request
def get_auth():
    # TODO:判断用户是否登录逻辑

    # 若用户已登录
    # g.user_id = 1

    # 若用户未登录
    g.user_id = None


def login_required(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        装饰器
        :param args:
        :param kwargs:
        :return:
        """
        if g.user_id:
            return func(*args, **kwargs)
        else:
            abort(401)

    return wrapper


@app.route('/login')
@login_required
def login():
    """
    登录
    :return:
    """
    return 'user {} login'.format(g.user_id)


if __name__ == '__main__':
    print(login.__name__)
    print(login.__doc__)
    app.run(debug=True)
