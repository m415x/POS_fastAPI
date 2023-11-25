import reflex as rx

# import views
from .pages.main_page import main_page


@rx.page()
def index() -> rx.Component:
    return rx.fragment(
        main_page()
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=[
        "styles/point_of_sale.css",
        "styles/inventory.css",
    ],
)
# app.add_page(index, route="/")
app.compile()
