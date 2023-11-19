import reflex as rx
from typing import List

# import components
from ..components.search_item import search_item

# import styles
from ..styles.colors import Color, TextColor

# import states
# from ..states import State


options: List[str] = ["Option 1", "Option 2", "Option 3"]


# class SelectState(rx.State):
#     option: str = "No selection yet."


def search_area() -> rx.Component:
    return rx.flex(
        rx.button_group(
            search_item("client 1"),
            search_item(),
            align_self="center",
        ),
        rx.hstack(
            rx.select(
                options,
                placeholder="Select category",
                color=TextColor.BODY_DARK.value,
                bg=Color.PRIMARY_DARK.value,
                focus_border_color=Color.OUTLINE_DARK.value,
                border_radius="30px",
                h="3em",
                max_w="200px",
                style={
                    "cursor": "pointer",
                    "option": {
                        "background": Color.PRIMARY_DARK.value,
                    },
                    "_focus": {
                        "background": "transparent",
                    },
                }
                # on_change=SelectState.set_option,
            ),
            rx.html(
                """
                    <form class="search__form">
                        <label for="search" class="search__label">
                            <input class="search__input" type="text" required="" placeholder="Search">
                            <div class="search__bg"></div>
                            <div class="search__icon">
                                <svg viewBox="0 0 24 24" aria-hidden="true" class="r-14j79pv r-4qtqp9 r-yyyyoo r-1xvli5t r-dnmrzs r-4wgw6l r-f727ji r-bnwqim r-1plcrui r-lrvibr">
                                    <g>
                                        <path d="M21.53 20.47l-3.66-3.66C19.195 15.24 20 13.214 20 11c0-4.97-4.03-9-9-9s-9 4.03-9 9 4.03 9 9 9c2.215 0 4.24-.804 5.808-2.13l3.66 3.66c.147.146.34.22.53.22s.385-.073.53-.22c.295-.293.295-.767.002-1.06zM3.5 11c0-4.135 3.365-7.5 7.5-7.5s7.5 3.365 7.5 7.5-3.365 7.5-7.5 7.5-7.5-3.365-7.5-7.5z"></path>
                                    </g>
                                </svg>
                            </div>
                            <button class="search__close-btn" type="reset">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
                                </svg>
                            </button>
                        </label>
                    </form>
                """
            ),
        ),
        direction="row",
        justify="space-between",
        align_self="center",
        h="100%",
        margin="0 0.5em"
    )
