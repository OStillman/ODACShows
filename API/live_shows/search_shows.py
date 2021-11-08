from API.validation import search_live_show_validation as validate
import datetime

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
            pass
        else:
            failure = True
            failure_msg = date[1]

        if failure:
            return [400, {"Error" : {"Message": failure_msg}}]
        else:
            return [200, ""]

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

    def convertDate(self, date):
        try:
            return [True, datetime.date(int(date[2]), int(date[1]), int(date[0]))]
        except (ValueError, IndexError) as Error:
            if (str(Error) == "list index out of range"):
                return [False, "Date is of incorrect Format. Please Ensure it's DD/MM/YYYY"]
            return [False, str(Error)]