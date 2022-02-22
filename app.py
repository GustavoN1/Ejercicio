from flask import Flask, render_template, request, redirect
from flask.helpers import url_for
from db import db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html", data=db)
    
@app.route('/update<name>', methods=["GET","POST"])
def update(name):
    if request.method == "GET":
        return render_template("update.html", name=name)
    elif request.method == "POST":
        print("Funciona")
        n_nombre = request.form.get("name")
        db[1]["nombre"] = n_nombre
        return redirect(url_for("home"))
    

if __name__ == '__main__':
    app.run(debug=True)
    
    
    