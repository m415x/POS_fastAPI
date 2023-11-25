import reflex as rx

# import styles
from .....styles.colors import DarkThemeColor


def tab_component(text: str | None = None) -> rx.Component:
    return rx.button(
        rx.icon(
            tag="add"
        ),
        class_name="cursor-pointer outline-none hover:rotate-90 duration-300",  # type: ignore
        border_radius="50%",
        w="3em",
        h="3em",
        bg=DarkThemeColor.SECONDARY.value,
        # _hover={
        #     "background": DarkThemeColor.HOVER.value,
        # },
        style={
            ":hover": {
                "background": DarkThemeColor.HOVER.value,
            },
        },  # type: ignore
    ) if text == None else (
        rx.button(
            text,
            color=DarkThemeColor.WHITE.value,
            class_name="cursor-pointer outline-none duration-300",
            border_radius="30px",
            h="3em",
            bg=DarkThemeColor.SECONDARY.value,
            # _hover={
            #     "background": DarkThemeColor.HOVER.value,
            # },
            style={
                ":hover": {
                    "background": DarkThemeColor.HOVER.value,
                }
            },  # type: ignore
            # onContextMenu="mostrar menu contextual con opciones de guardado o cerrado"
        )
    )
