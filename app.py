from json import load
import string
from flask import Flask, render_template, redirect, url_for,request, send_file, session
from flask.sessions import NullSession
from flask_bootstrap import Bootstrap
from flask.sessions import NullSession
import time
from jinja2 import pass_eval_context

import threading
import random
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'ghghchgcghchhddgdgf'

# @app.before_first_request
# def before_first_request():
#     threading.Thread(target=update_load()).start()

# def update_load():
#     with app.app_context():
#         while True:
#             time.sleep(5)
#             print(load)
#             render_template('index.html',load=load)
#             # turbo.push(turbo.replace(render_template('load.html'), load = 'load'))


# @app.context_processor
# def inject_load():
    
#     load = [int(random.random() * 100) / 100 for _ in range(1)]
    
#     return {'load': load[0]}


@app.route("/", methods =["GET", "POST"])
def index():
    tmp_set=0
    temperature_set= 0
    if request.method == "POST":
        tmp_set = request.form.get("temp")
      
        if request.form.get('action1') == 'Submit':

            if tmp_set == "":
                tmp_set=30
            temperature_set = int(tmp_set)
        
            return render_template('index.html', value=temperature_set)
        if request.form.get('action2') == 'New user':
            return redirect(url_for("add_user"))
        

        
    return render_template('index.html', value=temperature_set)


@app.route("/add_user", methods =["GET", "POST"])
def add_user():
    print("adding user started")
    print(request.method)
    if request.method == "POST":
     
        if request.form.get('action1') == 'Capture':
            name = request.form.get("Name")
            print("here",name)
            session["name"] = name
            print(session["name"])
            return redirect(url_for("capture"))
        if request.form.get('action3') == 'Back':
           return redirect(url_for("index"))
    else:
        return render_template('load.html')




@app.route("/capture/", methods =["GET", "POST"])
def capture():
    print("i m here",session["name"])
    if request.method == "POST":

        if request.form.get('action2') == 'Start Capture':
            print("capture Started")
            return redirect(url_for("index"))
        if request.form.get('action3') == 'Back':
            return redirect(url_for("add_user"))
    else:
        return render_template('capture.html',value = session["name"]) 

if __name__ == '__main__':
    app.config['SERVER_NAME'] = "127.0.0.1:2000"
  
    app.run(debug=True)