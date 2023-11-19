import reflex as rx

# import styles
from ..styles.colors import Color, TextColor


def search_item(text: str | None = None) -> rx.Component:
    return rx.button(
        rx.icon(
            tag="add"
        ),
        class_name="cursor-pointer outline-none hover:rotate-90 duration-300",  # type: ignore
        border_radius="50%",
        w="3em",
        h="3em",
        bg=Color.PRIMARY_DARK.value,
        _hover={
            "background": Color.HOVER_DARK.value
        }
    ) if text == None else (
        rx.button(
            text,
            color=TextColor.BODY_DARK.value,
            class_name="cursor-pointer outline-none duration-300",
            border_radius="30px",
            h="3em",
            bg=Color.PRIMARY_DARK.value,
            _hover={
                "background": Color.HOVER_DARK.value
            },
            # onContextMenu="mostrar menu contextual con opciones de guardado o cerrado"
        )
    )
