from examples import custom_style_3
from PyInquirer import prompt


class BaseCommand(object):
    @staticmethod
    def get_user_fiat_conversion_currency():
        fiat_conversion_currencies = [
            {
                "type": "list",
                "name": "currency",
                "message": "In what currency do you want your FIAT balance displayed? ",
                "choices": ["USD", "EUR", "NGN", "CNY", "CNY"],
            }
        ]
        currencies = prompt(fiat_conversion_currencies, style=custom_style_3)

        return currencies.get("currency")
