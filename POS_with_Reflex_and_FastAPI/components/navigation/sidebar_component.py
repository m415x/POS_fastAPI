import reflex as rx
from typing import Optional, Callable

# import styles
from ...styles import icons


def sidebar_component(name: str, theme: str, choice: str, on_click: Optional[Callable[[], None]] = None) -> rx.Component:
    return rx.image(
        src=f"icons/{name}_{theme}.svg",
        alt="i",
        class_name=rx.cond(
            choice == name,
            "sidebar-component active",
            "sidebar-component"
        ),
        w="90%",
        transition="filter 0.1s ease-out",
        style={
            ":hover": {
                "transition_duration": "0.3s",
                "filter": "invert(70%)",
            },
        },
        on_click=on_click,
    )
