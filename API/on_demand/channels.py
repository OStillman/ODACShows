from database.API import channels


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

