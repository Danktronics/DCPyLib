#should only work on Python 3.x
import json
import urllib.request
endpointJSON = urllib.request.urlopen("http://chat.danktronics.org/api/v1/gateway/endpoint").read()
endpointURL = json.load(endpointJSON)
print endpointURL["url"]