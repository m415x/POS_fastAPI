import reflex as rx


def sidebar_item(src: str) -> rx.Component:
    return rx.image(
        src=f"icons/{src}",
        width="2.5vw",
        transition="filter 0.5s ease",
        _hover={
            "src": "icons/add.svg",
            # ffffff
            "filter": "invert(98%) sepia(98%) saturate(7%) hue-rotate(146deg) brightness(101%) contrast(104%)",
        },
    )
