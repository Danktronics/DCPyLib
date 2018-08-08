# should only work on Python 3.x
import json
import requests
import asyncio
import ssl
import websockets
<<<<<<< HEAD
async def connect(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJEQU5LVFJPTklDU0NIQVQiLCJpZCI6MTR9.CqAQt5-2MZdeDAvFVi-imZDCMiqDRSyp2i0V58CB6No"):
	endpointJSON = requests.get("https://chat.danktronics.org/api/v1/gateway/endpoint")
	endpointURL = json.loads(endpointJSON.content.decode("utf-8"))["url"] + "?token=" + token
	print(endpointURL)
	async with websockets.connect(endpointURL, ssl = True) as chatwebsocket:
		pass

asyncio.get_event_loop().run_forever(connect())

# input("")