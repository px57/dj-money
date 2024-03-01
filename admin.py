from django.contrib import admin
from money.models import Account, TransfertModels, BankAccountModels

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
