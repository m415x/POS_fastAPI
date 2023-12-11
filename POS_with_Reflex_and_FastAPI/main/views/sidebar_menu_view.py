import reflex as rx

# import components
from ...components.navigation.sidebar_component import sidebar_component

# import styles
from ...styles.colors import DarkThemeColor

# import states
from ...states import State


class TabState(State):
    choice: str = "home"

    def set_choice(self, value: str):
        self.choice = value


def sidebar_menu_view() -> rx.Component:
    theme = "dark"

    return rx.box(
        rx.flex(
            rx.menu(
                rx.menu_button(
                    rx.image(
                        src=f"icons/avatar_{theme}.svg",
                        w="90%",
                    ),
                    w="90%",
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
                w="90%"
            ),
            rx.vstack(
                sidebar_component(
                    "home",
                    theme,
                    choice=TabState.choice,
                    on_click=TabState.set_choice("home"),
                ),
                sidebar_component(
                    "point_of_sale",
                    theme,
                    choice=TabState.choice,
                    on_click=TabState.set_choice("point_of_sale"),
                ),
                sidebar_component(
                    "inventory",
                    theme,
                    choice=TabState.choice,
                    on_click=TabState.set_choice("inventory"),
                ),
                sidebar_component(
                    "suppliers",
                    theme,
                    choice=TabState.choice,
                    on_click=TabState.set_choice("suppliers"),
                ),
                sidebar_component(
                    "clients",
                    theme,
                    choice=TabState.choice,
                    on_click=TabState.set_choice("clients"),
                ),
                # spacing="3em",
                # margin_bottom="8em",
                flex="0 0 60%",
                justify="space-evenly",
            ),
            rx.menu(
                rx.menu_button(
                    sidebar_component(
                        "logout",
                        theme,
                        choice=TabState.choice,
                        on_click=TabState.set_choice(""),
                    ),
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
        h="100vh",
        w="clamp(30px, 2.5vw, 50px)",
    )
