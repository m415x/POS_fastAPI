import reflex as rx

# import components
from ....components.navigation.button_component import button_component
from ....components.data_entry.search_component import search_component
from ....components.data_entry.select_component import select_component

# import styles
from ....styles.colors import DarkThemeColor


def tool_panel() -> rx.Component:
    return rx.flex(
        rx.button_group(
            button_component("client 1"),
            button_component(),
            align_self="center",
        ),
        rx.hstack(
            select_component(),
            search_component(),
        ),
        direction="row",
        justify="space-between",
        align_self="center",
        h="100%",
        margin="0 0.5em"
    )
