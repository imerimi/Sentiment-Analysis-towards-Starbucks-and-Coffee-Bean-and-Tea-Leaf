### Second Flask application - Dynamic HTMl in templates###
from flask import Flask, render_template
import os 


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, 'static')
FILES_STATIC = os.path.join(APP_STATIC, 'files')


@app.route('/')
def index():
    # store under templates folder
    return render_template("index.html")

