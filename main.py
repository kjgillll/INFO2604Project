from flask import Flask, render_template, url_for, request, jsonify, redirect
from pip._vendor.urllib3 import request
import json
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash
import uuid
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from os import environ, path

from models import db, User, Recipe, Ingredient, Step
from forms import LoginForm, SignupForm

''' Begin boilerplate code '''


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.config['SECRET_KEY'] = "MYSECRET"
    app.config['JWT_EXPIRATION_DELTA'] = timedelta(days=7)
    db.init_app(app)
    return app


app = create_app()
Bootstrap(app)

app.app_context().push()
db.create_all(app=app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
''' End Boilerplate Code '''


@app.route("/", methods=['GET', 'POST'])
def index():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=False)
                return redirect(url_for('home'))

    return render_template("login.html", form=form)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('/'))


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    signupForm = SignupForm()
    user_created = False

    if signupForm.validate_on_submit():

        hashed_password = generate_password_hash(signupForm.password.data, method='sha256')
        user = User(username=signupForm.username.data, email=signupForm.email.data,
                    password=hashed_password)
        user_created = create_user(user)

        if user_created:
            return redirect(url_for('home'))

    return render_template('signup.html', form=signupForm)


def create_user(data):
    try:
        db.session.add(data)
        db.session.commit()  # save user
    except IntegrityError:  # attempted to insert a duplicate user
        db.session.rollback()
        return False  # error

    return True


@app.route("/recipes")
def home():
    return render_template("/recipes.html")


def setIngredients(recipe, param):
    for data in param:
        ingredient = Ingredient()
        ingredient.name = data['name']
        ingredient.quantity = data['quantity']
        ingredient.type = data['type']
        db.session.add(ingredient)
        ingredient.recipe.append(recipe)


def setRecipeSteps(recipe, param):
    for step in param:
        recipeStep = Step()
        recipeStep.stepDetails = step
        db.session.add(recipeStep)
        recipeStep.recipe.append(recipe)


def generateRecipeData():
    with open('static/recipes.json') as file:
        data = json.load(file)
        for val in data:
            recipe = Recipe()
            recipe.recipe_name = val['name']
            setIngredients(recipe, val['ingredients'])
            setRecipeSteps(recipe, val['steps'])
            recipe.imageURL = val['imageURL']
            recipe.originalURL = val['originURL']
    db.session.commit()

generateRecipeData()

'''
@app.route("/home")
def home():
    return render_template("/index.html")
'''


@app.route("/veggies")
def veggies():
    return render_template("/veggies.html")


@app.route("/bakery")
def bakery():
    return render_template("/bakery.html")


@app.route("/personal")
def personal():
    return render_template("/personal.html")


@app.route("/other")
def other():
    return render_template("/other.html")


@app.route("/frozen")
def frozen():
    return render_template("/frozen.html")


@app.route("/beverages")
def beverages():
    return render_template("/beverages.html")


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True)
