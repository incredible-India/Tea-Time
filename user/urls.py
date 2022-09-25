from django.contrib import admin
from django.urls import path
from . import views as uv

urlpatterns = [
    path('', uv.home.as_view(),name='home'),
    path('create/account/', uv.crtaccount.as_view(),name='crtaccount'),
]
