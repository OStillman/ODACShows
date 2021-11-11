import requests

class GetChannelLogos():
    def __init__(self, channels_added):
        self.channels_added = channels_added

    def retrieveLogos(self):
        for channel in self.channels_added:
            directory = "static/img/channel_logos/" + str(channel["row_id"])
            url = channel["logourl"]

            filename = "static/img/channel_logos/" + str(channel["row_id"]) + "." + url.split(".")[-1]
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)