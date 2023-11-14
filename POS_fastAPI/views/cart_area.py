import reflex as rx

# import components
from ..components.cart_item import cart_item


def cart_area() -> rx.Component:
    return rx.vstack(
        cart_item()
    )
