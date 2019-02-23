import websockets
import requests

class Client:
    def __init__(self, token):
        self.token = token
        self.status = "DISCONNECTED"
        self.servers = {}
        self.users = {}
        self.ws = None

    def connect(self):
        try:
            self.status = "CONNECTING"
            gatewayURL = self.getGateway()
            self.ws = websockets.connect(gatewayURL + "?token=" + self.token)
        except:
            print("An error occurred while connecting")


    def getGateway(self):
        request = requests.get("https://chat.danktronics.org/api/v1/gateway/endpoint")
        response = request.json()
        return response["url"]