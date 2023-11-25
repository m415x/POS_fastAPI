import reflex as rx

# import views
from ..main.views.sidebar_menu_view import sidebar_menu_view
from ..main.views.home_view import home_view
from ..main.views.point_of_sale_view import point_of_sale_view
from ..main.views.inventory_view import inventory_view


# import styles
from ..styles.colors import DarkThemeColor


def main_page() -> rx.Component:
    return rx.grid(
        sidebar_menu_view(),
        # point_of_sale(),
        inventory_view(),
        template_columns="1fr 27fr",
        template_rows="1fr 10fr",
        width="calc(100vw - 0em)",
        height="calc(100vh - 0em)",
        gap=2,
        max_width="100vw",
        padding="0.5em",
        margin="0",
        bg=DarkThemeColor.BACKGROUND.value,
    )
