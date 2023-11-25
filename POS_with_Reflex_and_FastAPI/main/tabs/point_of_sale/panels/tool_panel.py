import reflex as rx
from typing import List

# import components
from ..components.tab_component import tab_component
from ..components.html_components import search_input

# import styles
from .....styles.colors import DarkThemeColor

# import states
# from ..states import State


options: List[str] = ["Option 1", "Option 2", "Option 3"]


# class SelectState(rx.State):
#     option: str = "No selection yet."


def tool_panel() -> rx.Component:
    return rx.flex(
        rx.button_group(
            tab_component("client 1"),
            tab_component(),
            align_self="center",
        ),
        rx.hstack(
            rx.select(
                options,
                placeholder="Select category",
                color=DarkThemeColor.WHITE.value,
                bg=DarkThemeColor.SECONDARY.value,
                focus_border_color=DarkThemeColor.OUTLINE.value,
                border_radius="30px",
                h="3em",
                max_w="200px",
                style={
                    "cursor": "pointer",
                    "option": {
                        "background": DarkThemeColor.SECONDARY.value,
                    },
                    "_focus": {
                        "background": "transparent",
                    },
                }
                # on_change=SelectState.set_option,
            ),
            rx.html(search_input),
        ),
        direction="row",
        justify="space-between",
        align_self="center",
        h="100%",
        margin="0 0.5em"
    )
