import reflex as rx
from ..states import HeaderState


def header() -> rx.Component:
    return rx.hstack(
        rx.color_mode_button(
            rx.color_mode_icon(),
            float="left",
        ),
        rx.avatar(
            name=HeaderState.name,
            size="md",
            border="solid 4px white",
            bg=HeaderState.color,
            on_click=HeaderState.flip_color,
        ),
    )
