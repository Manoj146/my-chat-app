from django.urls import re_path
from .consumers import ChatConsumer

wsPattern = [
    re_path(r'ws/messages/(?P<room_name>\w+)/$', ChatConsumer.as_asgi()),
]