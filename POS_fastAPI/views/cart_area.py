import reflex as rx

# import components
from ..components.cart_item import cart_item

# import styles
from ..styles.colors import DarkThemeColor


def cart_area() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Order N° 1234",
            size="md",
            align_self="flex-start",
            padding="0.5em"
        ),
        rx.flex(
            rx.text(
                "Description",
                flex="0 0 40%",
            ),
            rx.text(
                "Price",
                flex="0 0 15%",
                text_align="center",
            ),
            rx.text(
                "Qty",
                flex="0 0 30%",
                text_align="center",
            ),
            rx.text(
                "Total",
                flex="0 0 15%",
                text_align="center",
            ),
            direction="row",
            w="100%",
            h="2em",
            padding="0 20px",
            border_bottom=f"1px solid {DarkThemeColor.LIGHT.value}",
            align="center",
        ),
        rx.box(
            rx.vstack(
                cart_item(),
                cart_item(),
                cart_item(),
                cart_item(),                cart_item(),
                cart_item(),
                cart_item(),                cart_item(),
                cart_item(),
                cart_item(),                cart_item(),
                cart_item(),
                cart_item(),                cart_item(),
                cart_item(),
                cart_item(),                cart_item(),
                cart_item(),
                cart_item(),
            ),
            box_sizing="border-box",
            w="100%",
            h=f"calc((8/11)*100vh - 5.875em)",
            overflow_y="auto",
        ),
    )
