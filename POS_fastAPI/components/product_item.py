import reflex as rx


# import styles
from ..styles.colors import Color, TextColor, StockColor
from ..styles.sizes import Size


def product_item(img: str, id: str, stock: float, info: str, price: float) -> rx.Component:

    # Formatear el número con separador de miles y decimales
    format_price = f'$ {"{:,.2f}".format(price).replace(",", "~").replace(".", ",").replace("~", ".")}'

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
                            color=TextColor.FOOTER_DARK.value,
                            letter_spacing="1px",
                        ),
                        rx.text(
                            f"STOCK {stock}",
                            font_size=Size.MEDIUM.value,
                            line_height=Size.LARGE.value,
                            color=StockColor.LOW_DARK.value,
                        ),
                        justify="space-between"
                    ),
                    rx.text(  # 1.stock(color), 2.(category[0:2].upper()}}-{{ '%05d' % id), 3.(name <br> info), 4.price => STOCK=0 -> Card_bg=LOW
                        info,
                        font_size=Size.DEFAULT.value,
                        line_height=Size.LARGE.value,
                        color=TextColor.HEADER_DARK.value,
                        mb="0.2em"
                    ),
                    rx.text(
                        format_price,
                        line_height=Size.LARGE.value,
                        color=TextColor.FOOTER_DARK.value,
                        align_self="flex-end",
                        letter_spacing="1px",
                    ),
                    p="1rem"
                ),
                direction="column",
                align="center",
                bg=Color.PRIMARY_DARK.value,
                border_radius="6px",
                box_shadow="0 20px 40px -14px rgba(0, 0, 0, 0.25)",
                overflow="hidden",
                transition="transform 0.5s",
                _hover={
                    "cursor": "pointer",
                    "transform": "scale(1.1)",
                    "background": Color.CONTENT_DARK.value,
                },
                max_width="12rem",
                min_width="10rem",
            ),
            padding="0",
        ),
    )
