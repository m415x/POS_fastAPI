import reflex as rx

# import components
from ..components.sidebar_item import sidebar_item


def sidebar_menu() -> rx.Component:
    return rx.vstack(
        sidebar_item("home.svg"),
        sidebar_item("home.svg"),
        sidebar_item("home.svg"),
        sidebar_item("home.svg"),
        # rx.color_mode_button(
        #     rx.color_mode_icon(),
        #     float="right",
        # ),
        margin_top="2em",
        spacing="2em"
    )
