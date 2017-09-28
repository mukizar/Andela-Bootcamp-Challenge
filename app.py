"""Setting up flaskApp"""
from flask import Flask, render_template, request
from data import Posts
from wtforms import Form, StringField, PasswordField, validators

app = Flask(__name__) # pylint: disable=invalid-name

POSTS = Posts()

@app.route('/')
def home():
    """function to return home template"""
    return render_template('home.html')

@app.route("/about")
def about():
    """function to return about template"""
    return render_template("about.html")

@app.route("/posts")
def posts():
    """function to return posts template"""
    return render_template("posts.html", POSTS=Posts)

class SignUpForm(Form):
    """Setting up wtform for SignUp"""
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
    """function for returning the SignUp page"""
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('signup.html')
    return render_template('signup.html', form=form)

class SignInForm(Form):
    """Setting up wtform for SignIn"""
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route("/signin", methods=['GET', 'POST'])
def sign_in():
    """function to return SignIn page"""
    form = SignInForm(request.form)
    return render_template("signin.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
