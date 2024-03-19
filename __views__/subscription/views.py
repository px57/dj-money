

from kernel.http import load_response

from profiles.decorators import load_profile

from money.rules.stack import MONEY_RULESTACK
from money.models import Subscription

@load_response(
    stack=MONEY_RULESTACK,
    json=True,
    load_params=True,
)
@load_profile
def unsubscribe(
    request, 
    res=None,
    **kwargs, 
):
    """
    Unsubscribe from the subscription
    """
    return res.success()

@load_response(
    stack=MONEY_RULESTACK,
    json=True,
    load_params=True,
)
@load_profile
def subscribe(
    request, 
    res=None,
    **kwargs,
):
    """
    Subscribe to the subscription
    """
    return res.success()

@load_response(
    stack=MONEY_RULESTACK,
    json=True,
    load_params=True,
)
@load_profile
def info(
    request, 
    res=None,
    _in=None,
    **kwargs,
):
    """
    Get the subscription info
    """
    res.subscription_list = []

    for subscription in Subscription.objects.filter(
        profile=request.profile, 
        interface=_in.label
    ):
        res.subscription_list.append(subscription.serialize(request))
    return res.success()

