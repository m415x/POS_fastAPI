import reflex as rx

# import views
from .views.sidebar_menu import sidebar_menu
from .views.search_area import search_area
from .views.cart_area import cart_area


def index() -> rx.Component:
    return rx.fragment(
        rx.grid(
            rx.grid_item(
                sidebar_menu(),
                col_span=1,
                row_span=11,
                # bg="lightblue",
            ),
            rx.grid_item(
                search_area(),
                col_span=19,
                row_span=1,
                bg="lightgreen"
            ),
            rx.grid_item(
                cart_area(),
                col_span=8,
                row_span=8,
                bg="orange"
            ),
            rx.grid_item(col_span=19, row_span=10, bg="yellow"),
            rx.grid_item(col_span=8, row_span=3, bg="purple"),
            template_columns="repeat(28, 1fr)",
            template_rows="repeat(11, 1fr)",
            # h="200px",
            width="100vw",
            height="100vh",
            gap=2,
            style={
                "max_width": "100vw",
                "padding": "0.5em",
                "margin": "0",
                "background": "#1e1e1e"
            }
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index, route="/")
app.compile()
