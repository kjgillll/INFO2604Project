from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
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

if __name__ == "__main__":
    app.run(debug=True)