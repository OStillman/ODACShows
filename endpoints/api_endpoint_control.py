from flask import render_template, request
import json
from flask import Blueprint

from API.on_demand import add_od
from API.on_demand import get_od

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
            response_error_msg = add_show_outcome[1]
            response_error_code = add_show_outcome[0]
            return (response_error_msg, response_error_code)
    elif request.method == "GET":
        response = ["", 200]
        searched_show = request.args.get("show")
        if searched_show:
            print("Specific Show Requested")
        else:
            RetrieveAllODShows = get_od.RetrieveAllShows()
            all_od_shows = RetrieveAllODShows.run_retrieval()
            response[0] = all_od_shows
        return response[0], response[1]

