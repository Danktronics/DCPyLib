# Danktronics Chat Python Library
yes

## Installation
`None. Download it yourself`

## Example

### Creating a connection and sending a message
```py
import dankchat

class dankbot(dankchat.Client):
    async def onReady(self):
        print("Ready.")
    
    async def onMessage(self, message):
        print("Received message. Content" + message.content)

client = dankbot("token")
client.connect()
```