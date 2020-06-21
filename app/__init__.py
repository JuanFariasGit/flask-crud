from flask import Flask

app = Flask(__name__)
app.secret_key = b'8d8ec0785a9bf876b84884f12fdca9e5'

from app.controllers import *