from django.db import models
from kernel.models.base_metadata_model import BaseMetadataModel
from profiles.models import Profile


def convert_to_decimal(value):
    return value / 1000

class Account(BaseMetadataModel):
    """
        @description: 
    """
    # -> Le solde du compte.
    balance = models.PositiveBigIntegerField(default=0)

    # -> Le proprietaire du compte.
    owner = models.ForeignKey(
        Profile, 
        on_delete=models.CASCADE, 
        related_name='owner',
        unique=True
    )

    # -> Le solde du compte, qui ne peut etre retire.
    gift_balance = models.PositiveBigIntegerField(default=0)

    def total_balance(self):
        return self.balance + self.gift_balance
    
    def decimal_gift_balance(self):
        return convert_to_decimal(self.gift_balance)
    
    def decimal_balance(self):
        return convert_to_decimal(self.balance)

    def decimal_total_balance(self):
        return convert_to_decimal(self.total_balance())
    
    class Meta:
        verbose_name = "Compte"
        verbose_name_plural = "Comptes"

class TransfertModels(BaseMetadataModel):
    """
        @description: 
    """
    # -> Type comptable.
    accounting_type = models.CharField(
        max_length=255,
        choices=(
            # -> Ici il s'agit de l'argent que l'utilisateur recoit.
            ('debit', 'debit'),

            # -> Ici il s'agit de l'argent que l'utilisateur envoi.
            ('credit', 'credit')
    ))

    # -> Le montant du transfert.
    amount = models.PositiveIntegerField(default=0)

    # -> Montant cadeaux. (non retirables).
    gift_amount = models.PositiveIntegerField(default=0)

    # -> Le type de transfert.
    type = models.CharField(
        max_length=255, 
        choices=(
            # -> Ici il s'agit de l'argent que l'utilisateur a jouer
            ('playroom_playdraw', 'playroom_playdraw'),
            ('playroom_win', 'playroom_win'),
            ('deposit', 'deposit'),
            ('withdraw', 'withdraw'),
            ('transfer', 'transfer'),
            ('bonus', 'bonus')
    ))

    # -> Le compte d'origine.
    source = models.ForeignKey(
        'Account', 
        on_delete=models.CASCADE, 
        related_name='source',
        null=True,
        blank=True
    )

    # -> Le compte de destination.
    destination = models.ForeignKey(
        'Account', 
        on_delete=models.CASCADE, 
        related_name='destination',
        null=True,
        blank=True
    )


    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "Transfert"
        verbose_name_plural = "Transferts"    
