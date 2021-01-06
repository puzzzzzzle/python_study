from flask import Flask, session, redirect, url_for, escape, request
import time
import logging
import consts

logger = logging.getLogger(__name__)

app = Flask(__name__)

# 符合直觉的: 参数优先级比页面低, 贪心匹配方式
# path/ 访问地址
# path
# @app.route('/<name>')
# def hello_world(name):
#     time.sleep(2)
#     return f'name {name}!'


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(threaded=True)
