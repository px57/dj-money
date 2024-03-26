
from money import models as money_models


def account_exist(dbProfile):
    """
        @description: 
    """
    return money_models.Account.objects.filter(
        owner=dbProfile
    ).exists()

def get_or_create_account(dbProfile):
    """
        @description: 
    """
    dbAccount = money_models.Account.objects.filter(
        owner=dbProfile
    )
    if dbAccount.exists():
        return dbAccount.first()
    
    dbAccount = money_models.Account(
        owner=dbProfile
    )
    dbAccount.save()
    return dbAccount


def spend(dbAccount, value):
    """
        @description: Depenser de l'argent et realiser les differentes operations.
    """
    # TODO: plus tard verifier que l'ont peut debloquer cette somme.

    # -> use git balance or normal balance ?
    use_gift_balance = dbAccount.gift_balance > value
    if use_gift_balance:
        gift_amount = value
        amount = 0
    else:
        amount = value
        gift_amount = 0

    # -> Create the transfert.
    dbTransfert = money_models.TransfertModels(
        source=dbAccount,
        amount=amount,
        gift_amount=gift_amount,
        type='out'
    )
    dbTransfert.save()
    # -> Finalise the transfert discount.
    if use_gift_balance:
        dbAccount.gift_balance -= value
    else: 
        dbAccount.balance -= value
    dbAccount.save()
    return dbTransfert


def add_money(dbProfile, reason='???', amount=0): 
    """
        @description: 
    """
    dbAccount = get_or_create_account(dbProfile)
    dbAccount.balance += amount
    dbAccount.save()
    return dbAccount