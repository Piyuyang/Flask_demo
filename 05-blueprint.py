from flask import Flask

from goods import goods_bp
from users import users_bp

# 构造对象
# import_name:app初始化参数
app = Flask(__name__)


# 定义路由规则及视图
@app.route('/')
def index():
    return "hello"


# 注册蓝图对象-单一文件
app.register_blueprint(users_bp, url_prefix='/users')

# 注册蓝图对象-子目录划分蓝图范围
app.register_blueprint(goods_bp, url_prefix='/goods')

if __name__ == '__main__':
    # 运行项目
    app.run()
