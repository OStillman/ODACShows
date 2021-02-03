from flask import render_template, request
import json
from flask import Blueprint
import sys 

from Backend import todayOutput
from Backend import allShows
from Backend import searchDetails
from Backend import searchShows
from Backend import db as ShowsDB
from Backend import onToday

endpoint_control = Blueprint('endpoint_control', __name__)

@endpoint_control.route('/')
def index():
    # Today
    TodayOutput = todayOutput.TodayOutput()
    today_shows = TodayOutput.today

    #Fetch On Demand Shows
    all_od_shows = allShows.GetAllODShows().retrieveShows()
    
    #Fetch Live Showa
    all_live_shows = allShows.GetAllLiveShows().retrieveShows()

    # Fetch all Tags
    FetchTags = ShowsDB.FetchTags()
    all_tags = FetchTags.tags

    print(today_shows, file=sys.stderr)
    print(all_tags, file=sys.stderr)

    return render_template('index.html', live_shows=all_live_shows, today_shows=today_shows, tags=all_tags, od_shows=all_od_shows)

@endpoint_control.route('/add', methods=['GET', 'POST'])
def add_shows():
    if request.method == 'GET':
        FetchTags = ShowsDB.FetchTags()
        all_tags = FetchTags.tags

        # Channels
        FetchChannels = ShowsDB.FetchChannels()
        all_channels = FetchChannels.channels

        print(all_channels, file=sys.stderr)
        
        #data = getJSON.get_file("show_tags")
        return render_template('add.html', data=all_tags, channels=all_channels)
    else:
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        '''tags = False
        if len(data['tags']) > 0 or data['tags'] is not 'N/A':
            tags = True

        db.AddShow(data, tags)'''
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}

@endpoint_control.route('/live/search', methods=['POST'])
def showsSearch():
    data = request.get_json(force=True)
    print(data, file=sys.stderr)
    SearchShow = searchShows.SearchShow(data['service'], data['offset'])
    show_times = SearchShow.search(data['title'])
    print(show_times)
    return json.dumps(show_times), 200, {'ContentType': 'application/json'}

@endpoint_control.route('/live', methods=['POST', 'DELETE'])
def liveAdd():
    if request.method == "POST":
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        success = True
        try:
            found_show = searchDetails.SearchShowDetail(data["evtid"], data["service"]).show_details()
            AddLiveShow = ShowsDB.AddLiveShow(found_show)
            channel_id = AddLiveShow.fetchChannelID()
            AddLiveShow.addToDB(channel_id)
            print(found_show)
        except KeyError:
            success = False
        finally:
            if success:
                return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
            else:
                return json.dumps({'success': False}), 400, {'ContentType': 'application/json'}
    elif request.method == "DELETE":
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        ShowsDB.DeleteLiveShow(int(data['element']))
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}


@endpoint_control.route('/live/today')
def showsLiveToday():
    onToday.OnTodayController()
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@endpoint_control.route("/od", methods=['POST', 'PUT', 'DELETE'])
def odAdd():
    if request.method == "POST":
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        ShowsDB.AddODShow(data)
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    elif request.method == "PUT":
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        ShowsDB.UpdateODProgress(data)
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}
    else:
        data = request.get_json(force=True)
        print(data, file=sys.stderr)
        ShowsDB.DeleteODShow(int(data['element']))
        return json.dumps({'success': True}), 201, {'ContentType': 'application/json'}