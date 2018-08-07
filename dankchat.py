import json
import urllib.request
endpointJSON = urllib.request.urlopen("http://chat.danktronics.org/api/v1/gateway/endpoint").read()