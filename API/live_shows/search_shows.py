from API.validation import search_live_show_validation as validate

from API.live_shows.freesat_api import channel_showings

import datetime

import string

class SearchShow():
    def __init__(self, show_data):
        self.show_data = show_data

    def checkFormat(self):
        print(self.show_data)
        ValidateLiveShow = validate.Validate_LiveShow(self.show_data)
        checkJSON_outcome = ValidateLiveShow.validate_data()
        if checkJSON_outcome == True:
            return True            
        else:
            print(checkJSON_outcome)
            return checkJSON_outcome

    def searchShow(self):
        # First, get the date - How many days away is it? - No more than 7
        # THEN, search for the programme on that day
        # Return results
        failure = False
        failure_msg = ""
        date = self.transformDate(self.show_data["first_show_date"])
        if date[0]:
            date = date[1]
            channel = self.show_data["channel_id"]
            listing_details = self.searchListings(date, channel)
            if not listing_details[0]:
                failure = True
                failure_msg = listing_details[1]
            else:
                listing = self.transformResponseData(listing_details[1])
        else:
            failure = True
            failure_msg = date[1]

        if failure:
            return [400, {"Error" : {"Message": failure_msg}}]
        else:
            return [200, listing]

    def transformDate(self, date):
        print(date)
        date = date.split("/")
        todays_date = datetime.date.today()
        show_date = self.convertDate(date)
        if show_date[0] == True:
            difference = show_date[1] - todays_date
            if difference.days < 0:
                return [False, "Date must not be in the past"]
            elif difference.days > 7:
                return [False, "Date must not be more than 7 days away"]
            else:
                return [True, difference.days]
        else:
            return show_date


    def searchListings(self, date, channel):
        RequestShowings = channel_showings.RequestShowings(date, channel)
        RequestShowings.createURL()
        output = RequestShowings.request()
        match_found = False
        match_listing = None
        #print(output[0]["event"])
        search_term = self.show_data["search_term"].lower()
        for listing in output[0]["event"]:
            listing_name = listing["name"].translate(str.maketrans('', '', string.punctuation)).lower()
            if search_term in listing_name:
                print("Match found")
                match_found = True
                match_listing = listing

        if match_found:
            print(match_listing)
            return [True, match_listing]
        else:
            return [False, "No Listing Found"]


    def transformResponseData(self, listing):
        # Output back to user - Show Name, Show Time
        show_time = datetime.datetime.fromtimestamp(listing["startTime"])
        show_date = show_time.strftime("%d/%m")
        show_time = show_time.strftime("%H:%M")
        response = {"success" : {"name": listing["name"], "show_time": show_time, "show_date": show_date, "svcId": listing["svcId"], "evtId": listing["evtId"]}}
        return response


    def convertDate(self, date):
        try:
            return [True, datetime.date(int(date[2]), int(date[1]), int(date[0]))]
        except (ValueError, IndexError) as Error:
            if (str(Error) == "list index out of range"):
                return [False, "Date is of incorrect Format. Please Ensure it's DD/MM/YYYY"]
            return [False, str(Error)]