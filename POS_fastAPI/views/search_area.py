from turtle import position
from click import style
import reflex as rx

# import components
from ..components.button_header import button_header


def search_area() -> rx.Component:
    return rx.hstack(
        rx.button_group(
            button_header("Home", "#"),
            button_header("Otro", "#"),
            button_header("y otro", "#"),
            rx.form(
                rx.input_group(
                    rx.input_left_element(
                        rx.icon(tag="search"),
                    ),
                    rx.input(
                        placeholder="Phone number"
                    ),
                    rx.input_right_element(
                        rx.icon(tag="search"),

                    ),
                    style={
                        "display": "flex",
                        "align_items": "center",
                        "border": "1px solid #ccc",
                        "border_radius": "9999px",
                        "padding": "0.5rem",
                        "margin_bottom": "1rem"
                    }
                ),
            )
        ),
    )
