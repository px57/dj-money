
from gpm.http import Response

from profiles.decorators import profile_required, load_profile

from money.rules.stack import MONEY_RULESTACK

@load_profile
@profile_required
def profit_evolution(request):
    """
    Is used to display the profit evolution.
    """
    res = Response(request=request)
    GET = request.GET

    _in = MONEY_RULESTACK.get_rule(GET.get('_in'))
    # -> We get the profit evolution.
    # -> Add the profit evolution to the response. 
    return res.success()