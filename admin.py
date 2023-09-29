from django.contrib import admin
from money.models import Account, TransfertModels

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

