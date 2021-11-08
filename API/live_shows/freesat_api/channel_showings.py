import urllib.request as request
import urllib.parse as parse
import json

class RequestShowings():
    def __init__(self, offset, channel_id):
        self.base_url = "https://www.freesat.co.uk/tv-guide/api/"
        self.offset = offset
        self.channel_id = channel_id

    def createURL(self):
        self.full_url = "{}{}?channel={}".format(self.base_url, self.offset, self.channel_id)
        print(self.full_url)

    def request(self):
        req = request.Request(url=self.full_url, method='GET')
        request.urlopen(req)
        # We need to format the response so it's usable
        #print(request.urlopen(req).read().decode('utf-8'))
        request_output = request.urlopen(req).read().decode('utf-8')
        return json.loads(request_output)