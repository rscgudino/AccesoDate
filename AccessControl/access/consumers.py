import json
from channels.generic.websocket import AsyncWebsocketConsumer

class AccessLogConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("access_logs", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("access_logs", self.channel_name)

    async def receive(self, text_data):
        pass

    async def access_log_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
