import reflex as rx

# import styles
from ....styles.colors import DarkThemeColor
from ....styles.sizes import Size

# import utils
from ....utils.utils import format_number, format_code, assign_color


def item_component(item: dict) -> rx.Component:

    formatted_stock = format_number(item['stock'], item["unit"]["symbol"])
    formatted_price = format_number(item['price'])

    return rx.card(
        rx.card_body(
            rx.flex(
                rx.image(
                    src=f"/uploads/{item['img']}.jpg",
                    src_set="",  # <picture> <source avif><source webp><source jpg> </picture>
                    alt=f"Image from {item['info']}",
                    margin_top="1rem",
                    width="8.5rem",
                    height="8.5rem",
                    border_radius="50%",
                    box_shadow="5px 10px 20px rgba(0, 0, 0, 0.329)",
                    loading="lazy",
                ),
                rx.stack(
                    rx.flex(
                        rx.text(
                            format_code(item),
                            font_size=Size.MEDIUM.value,
                            line_height=Size.LARGE.value,
                            color=DarkThemeColor.WHITE.value,
                            letter_spacing="1px",
                        ),
                        rx.text(
                            f"Stock {formatted_stock} [{item['unit']['symbol']}]",
                            font_size=Size.MEDIUM.value,
                            line_height=Size.LARGE.value,
                            color=assign_color(item["stock"]),
                            letter_spacing="0.5px",
                        ),
                        justify="space-between"
                    ),
                    rx.text(
                        item['info'],
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
                    p="1rem",
                    width="100%",
                    height="100%",
                    justify="space-between",
                ),
                direction="column",
                align="center",
                bg=DarkThemeColor.SECONDARY.value if item[
                    'stock'] > 0 else DarkThemeColor.DANGER.value,
                border_radius="20px",
                box_shadow="0 20px 40px -14px rgba(0, 0, 0, 0.25)",
                overflow="hidden",
                transition="transform 0.5s",
                style={
                    ":hover": {
                        "cursor": "pointer",
                        "transform": "scale(1.1)",
                        "background": DarkThemeColor.CONTENT.value,
                    },
                },  # type: ignore
                width="13rem",
                height="100%",
            ),
            padding="0",
        ),
        border_radius="20px",
    )
