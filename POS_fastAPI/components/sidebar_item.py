import reflex as rx


def sidebar_item(src: str) -> rx.Component:
    return rx.image(
        src=f"icons/{src}",
        width="2.5vw",
        # 111111
        filter="invert(0%) sepia(3%) saturate(3497%) hue-rotate(320deg) brightness(97%) contrast(87%)",
        transition="filter 1.5s ease",
        _hover={
            "src": "icons/add.svg",
            # ffffff
            "filter": "invert(98%) sepia(98%) saturate(7%) hue-rotate(146deg) brightness(101%) contrast(104%)",
        },
    )
