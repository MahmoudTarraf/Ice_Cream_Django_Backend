import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'online'

        await self.channel_layer.group_add(self.room_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_type = text_data_json['type']
        message = text_data_json['message']

        if message_type == 'ice_cream':
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'send_ice_cream_notification',
                    'message': message
                }
            )
        elif message_type == 'offer':
            await self.channel_layer.group_send(
                self.room_name,
                {
                    'type': 'send_offer_notification',
                    'message': message
                }
            )

    async def send_ice_cream_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'type': 'ice_cream', 'message': message}))

    async def send_offer_notification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({'type': 'offer', 'message': message}))