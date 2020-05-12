from flask import Flask, render_template, url_for
from pip._vendor.urllib3 import request
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template("login.html") 

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

@app.route('/data', methods=['GET'])
def getData():
  token = request.args.get('token')
  res = 'Hello token='+token if token else "Hello"
  return res

@app.route('/data', methods=['POST'])
def addData():
  data = request.json
  res = 'Hello data='+json.dumps(data) if data else "Hello"
  return res, 201

@app.route('/data/:id', methods=['DELETE'])
def removeData(id):
  res = 'id '+id+' Deleted!'
  return res, 204

@app.route('/data/:id', methods=['UPDATE'])
def updateData(id):
  data = request.json
  res = 'id '+id
  res += ' Hello data='+json.dumps(data) if data else "Hello"
  return res, 201

if __name__ == "__main__":
    app.run(debug=True)