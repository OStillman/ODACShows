import urllib.request as request
import urllib.parse as parse
import json

class RequestAllChannels():
    def __init__(self):
        self.full_url = "https://www.freesat.co.uk/tv-guide/api/"

    def request(self):
        req = request.Request(url=self.full_url, method='GET')
        request.urlopen(req)
        # We need to format the response so it's usable
        #print(request.urlopen(req).read().decode('utf-8'))
        request_output = request.urlopen(req).read().decode('utf-8')
        return json.loads(request_output)