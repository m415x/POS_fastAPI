import reflex as rx

# import views
from .views.sidebar_menu import sidebar_menu
from .views.tool_area import tool_area
from .views.product_area import product_area
from .views.cart_area import cart_area

# import styles
from .styles.colors import DarkThemeColor


def index() -> rx.Component:
    return rx.fragment(
        rx.grid(
            rx.grid_item(
                sidebar_menu(),
                col_span=1,
                row_span=11,
                # border_radius="0 20px 20px 0",
                bg=DarkThemeColor.SECONDARY.value,
            ),
            rx.grid_item(
                tool_area(),
                col_span=19,
                row_span=1,
                # bg="lightblue"
            ),
            rx.grid_item(
                cart_area(),
                col_span=8,
                row_span=8,
                # border_radius="20px 0 0 0",
                bg=DarkThemeColor.SECONDARY.value,
            ),
            rx.grid_item(
                product_area(),
                col_span=19,
                row_span=10,
            ),
            rx.grid_item(col_span=8, row_span=3, bg="purple"),
            template_columns="repeat(28, 1fr)",
            template_rows="repeat(11, 1fr)",
            width="100vw",
            height="100vh",
            gap=2,
            max_width="100vw",
            # padding= "0.5em",
            margin="0",
            bg=DarkThemeColor.BACKGROUND.value,
        ),
    )


# Add state and page to the app.
app = rx.App(
    stylesheets=["styles/tool-area.css", "styles/cart-area.css",],
)
app.add_page(index, route="/")
app.compile()
