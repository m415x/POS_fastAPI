import reflex as rx

# import panels
from ..tabs.inventory.panels.filter_panel import filter_panel
from ..tabs.inventory.panels.inventory_panel import inventory_panel


def inventory_view() -> rx.Component:
    return rx.flex(
        rx.box(
            filter_panel(),
            w="100%",
            flex="0 0 (1/11)*100%",
        ),
        rx.box(
            inventory_panel(),
            id="inventory_panel",
            flex="0 0 (10/11)*100%",
            padding="20px 0 0 10px",
            max_h="100vh",
            max_w="calc(100vw - (1/27)*100vw - 1em)",
            wrap="wrap",
            overflow_y="auto",
            overflow_x="auto",
        ),
        direction="column",
        h="98vh",
    )
