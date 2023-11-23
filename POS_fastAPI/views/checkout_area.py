import reflex as rx
from typing import List


# import styles
from ..styles.colors import DarkThemeColor
from ..styles.sizes import Size


options_discount: List[str] = ["amount", "percentage",]


# class RadioState(rx.State):
#     text: str = "No Selection"


def checkout_area() -> rx.Component:
    return rx.vstack(
        rx.flex(
            rx.text(
                "Subtotal (Items: 20, Qty: 30)",
                flex="0 0 85%",
                size="sm",
            ),
            rx.text(
                "2.000",
                flex="0 0 15%",
                size="sm",
                text_align="right",
            ),
            w="100%",
            wrap="wrap",
            align="center",
        ),
        rx.flex(
            rx.text(
                "Discount",
                flex="0 0 30%",
                size="sm",
            ),
            rx.radio_group(
                options_discount,
                default_value="amount",
                default_checked=True,
                flex="0 0 45%",
                display="flex",
                justify_content="space-between",
                # on_change=RadioState.set_text,
            ),
            rx.number_input(
                class_name="discount",
                name="discount",
                variant="unstyled",
                allow_mouse_wheel=True,
                # clamped_value_on_blur=True,
                error_border_color=DarkThemeColor.DANGER.value,
                focus_border_color=DarkThemeColor.OUTLINE.value,
                w="3em",
                h="2em",
                display="flex",
                # value=NumberInputState.value,
                default_value=0,  # type: ignore
                # on_change=NumberInputState.set_value
                flex="0 0 25%",
            ),
            w="100%",
            wrap="wrap",
            align="center",
        ),
        rx.flex(
            rx.text(
                "Total",
                flex="0 0 65%",
                size="xl",
            ),
            rx.text(
                "$ 2.000",
                flex="0 0 35%",
                size="xl",
                text_align="right",
            ),
            w="100%",
            padding="10px 0",
            wrap="wrap",
            align="center",
            border_top=f"1px dashed {DarkThemeColor.LIGHT.value}",
            font_size=Size.BIG.value,
        ),
        rx.button_group(
            rx.button(
                "Cash",
                flex="0 0 30%",
            ),
            rx.button(
                "Transfer",
                flex="0 0 30%",
            ),
            rx.button(
                "Debit & Credit",
                flex="0 0 30%",
            ),
            w="100%",
            h="2em",
            justify_content="space-evenly",
        ),
        padding="20px",
        wrap="wrap",
    )
