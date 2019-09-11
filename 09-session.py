"""
原生flask将session存在了浏览器中
需要加密
在配置中设置私钥
"""

from flask import Flask, session

app = Flask(__name__)


class DefaultConfig(object):
    SECRET_KEY = 'asdfghjkl'


app.config.from_object(DefaultConfig)


@app.route('/set')
def set_session():
    session['user_id'] = 123
    return 'ok'


@app.route('/get')
def get_session():
    print(session.get('user_id'))
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True)
