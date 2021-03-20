from flask import Flask

app = Flask(__name__, template_folder='views')

from src.controllers import *
from src.routes import *

def start_app():
    app.run(port = 8890, debug=True)