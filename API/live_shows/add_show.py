from API.validation import add_live_validation as validate

from API.live_shows.freesat_api import listing_details

from API.live_shows import series_logic
from API.live_shows import episode_logic

class AddLiveShow():
    def __init__(self, show_data):
        self.show_data = show_data

    def validate_show(self):
        ValidateLiveShow = validate.Validate_LiveShow(self.show_data)
        checkJSON_outcome = ValidateLiveShow.validate_data()
        if checkJSON_outcome == True:
            return True            
        else:
            print(checkJSON_outcome)
            return checkJSON_outcome

    def processNewShow(self):
        # Retrieve full show details
        # Retrieve OUR channel ID
        # Save all to our db
       show_details = self.fetchShowDetails()
       show_details = self.formatShowDetails(show_details)
       return show_details

    def fetchShowDetails(self):
        channel_id = self.show_data["svcId"]
        event_id = self.show_data["evtId"]
        RequestListing = listing_details.RequestListing(channel_id, event_id)
        RequestListing.createURL()
        request_output = RequestListing.request()
        return request_output

    def formatShowDetails(self, show_details):
        is_series = self.isSeries(show_details)
        series_number = self.getSeriesNumber(show_details, is_series)
        episode_number = self.getEpisodeNumber(show_details, is_series)
        print(series_number)
        if episode_number[0] == False:
            print("Episode Number not found, can't continue...")
            return [False, "Listing Marked as Series, but Episode Number not found. Cannot Track Effecitvely, not added"]
        else:
            formatted_details = {
                "name": self.getName(show_details),
                "svcID": self.getSvcId(show_details),
                "evtID": self.getEvtId(show_details),
                "seriesNo": series_number[0],
                "episodeNo": episode_number[0],
                "isSeries": is_series,
                "tracking_type_series": series_number[1],
                "tracking_type_episode": episode_number[1]
            }
            print(formatted_details)
            return [True, formatted_details]


    def getSeriesNumber(self, show_details, is_series):
        if is_series:
            SeriesNumber = series_logic.SeriesNumber(show_details)
            series_number = SeriesNumber.getSeriesNumber()
            return series_number
        else:
            return [-1, "N/A"]

    def getEpisodeNumber(self, show_details, is_series):
        if is_series:
            EpisodeNumber = episode_logic.EpisodeNumber(show_details)
            episode_number = EpisodeNumber.getEpisodeNumber()
            return episode_number
        else:
            return [-1, "N/A"]

    def isSeries(self, show_details):
        return show_details["series"]

    def getName(self, show_details):
        return show_details["name"]

    def getSvcId(self, show_details):
        return show_details["svcId"]

    def getEvtId(self, show_details):
        return show_details["evtId"]