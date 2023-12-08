import reflex as rx

# import pages
from .pages.main_page import main_page

# import styles
from .styles.styles import STYLESHEETS, BASE_STYLE

META = {
    "title": "Point of Sale (POS) System",
    "description": "The Point of Sale (POS) System is a comprehensive software solution designed to streamline and optimize retail and sales operations. It provides a user-friendly interface for managing various aspects of a business, from handling sales transactions and managing inventory to tracking customer interactions.",
    "image": "/icons/home.png",
    "meta": [
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": "Point of Sale (POS) System"},
        {"name": "og:description",
            "content": "The Point of Sale (POS) System is a comprehensive software solution designed to streamline and optimize retail and sales operations. It provides a user-friendly interface for managing various aspects of a business, from handling sales transactions and managing inventory to tracking customer interactions."},
        {"name": "og:image", "content": "/icons/home.png"},
    ]
}


@rx.page(**META)
def index() -> rx.Component:
    return rx.fragment(
        rx.script("document.documentElement.lang = 'en'"),
        main_page()
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE
)
# app.add_page(index, route="/")
app.compile()
