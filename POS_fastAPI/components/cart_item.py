from pydoc import classname
import reflex as rx


def cart_item() -> rx.Component:
    return rx.card(
        rx.form(
            rx.hstack(
                rx.button(),
                rx.input(
                    classname="quantity"
                ),
                rx.button(),
                rx.spacer(),
                rx.text("Clavo", font_size="1em"),
                rx.spacer(),
                rx.text(100, font_size="1em"),
                rx.spacer(),
                rx.text(100, font_size="1em"),
                width="100%"
            ),
            width="100%"
        )
    )
