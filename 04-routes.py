import json

from flask import Flask

# 构造对象
# import_name:app初始化参数
app = Flask(__name__)


# 定义路由规则及视图
@app.route('/')
def index():
    print(app.url_map)  # app.url_map保存了flask的所有路由地址
    # <Rule '/' (GET, OPTIONS, HEAD) -> index>,
    # <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>])
    return "hello"


# 需求：获取当前web应用的所有接口
@app.route('/route')
def routes():
    api_list = []
    # app.url_map.iter_rules()可以理解为列表
    for item in app.url_map.iter_rules():
        api_list.append({
            'name': item.endpoint,
            'path': item.rule
        })
    return json.dumps({"api": api_list})

# if __name__ == '__main__':
#     # 运行项目
#     app.run()
