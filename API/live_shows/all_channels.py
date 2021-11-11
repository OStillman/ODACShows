from API.live_shows.freesat_api import all_channels as retrieve_channels

class ConfigureAllChannels():
    def __init__(self):
        # Retrieve all channels from Freesat's API
        # Run a check on the DB - does it already exist? - Will need to run this check on Name, Location, id
        # If no, add
        # If yes, check the channelID, channel name etc.
        self.RequestAllChannels = retrieve_channels.RequestAllChannels()

    def processChannels(self):
        all_channels = self.RequestAllChannels.request()
        print(all_channels)
        for channel in all_channels:
            main_details = self.channelMainDetails(channel)
            print(main_details)

    def channelMainDetails(self, channel):
        # Keeping the description as a comparison method - HD channels have the same description!
        details = {
            "channelId": channel["channelid"],
            "channelName": channel["channelname"],
            "location": channel["lcn"],
            "description": channel["channeldescription"]
        }
        return details