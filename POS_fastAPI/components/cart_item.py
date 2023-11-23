import reflex as rx


# import styles
from ..styles.colors import DarkThemeColor
from ..styles.sizes import Size


# import state
from ..states import State


# class NumberInputState(State):
#     value: float

#     def increment(self):
#         self.value += 0.5

#     def decrement(self):
#         self.value -= 0.5


def cart_item() -> rx.Component:
    return rx.card(
        rx.flex(
            rx.text(
                "Clavo",
                font_size="1em",
                flex="0 0 40%",
                custom_attrs={'title': 'EF-00012'},
            ),
            rx.text(
                "100",
                font_size="1em",
                flex="0 0 15%",
                text_align="right",
            ),
            rx.flex(
                rx.button(
                    "-",
                    variant="ghost",
                    h="30px",
                    w="30px",
                    padding="0",
                    size="xs"
                    # on_click=NumberInputState.decrement,
                ),
                rx.number_input(
                    class_name="quantity",
                    name="quantity",
                    variant="unstyled",
                    allow_mouse_wheel=True,
                    # clamped_value_on_blur=True,
                    error_border_color=DarkThemeColor.DANGER.value,
                    focus_border_color=DarkThemeColor.OUTLINE.value,
                    w="3em",
                    h="3em",
                    display="flex",
                    # value=NumberInputState.value,
                    default_value=20,  # type: ignore
                    min_=1,  # type: ignore
                    max_=100000,  # type: ignore
                    # on_change=NumberInputState.set_value
                ),
                rx.button(
                    "+",
                    variant="ghost",
                    h="30px",
                    w="30px",
                    padding="0",
                    size="xs"
                    # on_click=NumberInputState.increment,
                ),
                flex="0 0 30%",
                align="center",
                justify="flex-end",
            ),
            rx.text(
                "2.000",
                font_size="1em",
                flex="0 0 15%",
                text_align="right",
            ),
            direction="row",
            width="100%",
            align="center",
        ),
        w="100%",
        h="4em",
        color=DarkThemeColor.WHITE.value,
        bg="transparent",
        justify="center",
        margin_top="0px !important",
        box_shadow="none",
    )
