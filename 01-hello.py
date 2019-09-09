from flask import Flask

# 构造对象
# import_name:app初始化参数
app = Flask(__name__)


# 定义路由规则及视图
@app.route('/')
def index():
    return "hello"


if __name__ == '__main__':
    # 允许项目
    app.run()
