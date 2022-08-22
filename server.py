import datetime
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hi, Motherfuckers!"


@app.route("/status")
def status():
    return{
        'status': True,
        'name': 'VPritone Messeger',
        'time': str(datetime.now())
    }

app.run()
