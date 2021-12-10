from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/<user_id>/home")
def home(user_id):
    return render_template('home.html', user_id=user_id)


@app.route("/sign_in")
def signin():
    return render_template('sing-in.html')


@app.route("/sign_up")
def signup():
    return render_template('sign_up.html')


@app.route("/<user_id>/blog-posts/new-post")
def post():
    return render_template('post.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)
