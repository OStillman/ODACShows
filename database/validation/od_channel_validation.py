from database.API import channels


class ODChannelValidation():
    # Class deals with Validating Service Sent with OD Show is an On Demand Service
    def __init__(self, channel):
        self.channel = channel

    def run_checks(self):
        return self.check_exists()

    def check_exists(self):
        # First, let's run the search on the DB for the service/channel user requested
        SearchChannels = channels.SearchChannels(self.channel)
        channel_query = SearchChannels.searchChannel()
        print(channel_query)
        # If we have a query response, the service exists, but we need to check it's OD
        if channel_query:
            return(self.check_is_od(channel_query))
        else:
            # Otherwise, the channel has not yet been added in the DB and the user needs to add it before continuing
            print("Channel not found")
            return (400, "Service not found, please add the service before trying again")

    def check_is_od(self, channel_query_output):
        if(channel_query_output["type"] == "OD"):
            print("Service is OD")
            return True
        else:
            print("Service is not OD")
            return (400, "Live TV Channel Selected. Please select an On Demand Provider for this On Demand Show")