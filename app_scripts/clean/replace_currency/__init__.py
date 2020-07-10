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


def replace_currency_symbols(inStr, token):
    """
    Replace all currency symbols in ``text`` str with string specified by ``replace_with`` str.
    Args:
        text (str): raw text
        replace_with (str): if None (default), replace symbols with
            their standard 3-letter abbreviations (e.g. '$' with 'USD', '£' with 'GBP');
            otherwise, pass in a string with which to replace all symbols
            (e.g. "*CURRENCY*")
    Returns:
        str
    """
    if token is None:
        for k, v in constants.CURRENCIES.items():
            text = text.replace(k, v)
        return text
    else:
        return CURRENCY_REGEX.sub(token, inStr)