from flask import Flask, request
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 自定义转换器
class MobileConverter(BaseConverter):
    """自定义手机号转换器"""
    regex = r'1[3-9]\d{9}'


# 注册自定义转换器
app.url_map.converters['mobile'] = MobileConverter


# 路径参数
@app.route('/users/<int(min=1):user_id>')
def login(user_id):
    return "login page {}".format(user_id)


@app.route('/sms/<mobile:mobile_num>')
def sms(mobile_num):
    return "send sms to {}".format(mobile_num)


# 查询参数
@app.route('/users')
def get_user():
    user_id = request.args.get('pk')
    return "get user {}".format(user_id)


# 上传文件
@app.route('/file', methods=['POST'])
def save():
    # 从request中取出的是File对象，可以直接读
    file_obj = request.files.get('pic')

    # 普通方法
    # with open('./demo.jpg', 'wb') as new_file:
    #     new_file.write(file_obj.read())

    # flask额外提供了save方法，用于保存到本地
    file_obj.save('./demo.jpg')

    return "save pic ok"


if __name__ == '__main__':
    app.run(debug=True)
