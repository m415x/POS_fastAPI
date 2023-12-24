# import styles
from ..styles.colors import DarkThemeColor


def format_number(number: float, unit: str = None) -> str:
    if unit != "u":
        """ Format a floating-point number with periods as thousands and two-decimal place separators. """
        return "{:,.2f}".format(number).replace(",", "~").replace(".", ",").replace("~", ".")
    else:
        """ Format an integer with dots as thousands separators. """
        return "{:,}".format(int(number)).replace(",", ".")


def format_code(item: dict) -> str:
    return f"{item['category']['name'][0:2].upper()}-{item['id']:05d}"


def assign_color(stock: float) -> DarkThemeColor:
    if stock < 5:
        return DarkThemeColor.DANGER.value
    elif stock < 10:
        return DarkThemeColor.WARNING.value
    else:
        return DarkThemeColor.SUCCESS.value
