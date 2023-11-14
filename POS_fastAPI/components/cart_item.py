import reflex as rx


def cart_item() -> rx.Component:
    return rx.table_container(
        rx.table(
            caption="",
            headers=["Item", "Cant", "Precio", "Neto"],
            rows=[
                ("Pinza", 1, 5000, 5000),
                ("Clavo", 20, 10, 200),
                ("Foco", 3, 700, 2100),
            ],
            footers=["", "", "", ""],
            # footers=["", 24, "", 7300],
            # variant="striped",
        )
    )
