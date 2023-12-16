import reflex as rx

# import pages
from .pages.main_page import main_page

# import styles
from .styles.styles import STYLESHEETS, BASE_STYLE

# import constants
from .constants import META_DATA

# import models
from .database import models


@rx.page(**META_DATA)
def index() -> rx.Component:
    return rx.fragment(
        rx.script("document.documentElement.lang = 'en'"),
        main_page()
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
)


# app.add_page(index, route="/")
app.compile()
