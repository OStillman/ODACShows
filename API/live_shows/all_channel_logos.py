import requests
import os
import glob

class GetChannelLogos():
    def __init__(self, channels_added):
        self.channels_added = channels_added

    def retrieveLogos(self):
        for channel in self.channels_added:
            url = channel["logourl"]

            filename = "static/img/channel_logos/" + str(channel["row_id"]) + "." + url.split(".")[-1]
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)

class RemoveChannelLogos():
    def __init__(self):
        self.directory = "static/img/channel_logos/*"

    def removeAllLogos(self):
        files = glob.glob(self.directory)
        for f in files:
            os.remove(f)