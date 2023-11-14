import reflex as rx


def product_item() -> rx.Component:
    return rx.card(
        rx.text("Body of the Card Component"),
        header=rx.heading("Header", size="lg"),
        footer=rx.heading("Footer", size="sm"),
        width="95%"
    )
