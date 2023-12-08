import reflex as rx

# import views
from ..main.views.sidebar_menu_view import sidebar_menu_view
from ..main.views.home_view import home_view
from ..main.views.point_of_sale_view import point_of_sale_view
from ..main.views.inventory_view import inventory_view
from ..main.views.suppliers_view import suppliers_view
from ..main.views.clients_view import clients_view

# import styles
from ..styles.colors import DarkThemeColor

# import states
from ..main.views.sidebar_menu_view import TabState


def main_page() -> rx.Component:
    return rx.grid(
        sidebar_menu_view(),
        rx.box(
            rx.cond(
                TabState.choice == "home",
                home_view(),
                rx.cond(
                    TabState.choice == "point_of_sale",
                    point_of_sale_view(),
                    rx.cond(
                        TabState.choice == "inventory",
                        inventory_view(),
                        rx.cond(
                            TabState.choice == "suppliers",
                            suppliers_view(),
                            rx.cond(
                                TabState.choice == "clients",
                                clients_view()
                            )
                        )
                    )
                )
            ),
            padding="0.5em",
        ),
        template_columns="1fr 27fr",
        template_rows="1fr 10fr",
        width="calc(100vw - 0em)",
        height="calc(100vh - 0em)",
        gap=2,
        max_width="100vw",
        margin="0",
        bg=DarkThemeColor.BACKGROUND.value,
    )
