from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('d', consumers.ChatConsumer.as_asgi()),
]