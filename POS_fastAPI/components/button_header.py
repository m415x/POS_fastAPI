import reflex as rx


def button_header(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.span(
                text,
                position="relative",
                z_index="1",
            ),
            position="relative",
            overflow="hidden",
            height="3rem",
            padding="0 2rem",
            border_radius="1.5rem",
            background="#3d3a4e",
            background_size="400%",
            color="#fff",
            border="none",
            _hover={
                "::before": {
                    "transform": "scaleX(1)"
                }
            },
            _before={
                "content": "''",
                "position": "absolute",
                "top": "0",
                "left": "0",
                "transform": "scaleX(0)",
                "transform_origin": "0 50%",
                "width": "100%",
                "height": "inherit",
                "border_radius": "inherit",
                "background": """linear-gradient(
                    82.3deg,
                    rgba(150, 93, 233, 1) 10.8%,
                    rgba(99, 88, 238, 1) 94.3%
                )""",
                "transition": "all 0.475s",
            }
        ),
        href=url,
    )
