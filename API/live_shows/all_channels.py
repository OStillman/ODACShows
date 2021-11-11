from API.live_shows.freesat_api import all_channels as retrieve_channels

from database.API import channels

class ConfigureAllChannels():
    def __init__(self):
        # Retrieve all channels from Freesat's API
        # Run a check on the DB - does it already exist? - Will need to run this check on Name, Location, id
        # If no, add
        # If yes, check the channelID, channel name etc.
        self.RequestAllChannels = retrieve_channels.RequestAllChannels()
        self.AllChannels = channels.AllChannels()
        self.AddChannels = channels.AddChannels(live=True)
        self.UpdateChannel = channels.UpdateChannel()

    def processChannels(self):
        all_channels = self.RequestAllChannels.request()
        #print(all_channels)
        main_details = []
        for channel in all_channels:
            main_details.append(self.channelMainDetails(channel))
        current_channels = self.getCurrentLiveChannels()
        if current_channels[0] == False:
            for channel in main_details:
                self.addChannel(channel)
            self.AddChannels.commitAndClose()
        else:
            updates_required = []
            for channel in main_details:
                comparison_outcome = self.compareChannels(current_channels[1], channel)
                if comparison_outcome[0] == True and comparison_outcome[1] == "N":
                    # This is a new channel, so we can add it straight away:
                    self.addChannel(channel)
                if comparison_outcome[0] == True and comparison_outcome[1] == "A":
                    # This channel exists, but it needs to be updated
                    updates_required.append([channel["channelId"], comparison_outcome[2]])
            self.AddChannels.commitAndClose()
            self.runUpdates(updates_required)

    def channelMainDetails(self, channel):
        # Keeping the description as a comparison method - HD channels have the same description!
        details = {
            "channelId": channel["channelid"],
            "channelName": channel["channelname"],
            "location": channel["lcn"],
            "description": channel["channeldescription"]
        }
        return details


    def compareChannels(self, current_channels, this_channel):
        update_required = False
        new_channel = False
        update_id = -1
        for channel in current_channels:
            channel_name = channel["name"]
            channel_number = channel["number"]
            this_channel_name = this_channel["channelName"]
            this_channel_number = this_channel["channelId"]
            if channel_name == this_channel_name:
                print("Found a channel we already have")
                new_channel = False
                if int(channel_number) == int(this_channel_number):
                    print("And the channel number is the same")
                    update_required = False
                    break
                else:
                    print("But the channel number is different...")
                    update_required = True
                    update_id = channel["id"]
                    break
            else:
                new_channel = True
        
        if new_channel:
            print("It's a a new channel:")
            print(this_channel)
            return [True, "N"]
        elif update_required:
            print("channel needs updating")
            print(this_channel)
            return [True, "A", update_id]
        else:
            return [False, False]
            

    def getCurrentLiveChannels(self):
        current_channels = self.AllChannels.GetAllChannels(live_only=True)
        print(current_channels)
        if len(current_channels) == 0:
            return [False, current_channels]
        else:
            return [True, current_channels]

    def addChannel(self, channel_details):
        self.AddChannels.insertChannel(channel_details)

    def runUpdates(self, updates):
        for update in updates:
            print(update)
            self.UpdateChannel.run_Update(channel_new_number=update[0], channel_id=update[1])
        self.UpdateChannel.commitAndClose()