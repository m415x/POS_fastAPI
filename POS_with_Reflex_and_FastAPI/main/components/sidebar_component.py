import reflex as rx


def sidebar_component(src: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=f"icons/{src}",
            alt="i",
            width="2.5vw",
            transition="filter 0.1s ease-out",
            # _hover={
            #     "transition_duration": "0.3s",
            #     "filter": "invert(70%)",
            # },
            style={
                ":hover": {
                    "transition_duration": "0.3s",
                    "filter": "invert(70%)",
                },
                ":active": {
                    "filter": "invert(100%)",
                },
            },  # type: ignore
        ),
        href="#",
    )
