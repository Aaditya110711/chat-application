import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from chatapp.models import ChatMessage

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # Join Room
        await self.channel_layer.group_add(
            self.room_name,
            self.room_group_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.room_name,
            self.room_group_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_name, 
            {"type": 'chat.message', "message": message,}
        )

    # Receive message from room group
    async def chat_message(self, event):
        data = event["message"]

        respond_data = {
            'sender': data['sender'],
            'receiver': data['receiver'],
            'msg': data['message']
        }
        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": respond_data}))

    @database_sync_to_async
    def create_message(self, data):
        new_message = ChatMessage(body=data['message'], msg_sender=data['sender'], msg_receiver=data['receiver'],seen=False)
        new_message.save()  