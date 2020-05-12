from flask import Flask, render_template, url_for, request, jsonify, make_response
import json 
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError 
from datetime import timedelta
from werkzeug.security import generate_password_hash, check_password_hash 
import uuid  
import jwt 
import datetime 
from functools import wraps

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

def token_required(f): 
    @wraps(f) 
    def decorated(*args, **kwargs): 
        token = None 

        if 'x-access-token' in request.headers: 
            token = request.headers['x-access-token']  

        if not token: 
            return jsonify({'message': 'Token is missing!'}), 401 

        try: 
            data = jwt.decode(token, app.config['SECRET_KEY']) 
            current_user = User.query.filter_by(email=data['email']).first() 
        except: 
            return jsonify({'message':'Token is invalid'}),401  
        
        return f(current_user, *args, **kwargs) 

    return decorated



@app.route("/", methods=['GET']) 
def index():
    return render_template("login.html")   

@app.route("/user",methods=['GET'])  
@token_required
def get_users(current_user): 
    users = User.query.all() 
    output = [] 

    for user in users: 
        user_data = {} 
        user_data['username'] = user.username 
        user_data['password'] = user.password 
        user_data['email'] = user.email 
        output.append(user_data) 

    return jsonify({'users': output}) 

@app.route("/user/<username>", methods=['GET']) 
@token_required  
def get_one_user(current_user,username): 

    user = User.query.filter_by(username=username).first() 

    if not user: 
        return jsonify({'message': 'No user found'}) 

    user_data = {} 
    user_data['username'] = user.username 
    user_data['password'] = user.password 
    user_data['email'] = user.email  

    return jsonify({'user':user_data}) 

@app.route('/login')   
def login(): 
    auth = request.authorization 

    if not auth or not auth.username or not auth.password: 
       return make_response('Could not verify',401,{'WWW-Authenicate': 'Basic realm="Login required!"'}) 

    user = User.query.filter_by(username=auth.username).first()  

    if not user:  
         return make_response('Could not verify',401,{'WWW-Authenicate': 'Basic realm="Login required!"'})  

    if check_password_hash(user.password,auth.password): 
        token = jwt.encode({'email':user.email,'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=30)},app.config['SECRET_KEY'])

        return jsonify({'token': token.decode('UTF-8')})

    return make_response('Could not verify',401,{'WWW-Authenicate': 'Basic realm="Login required!"'})  
        

@app.route("/user",methods=['POST'])   
@token_required
def create_user(current_user): 
    data = request.get_json() 
    
    hashed_password = generate_password_hash(data['password'], method='sha256') 
    new_user = User(username=data['username'],email=data['email'], password = hashed_password) 
    db.session.add(new_user) 
    db.session.commit()  

    return jsonify({'message': 'New user created!'})

@app.route("/signup")
def signup():
    return render_template('signup.html')

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
