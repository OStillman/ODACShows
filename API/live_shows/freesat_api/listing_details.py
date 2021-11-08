import urllib.request as request
import urllib.parse as parse
import json

class RequestListing():
    def __init__(self, channel_id, episode):
        self.base_url = "https://www.freesat.co.uk/whats/showcase/api/"
        self.episode = episode
        self.channel_id = channel_id

    def createURL(self):
        self.full_url = "{}channel/{}/episode/{}".format(self.base_url, self.channel_id, self.episode)
        print(self.full_url)

    def request(self):
        req = request.Request(url=self.full_url, method='GET')
        request.urlopen(req)
        # We need to format the response so it's usable
        #print(request.urlopen(req).read().decode('utf-8'))
        request_output = request.urlopen(req).read().decode('utf-8')
        return json.loads(request_output)