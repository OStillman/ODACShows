from flask import render_template, request
import json
from flask import Blueprint

from API.on_demand import add_od
from API.on_demand import get_od
from API.on_demand import delete_od
from API.on_demand import channels as api_channels

from API.live_shows import search_shows

api_endpoint_control = Blueprint('api_endpoint_control', __name__)

@api_endpoint_control.route('/')
def index():
    return "ok"

@api_endpoint_control.route('/channels', methods=['GET', 'POST'])
def channels():
    #TODO: See Github for adding catch for only Live channel Retrieval
    response = ["", 200]
    if request.method == "GET":
        AllChannels =  api_channels.GetAllChannels()
        retrieved_channels = AllChannels.Retrieve()
        print(retrieved_channels)
        response[0] = (retrieved_channels)
    elif request.method == "POST":
        incorrect_request_data = False
        try:
            request_data = request.get_json(force=True)
        except:
            incorrect_request_data = True
            response[0] = {"Error" : {"Message": "No Channel or Service data supplied for addition"}}
            response[1] = 400
        finally:
            if not incorrect_request_data:
                print("Request data exists")
                AddChannel = api_channels.AddChannel(request_data)
                channel_add_status = AddChannel.Add()
                print(channel_add_status)
                if channel_add_status[0] == True:
                    if channel_add_status[1] == True:
                        response[1] = 201
                    else:
                        response[1] = 400
                        response[0] = {"Error" : {"Message": channel_add_status[2]}}
                else:
                    response[1] = 400
                    response[0] = json.loads(channel_add_status[0])
    return response[0], response[1]


@api_endpoint_control.route('/live/search', methods=["GET"])
def liveShows():
    response = ["", 200]
    if request.method == "GET":
        print("Recieved post...")
        incorrect_request_data = False
        try:
            request_data = request.get_json(force=True)
        except:
            incorrect_request_data = True
            response[0] = {"Error" : {"Message": "No Show data supplied for searching"}}
            response[1] = 400
        finally:
            if not incorrect_request_data:
                print("Data has Passed, continue")
                SearchShow = search_shows.SearchShow(request_data)
                check_format = SearchShow.checkFormat()
                if check_format == True:
                    print("Checks Passed")
                    show_search = SearchShow.searchShow()
                    response[1] = show_search[0]
                    response[0] = show_search[1]
                else:
                    response[0] = json.loads(check_format[0])
                
    else:
        response[1] = 501
    return response[0], response[1]

# User Navigates to /ODAC/shows/api/od
@api_endpoint_control.route('/od', methods=['GET', 'POST', 'DELETE'])
def on_demand():
    # If user request is a POSt - we are adding a new show to On Demand Shows
    response = ["", 200]
    if request.method ==  "POST":
        # Retrieve the JSON Request Data
        incorrect_request_data = False
        try:
            request_data = request.get_json(force=True)
        except:
            incorrect_request_data = True
            response[0] = {"Error" : {"Message": "No Show data supplied for addition"}}
            response[1] = 400
        finally:
            if not incorrect_request_data:
            # Send to ADDOD API Method
                AddOD = add_od.AddOD(request_data)
                # Attempt to add the show
                add_show_outcome = AddOD.add_show()
                if add_show_outcome == True:
                    response[1] = 201
                else:
                    print(add_show_outcome)
                    response[1] = add_show_outcome[1]
                    response[0] = json.loads(add_show_outcome[0])
    elif request.method == "GET":
        response = ["", 200]
        searched_show = request.args.get("show")
        if searched_show:
            RetrieveSpecificShow = get_od.RetrieveSpecificShow(searched_show)
            requested_show = RetrieveSpecificShow.fetch_show()
            response[0] = requested_show
        else:
            RetrieveAllODShows = get_od.RetrieveAllShows()
            all_od_shows = RetrieveAllODShows.run_retrieval()
            response[0] = all_od_shows
    elif request.method == "DELETE":
        response = ["", 200]
        identified_show = request.args.get("show")
        if identified_show:
            print("Show requested")
            DeleteODShow = delete_od.DeleteODShow(identified_show)
            deletion_status = DeleteODShow.run_deletion()
            if deletion_status[0]:
                response[1] = 204
            else:
                response[1] = 400
                response[0] = {"Error" : {"Message": deletion_status[1]}}
        else:
            response[0] = {"Error" : {"Message": "No Show ID Supplied for deletion"}}
            response[1] = 400
    return response[0], response[1]

