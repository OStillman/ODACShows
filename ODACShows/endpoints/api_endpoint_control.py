from flask import render_template, request
import json
from flask import Blueprint

from API import add_od

api_endpoint_control = Blueprint('api_endpoint_control', __name__)

@api_endpoint_control.route('/')
def index():
    return "ok"

# User Navigates to /ODAC/shows/api/od
@api_endpoint_control.route('/od', methods=['GET', 'POST'])
def on_demand():
    # If user request is a POSt - we are adding a new show to On Demand Shows
    if request.method ==  "POST":
        # Retrieve the JSON Request Data
        request_data = request.get_json(force=True)
        # Send to ADDOD API Method
        AddOD = add_od.AddOD(request_data)
        # Attempt to add the show
        add_show_outcome = AddOD.add_show()
        if add_show_outcome == True:
            return '', 201
        else:
            print(add_show_outcome)
            return add_show_outcome
    elif request.method == "GET":
        return '', 204

