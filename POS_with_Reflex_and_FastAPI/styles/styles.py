import reflex as rx

from .fonts import Font, FontWeight
from .colors import DarkThemeColor


STYLESHEETS = [

    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@300;500&display=swap",

    "styles/sidebar_component.css",
    "styles/point_of_sale.css",
    "styles/inventory.css",

]


BASE_STYLE = {

    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,

    rx.Button: {
        "font_weight": FontWeight.LIGHT.value,
        ":hover": {
            "background": DarkThemeColor.HOVER.value,
        }
    },

    rx.Heading: {
        "font_weight": FontWeight.MEDIUM.value,
    },

    rx.MenuList: {
        "background": DarkThemeColor.BACKGROUND.value,
    },

    rx.MenuItem: {
        "background": DarkThemeColor.BACKGROUND.value,
        ":hover": {
            "background": DarkThemeColor.HOVER.value
        },
    },
}
