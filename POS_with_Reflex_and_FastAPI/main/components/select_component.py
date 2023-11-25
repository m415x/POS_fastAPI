import reflex as rx
from typing import List

# import styles
from ...styles.colors import DarkThemeColor

# import states
# from ..states import State


options: List[str] = ["Option 1", "Option 2", "Option 3"]


# class SelectState(rx.State):
#     option: str = "No selection yet."


def select_component() -> rx.Component:
    return rx.select(
        options,
        placeholder="Select",
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
    )
