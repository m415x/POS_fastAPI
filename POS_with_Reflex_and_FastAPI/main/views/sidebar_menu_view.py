import reflex as rx

# import components
from ...components.navigation.sidebar_component import sidebar_component

# import styles
from ...styles.colors import DarkThemeColor


def sidebar_menu_view() -> rx.Component:
    theme = "dark"

    return rx.box(
        rx.flex(
            rx.menu(
                rx.menu_button(
                    rx.image(
                        src=f"icons/avatar_{theme}.svg",
                        width="2.5vw",
                    ),
                ),
                rx.menu_list(
                    rx.color_mode_button(
                        rx.color_mode_icon(),
                        float="right",
                        variant="unstyled",
                        position="absolute",
                        right=0,
                        top="6px"
                    ),
                    rx.menu_item("Config"),
                    rx.menu_divider(),
                    rx.menu_item("Example"),
                    position="relative"
                ),
            ),
            rx.vstack(
                sidebar_component(f"home_{theme}.svg"),
                sidebar_component(f"pos_{theme}.svg"),
                sidebar_component(f"inventory_{theme}.svg"),
                sidebar_component(f"suppliers_{theme}.svg"),
                sidebar_component(f"clients_{theme}.svg"),
                # spacing="3em",
                # margin_bottom="8em",
                flex="0 0 60%",
                justify="space-evenly",
            ),
            rx.menu(
                rx.menu_button(
                    sidebar_component(f"logout_{theme}.svg"),
                ),
                rx.menu_list(
                    rx.menu_item("Switch user"),
                    rx.menu_divider(),
                    rx.menu_item("Log out"),
                ),
            ),
            direction="column",
            h="calc(100vh - 3em)",
            margin="1em 0",
            justify="space-between",
            align="center",
        ),
        bg=DarkThemeColor.SECONDARY.value,
    )
