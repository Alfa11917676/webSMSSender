from flask import Flask, render_template, request
from flask.wrappers import Request
import pyrebase
import json


app = Flask(__name__)
config = {
    'apiKey': "AIzaSyAkTRKdJ9IdhAhDBvF200bpM_D6VUYC5Tg",
    'authDomain': "messageapp-67fc1.firebaseapp.com",
    'databaseURL': "https://messageapp-67fc1-default-rtdb.firebaseio.com",
    'projectId': "messageapp-67fc1",
    'storageBucket': "messageapp-67fc1.appspot.com",
    'messagingSenderId': "253214828846",
    'appId': "1:253214828846:web:b84582bc6d106e351732bf",
    'measurementId': "G-JMBJS6NT9F"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()


@app.route("/")
def mainPage():
    return render_template("index.html")


@app.route("/authenticate", methods=['GET', 'POST'])
def authen():
    try:
        if request.method == 'POST':
            email = request.form['s_email']
            password = request.form['s_pass']
            new_user = auth.create_user_with_email_and_password(email, password)
            auth.send_email_verification(new_user['idToken'])
        
    except:
        if request.method == 'POST':
            email = request.form['l_email']
            password = request.form['l_pass']
            login_user = auth.sign_in_with_email_and_password(email, password)

    return render_template('auth.html')


if __name__ == "__main__":
    app.run(debug=True, port=8000)
