import reflex as rx

# import components
from ..components.sidebar_component import sidebar_component

# import styles
from ...styles.colors import DarkThemeColor


def sidebar_menu_view() -> rx.Component:
    theme = "dark"

    return rx.box(
        rx.flex(
            rx.image(
                src=f"icons/avatar_{theme}.svg",
                width="2.5vw",
                # _hover={
                #     "transition_duration": "0.3s",
                #     "filter": "invert(70%)",
                # },
                style={
                    ":hover": {
                        "transition_duration": "0.3s",
                        "filter": "invert(70%)",
                    },
                },  # type: ignore
            ),
            rx.vstack(
                sidebar_component(f"home_{theme}.svg"),
                sidebar_component(f"pos_{theme}.svg"),
                sidebar_component(f"inventory_{theme}.svg"),
                sidebar_component(f"suppliers_{theme}.svg"),
                sidebar_component(f"clients_{theme}.svg"),
                spacing="3em",
                margin_bottom="8em",
            ),
            sidebar_component(f"logout_{theme}.svg"),
            # rx.color_mode_button(
            #     rx.color_mode_icon(),
            #     float="right",
            # ),
            direction="column",
            h="calc(100vh - 3em)",
            margin="1em 0",
            justify="space-between",
            align="center",
        ),
        border_radius="15px",
        bg=DarkThemeColor.SECONDARY.value,
    )
