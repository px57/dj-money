

from django.conf import settings
from django.utils import timezone

import os

from money.rules.stack import MONEY_RULESTACK

from gpm.interfaces.interfaces import InterfaceManager

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    The label to identify the rule interface.
    """
    label = 'DEFAULT'

    # ------------------------------------------ [SERVICE] ------------------------------------------
    """
    Is the service mail to be used.
    """
    service = settings.GEO_SERVICE

    """
    The service configuration name.
    """
    service_config_name = 'GOOGLEMAP'

    """
    Settings config name.
    """
    settings_config_name = 'GEO_CONFIG_AUTHENTIFICATION_KEYS'

    """
    Service module.
    """
    service_module = 'geo.__services__'

    # ------------------------------------------ [SUBSCRIPTION] ------------------------------------------
    """
    The maximum number of subscription.

    Choices:
        (int) -> The maximum number of countries selected
        (None) -> No limit

    """
    subscription_max_number = 1

    """
    Event after create the subscription.
    """
    def event_after_create_subscription(self, dbSubscription):
        """
        Event after create the subscription.
        """
        pass

    """
    Event after delete the subscription.
    """
    def event_after_delete_subscription(self, dbSubscription):
        """
        Event after delete the subscription.
        """
        pass

MONEY_RULESTACK.set_rule(DefaultRuleClass)