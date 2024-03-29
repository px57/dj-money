from django.db import models
from django.forms.models import model_to_dict
from django.conf import settings

from datetime import timedelta

from gpm.models.base_metadata_model import BaseMetadataModel

from profiles.models import Profile

from money.rules.stack import MONEY_RULESTACK

import json

def convert_to_decimal(value):
    return value / 1000


class Price(BaseMetadataModel):
    """
    The price model.
    """
    price = models.PositiveBigIntegerField(
        default=0,
    )

    currency = models.CharField(
        max_length=100,
        default=settings.MONEY_DEFAULT_CURRENCY,
        choices=settings.MONEY_LIST_CURRENCY,
    )

    @property
    def decimal_price(self):
        return convert_to_decimal(self.price)

class BankAccountModels(BaseMetadataModel):
    """
    @description:
    """

    profile = models.ForeignKey(
        Profile,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    account_name = models.CharField(
        max_length=100, 
        default=""
    )

    bankNumberType = models.CharField(
        max_length=100,
        choices=(
            ("us", "Numéro de compte us"),
            ("iban", "Numéro de compte iban"),
            ('transferwise', 'Numéro de compte transferwise'),
        ),
        default="us",
    )

    # DOC: Il s'agit ici du numéro de bank
    jsonBankNumber = models.CharField(
        max_length=1000,
        default="""
            {
                "routing_number": "",
                "account_number": ""
            }
        """,
    )

    status = models.CharField(
        max_length=50,
        default="empty",
        choices=(
            ("empty", "empty"),
            ("new", "new"),
            # DOC: Lorsque l'utilisateurs arrive à ce niveaux
            ("proof_of_identity", "proof_of_identity"),
            ("video_verification", "video_verification"),
            # DOC: Indique que ça été valider par u=l'un de nos gars
            ("usable", "usable"),
        ),
    )

    password_front = models.ImageField(
        "password_front",
        upload_to="profile/%Y/%m/%d/",
        default="assets/img/user1.jpg",
    )

    passport_back = models.ImageField(
        "passport_back",
        upload_to="profile/%Y/%m/%d/",
        default="assets/img/user1.jpg",
    )

    video_verification = models.ImageField(
        "passport_back",
        upload_to="profile/%Y/%m/%d/",
        default="assets/img/user1.jpg",
    )

    adress = models.CharField(max_length=100, default="")

    postal_code = models.CharField(max_length=100, default="")

    country = models.CharField(max_length=100, default="")

    city = models.CharField(max_length=100, default="")

    def serialize(self, request):
        """Chargée ces données pour les faires remonter."""
        serialized = model_to_dict(self)
        serialized["jsonBankNumber"] = json.loads(serialized.get("jsonBankNumber"))
        del serialized["password_front"]
        del serialized["passport_back"]
        del serialized["video_verification"]
        return serialized



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

    interface = models.CharField(
        max_length=100,
        help_text="The interface to manage the subscription.",
        choices=MONEY_RULESTACK.models_choices(),
        null=True,
        blank=True,
    )

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
        blank=True,
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

    def serialize(self, request):
        """
        Is used to serialize the object.
        """
        serialized = model_to_dict(self)
        serialized["source"] = self.source.serialize(request)
        serialized["destination"] = self.destination.serialize(request)
        return serialized
    
    class Meta:
        verbose_name = "Transfert"
        verbose_name_plural = "Transferts"

class SubscriptionTemplate(BaseMetadataModel):
    """
    Subscription model, to store the subscription.
    """
    interface = models.CharField(
        max_length=100,
        help_text="The interface to manage the subscription.",
        choices=MONEY_RULESTACK.models_choices(),
        null=True,
        blank=True,
    )

    description = models.TextField(
        help_text="The description of the subscription",
        null=True,
        blank=True,
    )

    price = models.ForeignKey(
        Price,
        on_delete=models.CASCADE,
        help_text="The price of the subscription",
        related_name='subscription_price',
        null=True,
        blank=True,
    )

    timdelta_type = models.CharField(
        max_length=100,
        default="day",
        help_text="The duration type of the subscription.",
        choices=(
            ("day", "day"),
            ("week", "week"),
            ("month", "month"),
            ("year", "year"),
        ),
    )

    timdelta_number = models.PositiveBigIntegerField(
        default=0,
        help_text="The number of day, week, month or year.",
    )

    @property
    def timedelta(self):
        return timedelta(
            **{self.timdelta_type: self.timdelta_number}
        )
    
class Subscription(BaseMetadataModel):
    """
    Subscription model, to store the subscription.
    """
    interface = models.CharField(
        max_length=100,
        help_text="The interface to manage the subscription.",
        choices=MONEY_RULESTACK.models_choices(),
        null=True,
        blank=True,
    )

    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='profile',
        help_text="The profile",
        null=True,
        blank=True,
    )

    template = models.ForeignKey(
        SubscriptionTemplate,
        on_delete=models.CASCADE,
        related_name='template',
        help_text="The subscription template",
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=100,
        default="active",
        help_text="The status of the subscription",
        choices=(
            ("active", "active"),
            ('pending', 'pending'),
            ("inactive", "inactive"),
        ),
    )

    begin_date = models.DateTimeField(
        null=True,
        help_text="Begin date of the subscription",
        auto_now=False,
    )

    end_date = models.DateTimeField(
        null=True,
        help_text="End date of the subscription",
        auto_now=False,
    )