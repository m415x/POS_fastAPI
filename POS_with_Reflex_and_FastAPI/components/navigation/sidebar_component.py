import reflex as rx
from typing import Optional, Callable


def sidebar_component(name: str, theme: str, on_click: Optional[Callable[[], None]] = None) -> rx.Component:
    return rx.image(
        src=f"icons/{name}_{theme}.svg",
        alt="i",
        class_name="sidebar-component",
        h="2.5vw",
        transition="filter 0.1s ease-out",
        style={
            ":hover": {
                "transition_duration": "0.3s",
                "filter": "invert(70%)",
            },
        },  # type: ignore
        on_click=on_click
    )
