from flask import Flask

from users import users_bp

# 构造对象
# import_name:app初始化参数
app = Flask(__name__)


# 定义路由规则及视图
@app.route('/')
def index():
    return "hello"


# 注册蓝图对象
app.register_blueprint(users_bp, url_prefix='/users')

if __name__ == '__main__':
    # 运行项目
    app.run()
