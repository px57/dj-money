
from gpm.http import load_response

from money.rules.stack import MONEY_RULESTACK


@load_response(stack=MONEY_RULESTACK)
def fetch_info(request, res=None):
    """
    @description: This function fetches the info of the user
    """
    return res.success()

@load_response(stack=MONEY_RULESTACK)
def add_bank_account(request, res=None):
    """
    @description: This function adds a bank account to the user
    """
    return res.success()