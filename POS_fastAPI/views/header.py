import reflex as rx

# import components
from ..components.button_header import button_header


def header() -> rx.Component:
    return rx.hstack(
        rx.button_group(
            button_header("Home", "#"),
            button_header("Otro", "#"),
            button_header("y otro", "#"),
        ),
        rx.menu(
            rx.menu_button(
                rx.avatar(
                    name="Cristian Lahoz",
                    size="md",
                    border="solid 4px white",
                    bg="#3d3a4e",
                    color="#fff"

                ),
            ),
            rx.menu_list(
                rx.menu_item("Example"),
                rx.menu_divider(),
                rx.menu_item("Example"),
                rx.menu_item("Example"),
                # bg="#3d3a4e"
            ),
        ),


    )
