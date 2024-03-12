"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views


urlpatterns = [
    path(
        "unsubscribe/", 
        views.unsubscribe, 
        name="unsubscribe"
    ),
    path(
        "subscribe/", 
        views.subscribe, 
        name="subscribe"
    ),
    path(
        "info/", 
        views.info, 
        name="info"
    ),
]
