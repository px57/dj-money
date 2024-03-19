from django.contrib import admin

from money.models import Account
from money.models import TransfertModels
from money.models import BankAccountModels 
from money.models import SubscriptionTemplate
from money.models import Subscription

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [
        'owner',

    ]

@admin.register(TransfertModels)
class TransfertModelsAdmin(admin.ModelAdmin):
    list_display = [
        # 'sender',
        # 'receiver',
        # 'value',
        # 'date',
        # 'status',
    ]


@admin.register(BankAccountModels)
class BankAccountModelsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "profile",
        "account_name",
        "bankNumberType",
        "jsonBankNumber",
        "status",
    ]
    list_filter = []

@admin.register(SubscriptionTemplate)
class SubscriptionTemplateAdmin(admin.ModelAdmin):
    list_display = [
        # "id",
        # "name",
        # "description",
        # "price",
        # "currency",
        # "status",
    ]
    list_filter = []

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = [
        # "id",
        # # "profile",
        # "subscriptionTemplate",
        # "status",
    ]
    list_filter = []