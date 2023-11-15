import reflex as rx

# import components
from ..components.sidebar_item import sidebar_item


def sidebar_menu() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="icons/avatar.svg",
            width="2.5vw",
        ),
        rx.spacer(),
        sidebar_item("home.svg"),
        sidebar_item("cart.svg"),
        sidebar_item("add.svg"),
        sidebar_item("suppliers.svg"),
        sidebar_item("clients.svg"),
        rx.spacer(),
        rx.spacer(),
        sidebar_item("logout.svg"),
        # rx.color_mode_button(
        #     rx.color_mode_icon(),
        #     float="right",
        # ),
        margin_top="1em",
        spacing="3em",
    )
