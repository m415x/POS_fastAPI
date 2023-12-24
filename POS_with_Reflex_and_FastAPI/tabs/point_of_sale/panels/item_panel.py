import reflex as rx
from typing import List

# import components
from ....tabs.point_of_sale.components.item_component import item_component

# import queries
from ....database.queries import ItemQuery


def item_panel() -> rx.Component:

    # Call 'get_items' method to fetch items if not already done
    item_query_instance = ItemQuery()
    item_query_instance.get_items()
    items: List[dict] = item_query_instance.items

    return rx.container(
        rx.flex(
            # Use '*map' to render each item using 'item_component'
            *map(item_component, items),
            justify_content="center",
            wrap="wrap",
            gap=["0.25rem", "0.5rem", "0.75rem", "1rem", "1.25rem"],
        ),
        id="item_panel",
        max_w="100%",
        max_h=f"calc((10/11)*100vh - 1em)",
        padding_top="0.5rem",
        overflow_y="auto",
    )
