"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path("bank/", include("money.__views__.bank.urls")),
    path("subscription/", include("money.__views__.subscription.urls")),
    path("card/", include("money.__views__.card.urls")),
    path("account/", include("money.__views__.card.urls")),
    path("statistic/", include("money.__views__.statistic.urls")),
]