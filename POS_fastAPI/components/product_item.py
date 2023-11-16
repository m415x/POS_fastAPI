import reflex as rx

# import styles
from ..styles.colors import Color, TextColor
from ..styles.sizes import Size


def product_item() -> rx.Component:
    return rx.card(
        rx.card_body(
            rx.flex(
                rx.image(
                    src="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1770&q=80",
                    alt="Green double couch with wooden legs",
                    fit="cover",
                    border_radius="6px 6px 0px 0px",
                    opacity="0.91"
                ),
                rx.stack(
                    rx.text(
                        "Some",
                        font_size=Size.LARGE.value,
                        line_height=Size.MEDIUM.value,
                        color=TextColor.HEADER_DARK.value,
                        mb="0.2em"
                    ),
                    rx.text(
                        "Some",
                        line_height=Size.LARGE.value,
                        color=TextColor.BODY_DARK.value,
                    ),
                    p="1rem"
                ),
                direction="column",
                bg=Color.PRIMARY_DARK.value,
                border_radius="6px",
                box_shadow="0 20px 40px -14px rgba(0, 0, 0, 0.25)",
                overflow="hidden",
                transition="transform 0.5s",
                _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.1)",
                },
                max_width="12rem",
                min_width="10rem",
            ),
            padding="0",
        ),
    )
