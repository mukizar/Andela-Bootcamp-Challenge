from flask import Flask, render_template, request
from data import Posts
from wtforms import Form, StringField, TextAreaField, PasswordField, validators

app = Flask(__name__)

Posts = Posts()


@app.route('/')
def home():
    return render_template('home.html')




@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/posts")
def posts():
    return render_template("posts.html", posts= Posts)

class SignUpForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords do not match')
    ])
    confirm = PasswordField('Confirm Password')

#User SignUp
@app.route('/signup', methods=['GET', 'POST'])
def SignUp():
    form = SignUpForm(request.form)
    if request.method == 'POST' and form.validate():
        return render_template('signup.html') 
    return render_template('signup.html', form=form)

class SignInForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password',[validators.DataRequired()])

# User Signin
@app.route("/signin", methods=['GET', 'POST'])
def signin():
    form = SignInForm(request.form)
    return render_template("signin.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)