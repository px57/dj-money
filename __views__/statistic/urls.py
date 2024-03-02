"""
    @description: This file contains the urls for the profiles app
"""

from django.urls import path
from . import views


urlpatterns = [
    path("profit_evolution/", views.profit_evolution, name="profit_evolution"),
    # path("save_account/", views.save_account, name="save_account"),
    # path("transfert/", views.transfert, name="transfert"),
    # path("bank_account/", include("money.bank_account.urls")),
    # path("promo_code_manager/", include("money.promo_code_manager.urls")),
    # path("history/", include("money.history.urls")),
    # path("stripe/", include("money.stripe.urls")),
    # path("talkto_card/", include("money.talkto_card.urls")),
]
