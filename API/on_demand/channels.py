from database.API import channels
from API.validation import add_channel_validation

class GetAllChannels():
    def __init__(self):
        pass

    def Retrieve(self):
        AllChannels = channels.AllChannels()
        return self.format(AllChannels.GetAllChannels())

    def format(self, channels):
        database_channels = {"channels": []}
        for channel in channels:
            database_channels["channels"].append(channel)
        return database_channels


class AddChannel():
    def __init__(self, channel_data):
        self.channel_data = channel_data

    def Add(self):
        validation = self.validateJSON()
        if validation == True:
            if self.channel_data["type"] == "OD":
                return self.addOD()
            elif self.channel_data["type"] == "Live":
                return self.addLive()
            else:
                return [True, False, "Type Must be OD or Live"]
        else:
            return validation

    def validateJSON(self):
        Validate_AddChannel = add_channel_validation.Validate_AddChannel(self.channel_data)
        validation = Validate_AddChannel.validate_data()
        if validation == True:
            print("Input is Clean")
            return True
        else:
            print("Input is dirty:")
            return validation

    def addOD(self):
        return [True, False, "OD Not Implemented"]

    def addLive(self):
        return [True, False, "Live TV Not Implemented"]