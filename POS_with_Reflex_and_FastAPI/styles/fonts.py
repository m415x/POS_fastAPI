from enum import Enum

from .sizes import Size


class Font(Enum):
    DEFAULT = "Poppins"
    LOGO = "Comfortaa"


class FontWeight(Enum):
    LIGHT = "300"
    MEDIUM = "500"


FONT_SIZES = [
    Size.SMALL.value,
    Size.X_SMALL.value,
    Size.MEDIUM.value,
    Size.DEFAULT.value
]
