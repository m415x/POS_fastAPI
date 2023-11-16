import reflex as rx

# import components
from ..components.sidebar_item import sidebar_item


def sidebar_menu() -> rx.Component:
    theme = "dark"

    return rx.vstack(
        rx.image(
            src=f"icons/avatar_{theme}.svg",
            width="2.5vw",
        ),
        rx.spacer(),
        sidebar_item(f"home_{theme}.svg"),
        sidebar_item(f"pos_{theme}.svg"),
        sidebar_item(f"inventory_{theme}.svg"),
        sidebar_item(f"suppliers_{theme}.svg"),
        sidebar_item(f"clients_{theme}.svg"),
        rx.spacer(),
        rx.spacer(),
        sidebar_item(f"logout_{theme}.svg"),
        # rx.color_mode_button(
        #     rx.color_mode_icon(),
        #     float="right",
        # ),
        margin_top="1em",
        spacing="3em",
    )
