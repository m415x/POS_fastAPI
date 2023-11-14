import reflex as rx

# import components
from ..components.sidebar_button import sidebar_button


def sidebar_menu() -> rx.Component:
    return rx.vstack(
        sidebar_button("home.svg"),
        sidebar_button("home.svg"),
        sidebar_button("home.svg"),
        sidebar_button("home.svg"),
        # rx.color_mode_button(
        #     rx.color_mode_icon(),
        #     float="right",
        # ),
        margin_top="2em",
        spacing="2em"
    )
