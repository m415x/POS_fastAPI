import reflex as rx

# import components
from ..components.sidebar_item import sidebar_item


def sidebar_menu() -> rx.Component:
    theme = "dark"

    return rx.flex(
        rx.image(
            src=f"icons/avatar_{theme}.svg",
            width="2.5vw",
            _hover={
                "transition_duration": "0.3s",
                "filter": "invert(50%)",
            },
        ),
        rx.vstack(
            sidebar_item(f"home_{theme}.svg"),
            sidebar_item(f"pos_{theme}.svg"),
            sidebar_item(f"inventory_{theme}.svg"),
            sidebar_item(f"suppliers_{theme}.svg"),
            sidebar_item(f"clients_{theme}.svg"),
            spacing="3em",
            margin_bottom="8em",
        ),
        sidebar_item(f"logout_{theme}.svg"),
        # rx.color_mode_button(
        #     rx.color_mode_icon(),
        #     float="right",
        # ),
        direction="column",
        h="calc(100vh - 3em)",
        margin="1em 0",
        justify="space-between",
        align="center",
    )
