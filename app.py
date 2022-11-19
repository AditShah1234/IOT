from json import load
from flask import Flask, render_template, redirect, url_for,request, send_file, session
from flask.sessions import NullSession
from flask_bootstrap import Bootstrap
from flask.sessions import NullSession
import time
from jinja2 import pass_eval_context
from src.cap import extractImages
import threading
import random
from src.client_mqtt import *
from src.client import start_socket
app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'ghghchgcghchhddgdgf'

class profile():
    def __init__(self):
        self.user_name= "None"
        self.temp_set = 0
User = profile()      
def message(client, feed_id, payload):
    print(feed_id, payload)
    with app.test_request_context('/'):
        if feed_id == "Name":
            
            User.user_name = payload
        if feed_id == "Temp_set":
            User.temp_set = payload


def connected(client):
   
    print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
    client.subscribe("Temp_set")
    client.subscribe("iot.name")
def subscribe(client, userdata, mid, granted_qos):
    # This method is called when the client subscribes to a new feed.
    print('Subscribed to {0} with QoS {1}'.format("Temp_set", granted_qos[0]))
    print('Subscribed to {0} with QoS {1}'.format("iot.name", granted_qos[0]))

@app.route("/", methods =["GET", "POST"])
def index():

    temperature_set = User.temp_set
    print(temperature_set)
    if request.method == "POST":
        print("Here111111")
        
        if request.form.get('action1') == 'Submit':
            temperature_set = request.form.get("temp")
            if temperature_set == "":
                temperature_set = 30

            print(temperature_set)
            client.publish("iot.temp-set",int(temperature_set))
          
            return render_template('index.html', value={"tmp":temperature_set,"name":User.user_name})
        if request.form.get('action2') == 'New user':
            return redirect(url_for("add_user"))
        if request.form.get('action3') == 'Update':
            return redirect(url_for("update"))
         
    return render_template('index.html', value={"tmp":User.temp_set,"name":User.user_name})

@app.route("/update")
def update():
    return redirect(url_for("index"))


@app.route("/add_user", methods =["GET", "POST"])
def add_user():
    print("adding user started")
    print(request.method)
    if request.method == "POST":
     
        if request.form.get('action1') == 'Capture':
            name = request.form.get("Name")
            print(name)
            client.publish("iot.name",name)
            User.user_name = name
        
            return redirect(url_for("capture"))
        if request.form.get('action3') == 'Back':
           return redirect(url_for("index"))
    else:
        return render_template('load.html')




@app.route("/capture", methods =["GET", "POST"])
def capture():
    name = User.user_name
    print(name)
    if request.method == "POST":
         
        if request.form.get('action2') == 'Start Capture':
            print("capture Started")
            file_name = extractImages(name,20)
            print(file_name)
            out = start_socket(file_name)
            print(out)
            return redirect(url_for("index"))
        if request.form.get('action3') == 'Back':
            return redirect(url_for("add_user"))
    else:
        return render_template('capture.html',value = name) 
def mqtt():
    client.on_connect    = connected
    # client.on_disconnect = disconnected
    client.on_message    = message
    client.on_subscribe  = subscribe
    client.connect()
    client.loop_blocking()
def application():
    app.config['SERVER_NAME'] = "127.0.0.1:2000"
        
    app.run(debug=True)
if __name__ == '__main__':
    
    t1 = threading.Thread(target=mqtt)
    # t2 = threading.Thread(target=application)
 
    # starting thread 1
    t1.start()
    application()
    # starting thread 2
    # t2.start()
 
   

    