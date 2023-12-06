import reflex as rx


def sidebar_component(src: str) -> rx.Component:
    return rx.image(
        src=f"icons/{src}",
        alt="i",
        h="2.5vw",
        transition="filter 0.1s ease-out",
        style={
            ":hover": {
                "transition_duration": "0.3s",
                "filter": "invert(70%)",
            },
            ":active": {
                "filter": "invert(100%)",
            },
        },  # type: ignore
    )
