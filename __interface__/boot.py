

from boot.rules.stack import BOOT_RULESTACK
from boot.rules.default_boot import DefaultRuleClass

class MoneyBoot(DefaultRuleClass):
    """

    """
    label = 'MONEY_BOOT'

    def gpm_run(self, *args, **kwargs):
        """
        Is fonction to run the money boot.
        """
        res = kwargs.get('res', None)
        request = res.get_request()
        
        # if not res.is_authenticated():
        #     return
        
        res.money = {
            'balance': {
                'currency': 'USD',
                'balance': 0,
            },
        }
        # -> load the service to get the balance

BOOT_RULESTACK.set_rule(MoneyBoot)