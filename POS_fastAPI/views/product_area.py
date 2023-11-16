import reflex as rx

# import components
from ..components.product_item import product_item


def product_area() -> rx.Component:
    return rx.container(
        rx.flex(
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            product_item(),
            justify_content="center",
            wrap="wrap",
            gap=["0.25rem", "0.5rem", "0.75rem", "1rem", "1.25rem"],
        ),
        max_w="100%",
        max_h=f"calc(100vh - {1/11}vh - 6rem)",
        padding_top="1.5rem",
        overflow_y="auto",
    )
