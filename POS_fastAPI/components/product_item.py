import reflex as rx


# import styles
from ..styles.colors import DarkThemeColor
from ..styles.sizes import Size

# import utils
from ..utils.formatting import format_int, format_float_1f, format_float_2f


def product_item(img: str, id: str, stock: float, info: str, price: float) -> rx.Component:

    formatted_stock = format_int(stock) if int(
        stock) == stock else format_float_1f(stock)
    formatted_price = format_float_2f(price)

    return rx.card(
        rx.card_body(
            rx.flex(
                rx.image(
                    src=img,
                    src_set="",  # <picture> <source avif><source webp><source jpg> </picture>
                    alt="Green double couch with wooden legs",
                    margin_top="1rem",
                    width="8.5rem",
                    height="8.5rem",
                    border_radius="50%",
                    box_shadow="5px 10px 20px rgba(0, 0, 0, 0.329)",
                ),
                rx.stack(
                    rx.flex(
                        rx.text(
                            id,
                            font_size=Size.MEDIUM.value,
                            line_height=Size.LARGE.value,
                            color=DarkThemeColor.WHITE.value,
                            letter_spacing="1px",
                        ),
                        rx.text(
                            f"Stock {formatted_stock} u",
                            font_size=Size.MEDIUM.value,
                            line_height=Size.LARGE.value,
                            color=DarkThemeColor.DANGER.value,
                        ),
                        justify="space-between"
                    ),
                    rx.text(  # 1.stock(color), 2.(category[0:2].upper()}}-{{ '%05d' % id), 3.(name <br> info), 4.price => STOCK=0 -> Card_bg=LOW
                        info,
                        font_size=Size.DEFAULT.value,
                        line_height=Size.LARGE.value,
                        color=DarkThemeColor.WHITE.value,
                        mb="0.2em"
                    ),
                    rx.text(
                        f"$ {formatted_price}",
                        line_height=Size.LARGE.value,
                        color=DarkThemeColor.WHITE.value,
                        align_self="flex-end",
                        letter_spacing="1px",
                    ),
                    p="1rem"
                ),
                direction="column",
                align="center",
                bg=DarkThemeColor.SECONDARY.value,
                border_radius="20px",
                box_shadow="0 20px 40px -14px rgba(0, 0, 0, 0.25)",
                overflow="hidden",
                transition="transform 0.5s",
                # _hover={
                #     "cursor": "pointer",
                #     "transform": "scale(1.1)",
                #     "background": DarkThemeColor.CONTENT.value,
                # },
                style={
                    ":hover": {
                        "cursor": "pointer",
                        "transform": "scale(1.1)",
                        "background": DarkThemeColor.CONTENT.value,
                    },
                },  # type: ignore
                max_width="12rem",
                min_width="10rem",
            ),
            padding="0",
        ),
        border_radius="20px",

    )
