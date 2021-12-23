from flask import Flask, render_template
from forms.login import LoginForm
from forms.register import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ebc701ad02288d439cc079060cb28dbe681b9d100e387ac40cbb0728150b4aef'


@app.route("/")
def index():
    return render_template('base.html')


@app.route("/<user_id>/home/status")
def home(user_id):
    return render_template('home.html', user_id=user_id)


@app.route("/sign_in")
def signin():
    form = LoginForm()
    return render_template('sign-in.html', form=form)


@app.route("/sign_up")
def signup():
    form = RegistrationForm()
    return render_template('sign-up.html', form=form)


@app.route("/<user_id>/blog-posts/new-post")
def post():
    return render_template('post.html')


@app.route("/<user_id>/profile")
def profile(user_id):
    return render_template('profile.html', user_id=user_id)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
