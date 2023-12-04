import reflex as rx
from typing import List

# import components
from ....components.navigation.button_component import button_component
from ....components.data_entry.search_component import search_component
from ....components.data_entry.select_component import select_component

# import styles
from ....styles.colors import DarkThemeColor

# import states
# from ..states import State


options: List[str] = ["Option 1", "Option 2", "Option 3"]


# class SelectState(rx.State):
#     option: str = "No selection yet."


def filter_panel() -> rx.Component:
    return rx.flex(
        rx.hstack(
            select_component(),
            button_component("Apply"),
            button_component(),
            align_self="center",
        ),
        rx.hstack(
            search_component(),
        ),
        direction="row",
        justify="space-between",
        align_self="center",
        h="100%",
        margin="0 10px"
    )
