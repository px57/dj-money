
from kernel.http import load_response

from money.rules.stack import MONEY_RULESTACK

@load_response(stack=MONEY_RULESTACK)
def unsubscribe(request, res=None):
    """
    Unsubscribe from the subscription
    """
    return res.success()

@load_response(stack=MONEY_RULESTACK)
def subscribe(request, res=None):
    """
    Subscribe to the subscription
    """
    return res.success()

@load_response(stack=MONEY_RULESTACK)
def info(request, res=None):
    """
    Get the subscription info
    """
    return res.success()