import reflex as rx

# import views
from .views.header import header


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(
            rx.color_mode_icon(),
            float="right",
        ),
        rx.container(
            header(),
            style={
                "max_width": "100vw",
                "padding": "0",
                "margin": "10px",
            }
        )
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, route="/")
app.compile()
