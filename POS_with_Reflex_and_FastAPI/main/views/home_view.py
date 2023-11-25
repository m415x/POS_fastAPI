import reflex as rx

# import panels


# import styles


def home_view() -> rx.Component:
    return rx.grid(
        template_columns="repeat(27, 1fr)",
        template_rows="repeat(11, 1fr)",
        # width="calc(100vw - 1fr)",
        # height="100vh",
        gap=2,
        # max_width="100vw",
        # padding="0.5em",
        # margin="0",
    )
