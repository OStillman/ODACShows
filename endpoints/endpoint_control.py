from flask import render_template, request
import json
from flask import Blueprint

endpoint_control = Blueprint('endpoint_control', __name__)

@endpoint_control.route('/')
def index():
    return "Hello"