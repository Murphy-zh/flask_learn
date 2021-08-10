from flask import Flask,url_for,render_template,make_response,abort, redirect,jsonify
from flask import request
from markupsafe import escape
app = Flask(__name__)

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % escape(username)

# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id

# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return 'Subpath %s' % escape(subpath)

# @app.route('/projects/')
# def projects():
#     return 'The project page'

# @app.route('/about')
# def about():
#     return 'The about page'

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return "this is post"
#     else:
#         return "this is get"

# @app.route('/')
# def index():
#     return 'index'


# @app.route('/user/<username>')
# def profile(username):
#     return '{}\'s profile'.format(escape(username))

# # with app.test_request_context():
# #     print(url_for('index'))
# #     print(url_for('login'))
# #     print(url_for('login', next='/'))
# #     print(url_for('profile', username='John Doe'))

# @app.route('/get_static')
# def get_static():
#     return url_for('static', filename='hahaha.txt')

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)


# @app.route('/')
# def index():
#     resp = make_response(render_template("hello.html"))
#     resp.set_cookie('username', 'this is cookie')
#     print(resp.set_cookie)
#     return resp


@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(404)

@app.errorhandler(404)
def page_not_found(error):
    # return render_template('hello.html'), 404
    resp = make_response(render_template('hello.html'), 404)
    resp.headers['X-Something'] = 'ooc'
    return resp

def get_current_user():
    user = {
        "username": "user.username",
        "theme": "user.theme",
        "image": 'imane'
    }
    return user

@app.route("/me")
def me_api():
    user = get_current_user()
    return {
        "username": user.get("username"),
        "theme": user.get("theme"),
        "image": url_for("user_image", filename=user.get("image")),
    }

