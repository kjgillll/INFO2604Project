from flask import Flask, render_template, url_for, request,jsonify
from pip._vendor.urllib3 import request
import json 
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError 
from datetime import timedelta 
from werkzeug.security import generate_password_hash, check_password_hash 
import uuid

from models import db, User

''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__)
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()
db.create_all(app=app) 
''' End Boilerplate Code '''


@app.route("/", methods=['GET'])
def index():
    return render_template("login.html")  

@app.route("/user",methods=['POST']) 
def create_user(): 
    data = request.get_json() 
    
    hashed_password = generate_password_hash(data['password'], method='sha256') 
    new_user = User(id=str(uuid.uuid4()),name=data['name'],username=data['username'],email=data['email'], password = hashed_password) 
    db.session.add(new_user) 
    db.session.commit()  

    return jsonify({'message': 'New user created!'})

@app.route("/home")
def home():
    return render_template("index.html") 

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
