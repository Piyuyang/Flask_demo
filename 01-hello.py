from flask import Flask


# 配置对象加载
class DefaultConfig(object):
    REDIS_ADDR = "redis in class"
    MYSQL_ADDR = "mysql"


# 构造对象
# import_name:app初始化参数
app = Flask(__name__)

# 工程配置参数 由app.config字典类型属性保存
app.config.from_object(DefaultConfig)


# 定义路由规则及视图
@app.route('/')
def index():

    # 测试配置是否生效
    print(app.config.get('REDIS_ADDR'))

    return "hello"


if __name__ == '__main__':
    # 运行项目
    app.run()
