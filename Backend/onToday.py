from Backend import db
from Backend import searchShows
from Backend import searchDetails
import datetime


class OnTodayController():
    def __init__(self):
        self.checkCleanupRequired()
        self.channels = OnToday().getLiveChannels()
        self.fetchShows()

    def fetchShows(self):
        for channel in self.channels:
            shows = OnToday().fetchShows(channel)
            self.searchShows(shows)

    def searchShows(self, shows):
        for show in shows:
            show_list = OnToday().searchShows(show)
            print(show_list)
            for listing in show_list:
                db.TodayShowOperations().addTodayShow(listing)

    def checkCleanupRequired(self):
        time_now = datetime.datetime.today()
        first_timeslot = time_now.replace(hour=7, minute=30, second=0)
        midnight = time_now.replace(hour=0, minute=1, second=0)
        if time_now <= first_timeslot and time_now > midnight:
            print("This is the first of the day, need to delete yesterday's first")
            db.TodayShowOperations().deleteTodayShows()
        else:
            print("It's after, continue")



class OnToday():
    def __init__(self):
        self.FetchLiveShows = db.FetchLiveShows()
        self.FetchLiveChannels = db.FetchChannels()

    def getLiveChannels(self):
        return self.FetchLiveChannels.live_channels


    def fetchShows(self, service):
        '''
        Fetch all live shows stored in the DB
        '''
        self.FetchLiveShows.service = service
        shows_output = self.FetchLiveShows.liveshowsQuery()
        return(shows_output)

    def searchShows(self, show):
        '''
        Search the Show param is on today
        Offset = 0 as we only want to search today
        Show[8] = Show's service number (according to Freesat)
        '''
        # Set up the class instance
        SearchShows = searchShows.SearchShow(offset=0, service=show[8])
        # Search on the show name
        search_results = SearchShows.search(show[1])
        # Check the EnvtID is either one of the shows, or has already passed
        if (search_results[0][0] == "Error, show not found" ):
            return []
        else:
            print("===== Show found ====")
            final_results = self.checkInitialEvtID(show, search_results)
            show_list = self.mergeResults(show, final_results)
            return show_list


    def checkInitialEvtID(self, show, results):
        '''
        We have initial eventID (Evtid) which is what the user has said "this is the first show"
        So, we need to check the show returned is, indeed, the first show they've said, or if the initial event has passed it can just be stored
        '''
        new_results = []
        show = list(show)
        show_evtid = show[6]
        initalevtpassed = show[7]
        for result in results:
            print(result)
            this_evtid = result[1]
            print(this_evtid)
            # If the initial Event has not passed, we need to do check the Event ID from freesat is the one we aren interested in
            if initalevtpassed == "N":
                if this_evtid == show_evtid:
                    # Once we've found the initial event, we can store and allow any others to be added
                    #print("Found first eventid")
                    result.append(show[3])
                    new_results.append(result)
                    initalevtpassed = "Y"
                    #Update that the initial event has now passed, ready for potentially 2 showings on one day
                    db.UpdateLiveShow(show[0]).updateDBInitialPassed()
            else:
                # Initial event ID has passed so we can append all other results
                #print("initial evtid passed")
                episodeDetail = self.checkEp(show, this_evtid, initalevtpassed, show_evtid)
                if episodeDetail[0] == True:
                    #Index 3 = duration. Some shows will have different durations...
                    result.append(episodeDetail[3])
                    new_results.append(result)
                    #Update DB to reflect our new Episode Numbers
                    db.UpdateLiveShow(show[0]).updateDBES(episodeDetail[1], episodeDetail[2])
                    #Also update the show index we locally use
                    show[4] = episodeDetail[1]
                    show[5] = episodeDetail[2]
                else:
                    print("Told to ignore")
        #print(new_results)
        return new_results

    def checkEp(self, show, evtid, initialevtpassed, show_evtid):
        '''
        If the episode looks to be good, and it isn't the first they've selected, check:
        - Is it just the next episode?
        - Is it just the next series?
        - Otherwise, we can assume it's an old episode that we don't want
        If it is ok, we need to:
        - Mark it as True (i.e. ok)
        - Send back this Ep and S number for the DB to updated
        '''
        show_ep = show[4]
        show_series = show[5]
        service = show[8]
        SearchShowDetail = searchDetails.SearchShowDetail(channel=service, evtid=evtid)
        show_detail = SearchShowDetail.show_details()
        print(show_detail)
        if int(show_ep) < int(show_detail["episodeNo"]):
            print("Show Ep is greater than episode number")
            return [True, show_detail["episodeNo"], show_detail["seriesNo"], show_detail["duration"]]
        elif int(show_series) < int(show_detail["seriesNo"]):
            print("It's a new series")
            return [True, show_detail["episodeNo"], show_detail["seriesNo"], show_detail["duration"]]
        else:
            print("It can't be the next episode, or the episode they want. Ignoring")
            return [False]


    def mergeResults(self, show, results):
        '''
        We need to prepare this to be added to the OnToday DB Table
        @Param results = [time, eventid, duration]
        @Show = [LiveShows.id, LiveShows.name, channel, duration, episodeNo, seriesNo, initialEvtid, initialEpPassed, channels.number]
        Combine showID, epoch and eventID ready for storage
        '''
        #print(show[0])
        show_list = []
        for result in results:
            # Currently, the time is in a readable format, convert that back into an epoch timestamp - aids DB sorting later on
            this_epoch = datetime.datetime.strptime(result[0], '%A %B %d, %Y %H:%M:%S').timestamp()
            show_list.append([show[0], this_epoch, result[1], result[2]])
        #print(show_list)
        return show_list
        

