from flask import Flask, render_template, redirect, jsonify, make_response

app = Flask(__name__)


# 渲染模板
@app.route('/')
def index():
    data = {
        'my_str': 'python',
        'my_int': 123
    }
    return render_template('index.html', **data)


# 重定向
@app.route('/index')
def re_index():
    return redirect('/')


# 返回json
@app.route('/json')
def re_json():
    data = {
        'my_str': 'python',
        'my_int': 123
    }
    return jsonify(data)


# 返回自定义
@app.route('/my_return')
def my_return():
    # return 响应体, 状态码, 响应头
    # 响应头形式一：[(响应头名字1, 响应头值1), (响应头名字2, 响应头值2), ..]
    # 响应头形式二：{响应头名字1:响应头值1, 响应头名字2:响应头值2, ..}
    return "my return", 200, {'user_name': 'pyy'}


# make_response() 构造响应对象
@app.route('/my_response')
def my_response():
    res = make_response("my_response")
    res.headers['user_name'] = 'pyy'
    # res.status = 200  # Invalid status argument
    return res


if __name__ == '__main__':
    app.run(debug=True)
