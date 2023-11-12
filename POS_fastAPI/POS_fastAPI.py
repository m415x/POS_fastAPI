import reflex as rx
# views
from .views.header import header


def index() -> rx.Component:
    return rx.fragment(
        header(),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, route="/")
app.compile()
