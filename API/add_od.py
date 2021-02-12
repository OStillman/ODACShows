from API.validation import add_od_validation as input_validation
from API.db import od

class AddOD():
    def __init__(self, show_data):
        self.show_data = show_data

    def add_show(self):
        print(self.show_data)
        checkJSON_outcome = self.checkJSON()
        if checkJSON_outcome == True:
            #self.addODShow()
            return True
        else:
            print(checkJSON_outcome)
            return checkJSON_outcome

    def checkJSON(self):
        validation = input_validation.Validate_AddOD(self.show_data)
        return validation.validate_data()

    def addODShow(self):
        AddODShow = od.AddODShow(self.show_data)
        AddODShow.add_od_show()