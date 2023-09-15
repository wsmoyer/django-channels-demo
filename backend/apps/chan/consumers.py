# chat/consumers.py
import json
from asgiref.sync import async_to_sync, sync_to_async

from channels.generic.websocket import WebsocketConsumer
from django.template.loader import render_to_string
from .models import FavoriteAnimal
from .views import show_chart, save_fav_animal

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'joke'
        self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['animal_choice']
        save_fav_animal(message)
        vals = show_chart('blue')
        html =  render_to_string('chart.html', {'script': vals['script'], 'div': vals['div']})
        self.send(text_data=html)

    def send_joke(self, text_data):
        
        print('recievd')        
     