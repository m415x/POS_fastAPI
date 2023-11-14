import reflex as rx


def sidebar_button(src: str) -> rx.Component:
    return rx.image(
        src=f"icons/{src}",
        width="3vw",
        filter="invert(14%) sepia(9%) saturate(13%) hue-rotate(342deg) brightness(105%) contrast(82%)",
        transition="filter 0.5s ease",
        _hover={
            "filter": "invert(98%) sepia(98%) saturate(7%) hue-rotate(146deg) brightness(101%) contrast(104%)"
        },
    )
