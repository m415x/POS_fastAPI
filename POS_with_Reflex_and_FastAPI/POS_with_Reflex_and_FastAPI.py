import reflex as rx

# import pages
from .pages.main_page import main_page

# import styles
from .styles.styles import STYLESHEETS, BASE_STYLE


@rx.page()
def index() -> rx.Component:
    return rx.fragment(
        main_page()
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE
)
# app.add_page(index, route="/")
app.compile()
