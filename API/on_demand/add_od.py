from API.validation import add_od_validation as input_validation
from database.API import on_demand as od
from database.validation import od_channel_validation

class AddOD():
    def __init__(self, show_data):
        self.show_data = show_data

    def add_show(self):
        print(self.show_data)
        checkJSON_outcome = self.checkJSON()
        if checkJSON_outcome == True:
            check_channel_outcome = self.checkChannel()
            if check_channel_outcome == True:
                self.addODShow()
            return check_channel_outcome
            
        else:
            print(checkJSON_outcome)
            return checkJSON_outcome

    def checkJSON(self):
        validation = input_validation.Validate_AddOD(self.show_data)
        return validation.validate_data()

    def checkChannel(self):
        # TODO: Invoke Channel Check to ensure it's an OD Channel, or that it exists in the DB - use od_channel_validation
        # Get channel number, search for it in the DB - does it exist? Yes - is it OD? Live/Non-Existent report back to user
        chosen_channel = self.show_data["service"]
        ODChannelValidation = od_channel_validation.ODChannelValidation(chosen_channel)
        return ODChannelValidation.run_checks()


    def addODShow(self):
       AddODShow = od.AddODShow(self.show_data)
       AddODShow.ExecuteAdd()