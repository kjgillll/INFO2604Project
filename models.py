from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'login'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    todos = db.relationship('Todo', backref='user', lazy=True)  # sets up a relationship to todos which references User

    def toDict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "todos": self.todos,
            "password": self.password
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(255), nullable=False)
    userid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # set userid as a foreign key to user.id
    price = db.Column(db.Float, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def toDict(self):
        return {
            'id': self.id,
            'text': self.text,
            'userid': self.userid,
            'done': self.done
        }


recipe_steps = db.table('recipe_steps',
                        db.Column('recipe_id', db.Integer, ForeignKey('recipe.recipe_id')),
                        db.Column('step_id', db.Integer, ForeignKey('step.step_id'))
                        )

ingredients = db.table('ingredients',
                       db.Column('recipe_id', db.Integer, ForeignKey('recipe.recipe_id')),
                       db.Column('ingredient_id', db.Integer, ForeignKey('ingredient.ingredient_id'))
                       )


class Recipe(db.Model):
    __tablename__ = 'recipe'
    recipe_id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(200), nullable=False)
    ingredients = db.relationship('Ingredient', secondary=ingredients, backref=db.backref('recipe', lazy='dynamic'))
    steps = db.relationship('Step', secondary=recipe_steps, backref=db.backref('recipe', lazy='dynamic'))
    imageURL = db.Column(db.String(500), nullable=False)
    originalURL = db.Column(db.String(500), nullable=False)


class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    ingredient_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(50), nullable=False, unique=True)
    ingredient_type = db.Column(db.String(50), nullable=False)


class Step(db.Model):
    __tablename__ = 'step'
    step_id = db.Column(db.Integer, primary_key=True)
    step_details = db.Column(db.String(200), nullable=False)
