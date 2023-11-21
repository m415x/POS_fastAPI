

def format_int(number: float):
    """ Format an integer with dots as thousands separators. """
    return "{:,}".format(number).replace(",", ".")


def format_float_1f(number: float):
    """ Format a floating-point number with periods as thousands and one-decimal place separators. """
    return "{:,.1f}".format(number).replace(",", "~").replace(".", ",").replace("~", ".")


def format_float_2f(number: float):
    """ Format a floating-point number with periods as thousands and two-decimal place separators. """
    return "{:,.2f}".format(number).replace(",", "~").replace(".", ",").replace("~", ".")
