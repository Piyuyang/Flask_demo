from flask import Flask

# 构造对象
# import_name:app初始化参数
app = Flask(__name__)


# 定义路由规则及视图
@app.route('/')
def index():
    return "hello"


if __name__ == '__main__':
    # 运行项目
    app.run(
        host='0.0.0.0',  # 访问ip
        port=8000,  # 访问端口
        debug=True  # 前端展示具体的错误信息、修改代码后重启服务器
    )
