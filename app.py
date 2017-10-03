"""Setting up flaskApp"""
from flask import Flask, redirect, url_for, render_template, request, flash
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
import users_data
import recipes_models

app = Flask(__name__) # pylint: disable=invalid-name

Recipes_ = recipes_models.user_recipes # pylint: disable=invalid-name

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
    return render_template("recipes.html", recipes=Recipes_)


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
        add_user = users_data.Users(email, password, name, username)
        add_user.signup()

        return render_template('signin.html')

    return render_template('signup.html', form=form)



@app.route("/signin", methods=['GET', 'POST'])
def sign_in():
    """function to return SignIn page"""
    if request.method == 'POST':
        email_ = request.form['email']
        password_ = request.form['password']

        for email in users_data.registered_users:
            if email == email_:
                return redirect(url_for('dashboard'))
            #loggedIn = users_data.Users(email, password)

    return render_template("signin.html")


# User dashboard
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    """function to return dashboard page"""
    return render_template('dashboard.html', recipes=Recipes_)


class RecipeForm(Form):
    """Recipe form class"""
    title = StringField('Title', [validators.Length(min=10)])
    details = TextAreaField('Details', [validators.Length(min=10)])

# Create Recipe Route
@app.route('/create_recipe', methods=['GET', 'POST'])
def create_recipe():
    """intiate form for creating a new recipe"""
    form = RecipeForm(request.form)
    if request.method == 'POST' and form.validate():
        title = form.title.data
        details = form.details.data
        # adding a new recipe to storage
        new_recipe = recipes_models.Recipe(title, details)
        new_recipe.create_recipe()
        return redirect(url_for('dashboard'))

    return render_template('create_recipe.html', form=form)


# Update Created Recipe
@app.route('/update_recipe/<string:title>', methods=['GET', 'POST'])
def update_recipe():
    """intialize recipe update"""
    form = RecipeForm(request.form)

    #fill the form with recipe details
    form.title.data = Recipes_['title']
    form.details.data = Recipes_['details']


    if request.method == 'POST' and form.validate():
        title = request.form['title']
        details = request.form['details']

        updated_recipe = recipes_models.Recipe(title, details)
        updated_recipe = update_recipe()

        return redirect(url_for('dashboard'))

    return render_template('update_recipe.html', form=form)

# Delete Recipe
@app.route('/delete_recipe/<string:title>', methods=['POST'])
def delete_recipe(title):
    """intialize delete a recipe"""
    if request.method == 'POST':
        recipe = recipes_models.Recipe()
        recipe.delete_recipe(title)

        
        
        return redirect(url_for('dashboard'))


if __name__ == '__main__':
    app.run(debug=True)
