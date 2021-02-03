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