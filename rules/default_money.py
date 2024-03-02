


from django.utils import timezone
import os
from money.rules.stack import MONEY_RULESTACK
from kernel.interfaces.interfaces import InterfaceManager

class DefaultRuleClass(InterfaceManager):
    """
    The default rule class. 
    """

    """
    The label to identify the rule interface.
    """
    label = 'DEFAULT'


MONEY_RULESTACK.set_rule(DefaultRuleClass())