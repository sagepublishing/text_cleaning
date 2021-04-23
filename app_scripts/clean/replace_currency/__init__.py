"""This module consists of method to Replace all currency symbols in
    ``text`` str with the string specified by ``replace_with`` str."""
# source: https://github.com/jfilter/clean-text/

import re

CURRENCIES = {
    "$": "USD",
    "zł": "PLN",
    "£": "GBP",
    "¥": "JPY",
    "฿": "THB",
    "₡": "CRC",
    "₦": "NGN",
    "₩": "KRW",
    "₪": "ILS",
    "₫": "VND",
    "€": "EUR",
    "₱": "PHP",
    "₲": "PYG",
    "₴": "UAH",
    "₹": "INR",
}

CURRENCY_REGEX = re.compile(
    "({})+".format("|".join(re.escape(c) for c in CURRENCIES.keys()))
)


def replace_currency_symbols(string_value: str, opts: dict):
    """
    Replace all currency symbols in ``text`` str with
    string specified by ``replace_with`` str.
    Args:
        string_value (str): raw text
        opts (str): if None (default), replace symbols with their standard
        3-letter abbreviations (e.g. '$' with 'USD', '£' with 'GBP');otherwise,
        pass in a string with which to replace all symbols (e.g. "*CURRENCY*")
    Returns:
        str
    """
    token = opts["token"]

    if token is None:
        for key, val in CURRENCIES.items():
            string_value = string_value.replace(key, val)
        return string_value
    else:
        return CURRENCY_REGEX.sub(token, string_value)
