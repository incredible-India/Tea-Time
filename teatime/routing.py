from django.urls import path  
from teatime.consumer import myConsumer
ws = [
    path('ws/teatime/',myConsumer.as_asgi())
]