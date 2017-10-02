"""Setting up flaskApp"""
from flask import Flask, render_template, request, flash
from data import Recipes
from wtforms import Form, StringField, PasswordField, validators
import users_data

app = Flask(__name__) # pylint: disable=invalid-name

Recipes = Recipes() # pylint: disable=invalid-name

@app.route("/")
def home():
    """function to return home template"""
    return render_template('home.html')

@app.route("/about")
def about():
    """function to return about template"""
    return render_template("about.html")

@app.route("/recipes")
def user_recipes():
    """function to return recipes template"""
    return render_template("recipes.html", recipes=Recipes)

@app.route("/recipe/<string:ID>/")
def user_recipe(ID):
    """function to return recipe template"""
    return render_template("recipe.html", ID=ID)

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
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = form.password.data
        add_user = users_data.Users(name, username, email, password)
        add_user.signup()

        return render_template('signin.html')

    return render_template('signup.html', form=form)

class SignInForm(Form):
    """Setting up wtform for SignIn"""
    email = StringField('Email', [validators.Length(min=6, max=50)])
    password = PasswordField('Password', [validators.DataRequired()])

@app.route("/signin", methods=['GET', 'POST'])
def sign_in():
    """function to return SignIn page"""
    form = SignInForm(request.form)
    if request.method == 'POST' and form.validate():
        email = form.email.data
        password = form.password.data

        if email in users_data.registered_users:
            #signedin_user = users_data.Users(email, password)
            return render_template("dashboard.html",form = form)

    return render_template("signin.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
