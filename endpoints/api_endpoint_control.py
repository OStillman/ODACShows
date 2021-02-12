from flask import render_template, request
import json
from flask import Blueprint

api_endpoint_control = Blueprint('api_endpoint_control', __name__)

@api_endpoint_control.route('/')
def index():
    return "ok"

@api_endpoint_control.route('/od', methods=['GET', 'POST'])
def on_demand():
    if request.method ==  "POST":
        return '', 204
    elif request.method == "GET":
        return '', 204

