"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views


urlpatterns = [
    path(
        "fetch_info/", 
        views.fetch_info, 
        name="money__bank__fetch_info"
    ),
    path(
        "add_bank_account/", 
        views.add_bank_account, 
        name="money__bank__add_bank_account"
    ),
]
