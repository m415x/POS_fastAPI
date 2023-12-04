import reflex as rx

# import panels
from ...tabs.inventory.panels.filter_panel import filter_panel
from ...tabs.inventory.panels.inventory_panel import inventory_panel


def inventory_view() -> rx.Component:
    return rx.grid(
        rx.grid_item(
            filter_panel(),
            col_span=27,
            row_span=1,
            w="100%",
        ),
        rx.grid_item(
            inventory_panel(),
            col_span=27,
            row_span=10,
            padding="0 0 0 10px",
            max_h="100vh",
            max_w="calc(100vw - (1/27)*100vw - 1em)",
            wrap="wrap",
            overflow_y="auto",
            overflow_x="auto",
        ),
        template_columns="repeat(27, 1fr)",
        template_rows="repeat(11, 1fr)",
        gap=2,
        h="98vh",
    )
